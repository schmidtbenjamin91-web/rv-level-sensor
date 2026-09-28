"""Buttons for RV Level Sensor."""
from __future__ import annotations

from homeassistant.components.button import ButtonEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import CONNECTION_BLUETOOTH, DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .coordinator import RVLevelCoordinator

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    coordinator: RVLevelCoordinator = entry.runtime_data
    # Explicit list: all three entities are instantiated on every platform setup.
    async_add_entities([
        RVLevelActionButton(coordinator, "read_now", "Read BLE values now"),
        RVLevelActionButton(coordinator, "connect", "Connect"),
        RVLevelActionButton(coordinator, "disconnect", "Disconnect"),
    ], update_before_add=False)

class RVLevelActionButton(ButtonEntity):
    _attr_has_entity_name = True

    def __init__(self, coordinator: RVLevelCoordinator, key: str, name: str) -> None:
        self.coordinator = coordinator
        self._key = key
        self._attr_name = name
        self._attr_unique_id = f"{coordinator.address}_{key}"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, coordinator.address)},
            connections={(CONNECTION_BLUETOOTH, coordinator.address)},
            name=coordinator.name,
            manufacturer="RVLevel compatible",
            model="RV Level 410 / RVS01",
        )

    async def async_press(self) -> None:
        if self._key == "connect":
            await self.coordinator.async_connect()
        elif self._key == "disconnect":
            await self.coordinator.async_disconnect()
        else:
            await self.coordinator.async_read_now()
