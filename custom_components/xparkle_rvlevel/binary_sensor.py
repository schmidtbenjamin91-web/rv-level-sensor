"""Connection binary sensor for RV Level Sensor."""
from __future__ import annotations
from homeassistant.components.binary_sensor import BinarySensorEntity, BinarySensorDeviceClass
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.device_registry import CONNECTION_BLUETOOTH, DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from .const import DOMAIN
from .coordinator import RVLevelCoordinator, SIGNAL_UPDATE

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    async_add_entities([RVLevelConnection(entry.runtime_data)])

class RVLevelConnection(BinarySensorEntity):
    _attr_has_entity_name = True
    _attr_name = "Bluetooth connection"
    _attr_device_class = BinarySensorDeviceClass.CONNECTIVITY

    def __init__(self, coordinator: RVLevelCoordinator) -> None:
        self.coordinator = coordinator
        self._attr_unique_id = f"{coordinator.address}_connected"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, coordinator.address)},
            connections={(CONNECTION_BLUETOOTH, coordinator.address)},
            name=coordinator.name, manufacturer="RVLevel compatible",
            model="RV Level 410 / RVS01",
        )

    @property
    def is_on(self):
        return self.coordinator.state.connected

    @property
    def extra_state_attributes(self):
        return {
            "auto_disconnect_remaining": self.coordinator.state.auto_disconnect_remaining,
            "auto_disconnect_seconds": self.coordinator._auto_disconnect_seconds,
            "connection_enabled": self.coordinator._connection_enabled,
        }

    async def async_added_to_hass(self):
        self.async_on_remove(async_dispatcher_connect(self.hass, SIGNAL_UPDATE, self._update))

    @callback
    def _update(self, address):
        if address == self.coordinator.address:
            self.async_write_ha_state()
