"""Switch platform for integration_blueprint."""
from homeassistant.components.button import ButtonEntity
from .mqtt import HAMQTTAutodiscoveryPublish
from .const import DEFAULT_NAME, DOMAIN, ICON, BUTTON


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices([HAMQTTAutodiscoveryButton(coordinator, entry)])


class HAMQTTAutodiscoveryButton(ButtonEntity):
    """HA MQTT Autodiscovery button class."""

    async def async_press(self, **kwargs):  # pylint: disable=unused-argument
        """Turn on the switch."""
        HAMQTTAutodiscoveryPublish()
        await self.coordinator.api.HAMQTTAutodiscoveryPublish()
        await self.coordinator.async_request_refresh()

    @property
    def name(self):
        """Return the name of the button."""
        return f"{DEFAULT_NAME}_{BUTTON}"

    @property
    def icon(self):
        """Return the icon of this button."""
        return ICON