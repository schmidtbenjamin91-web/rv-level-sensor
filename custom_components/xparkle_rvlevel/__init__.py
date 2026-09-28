"""RV Level Sensor integration."""
from __future__ import annotations

from pathlib import Path

from homeassistant.components.frontend import add_extra_js_url, remove_extra_js_url
from homeassistant.components.http import StaticPathConfig
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .coordinator import RVLevelCoordinator

PLATFORMS = ["sensor", "button", "binary_sensor"]
STATIC_URL = "/rv-level-sensor"
CARD_URL = f"{STATIC_URL}/rv-level-card.js?v=1.0.0"
FRONTEND_DIR = Path(__file__).parent / "frontend"
DATA_FRONTEND_REGISTERED = "xparkle_rvlevel_frontend_registered"

async def async_update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Reload when vehicle dimensions are changed."""
    await hass.config_entries.async_reload(entry.entry_id)

async def _async_register_frontend(hass: HomeAssistant) -> None:
    """Serve and auto-load the bundled dashboard card."""
    if hass.data.get(DATA_FRONTEND_REGISTERED):
        return
    await hass.http.async_register_static_paths([
        StaticPathConfig(STATIC_URL, str(FRONTEND_DIR), False)
    ])
    add_extra_js_url(hass, CARD_URL)
    hass.data[DATA_FRONTEND_REGISTERED] = True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    await _async_register_frontend(hass)
    coordinator = RVLevelCoordinator(hass, entry)
    entry.runtime_data = coordinator
    entry.async_on_unload(entry.add_update_listener(async_update_listener))
    await coordinator.async_start()
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        await entry.runtime_data.async_stop()
    return unload_ok
