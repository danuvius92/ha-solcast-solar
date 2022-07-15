"""Config flow for Solcast Solar integration."""
from __future__ import annotations

from typing import Any

import voluptuous as vol
from homeassistant.config_entries import ConfigEntry, ConfigFlow, OptionsFlow
from homeassistant.const import CONF_API_KEY, CONF_ELSE
from homeassistant.core import callback
from homeassistant.data_entry_flow import FlowResult

from .const import DOMAIN

class SolcastSolarFlowHandler(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Solcast Solar."""

    VERSION = 2

    @staticmethod
    @callback
    def async_get_options_flow(
        config_entry: ConfigEntry,
    ) -> SolcastSolarOptionFlowHandler:
        """Get the options flow for this handler."""
        return SolcastSolarOptionFlowHandler(config_entry)

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle a flow initiated by the user."""
        if user_input is not None:
            return self.async_create_entry(
                title= "Solcast Solar", 
                data = {},
                options={
                    CONF_API_KEY: user_input[CONF_API_KEY],
                    CONF_ELSE: user_input[CONF_ELSE],
                },
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_API_KEY, default=""): str,
                    vol.Required(CONF_ELSE, default="2"): int,
                }
            ),
        )


class SolcastSolarOptionFlowHandler(OptionsFlow):
    """Handle options."""

    def __init__(self, config_entry: ConfigEntry) -> None:
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="Solcast Solar", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_API_KEY,
                        CONF_ELSE,
                        default=self.config_entry.options.get(CONF_API_KEY, CONF_ELSE),
                    ): str,
                }
            ),
        )
