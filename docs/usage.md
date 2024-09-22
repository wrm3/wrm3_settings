# WRM3 Settings Usage Guide

This guide provides detailed instructions on how to use the WRM3 Settings module.

## Installation

You can install WRM3 Settings using pip:
bash
pip install wrm3-settings



## Basic Usage

Here's a basic example of how to use WRM3 Settings:


python
from wrm3_settings import Settings
Define a settings template
settings_template = {
"edited_yn": "N",
"some_setting_name": "some_setting_value",
"some_setting_thats_an_int": 15,
"some_setting_thats_a_float": 15.51,
"some_setting_thats_a_list": ["DAI", "GUSD", "PAX", "PYUSD", "USD", "USDC", "USDT"],
"some_setting_thats_a_dict": {
"trade_yn": "Y",
"trade_live_yn": "Y",
}
}
Initialize settings
settings = Settings('settings/settings.json', settings_template)
Load or reload settings
st = settings.reload()
Access settings
print(st.edited_yn)
print(st.some_setting_name)
print(st.some_setting_thats_an_int)
print(st.some_setting_thats_a_float)
print(st.some_setting_thats_a_list)
print(st.some_setting_thats_a_dict.trade_yn)
You can also access settings using dictionary notation
print(st['edited_yn'])
print(st['some_setting_thats_a_dict']['trade_yn'])




## Advanced Usage

### Default Overrides

You can use the `get_ovrd` method to provide default overrides:


python
settings_with_override = {
"": -1,
"BTC": 42,
"ETH": 123,
"SOL": 57,
"USDC": 99
}
Get value for BTC
btc_value = settings.get_ovrd(in_dict=settings_with_override, in_key='BTC')
print(btc_value) # Output: 42
Get value for a non-existent key (will return the default value)
xxx_value = settings.get_ovrd(in_dict=settings_with_override, in_key='XXX')
print(xxx_value) # Output: -1

### Multiple Settings Objects

You can have multiple settings objects running simultaneously:


python
buy_settings = Settings('some_folder/buy_settings.json', buy_template_json)
sell_settings = Settings('some_folder/sell_settings.json', sell_template_json)
log_settings = Settings('log_settings.json', log_template_json)
buy_st = buy_settings.reload()
sell_st = sell_settings.reload()
log_st = log_settings.reload()

## Error Handling

If the settings file becomes invalid JSON, the module will create a dated backup of your file before replacing it with a blank template. This prevents data loss in case of file corruption.

## Best Practices

1. Always use the `reload()` method to ensure you have the latest settings, especially in long-running scripts.
2. Use descriptive names for your settings to make the configuration more intuitive.
3. Group related settings together in nested dictionaries for better organization.
4. Regularly back up your settings files, especially before making significant changes.





