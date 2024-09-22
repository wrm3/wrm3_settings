# WRM3 Settings

WRM3 Settings is a Python module for managing configuration settings in JSON format. It provides an easy-to-use interface for loading, updating, and accessing settings with attribute-style dict functionality.

## Features

- Load and save settings from/to JSON files
- Access settings using dot notation
- Override default values
- Automatic creation of settings file if not present

## Installation

You can install WRM3 Settings using pip:
    pip install wrm3-settings

## Usage

Here's a quick example of how to use WRM3 Settings:

python
from wrm3_settings import Settings
Initialize settings with a template
settings_template = {
"app_name": "MyApp",
"version": "1.0.0",
"debug": True
}
settings = Settings('settings.json', settings_template)
Access settings
print(settings.kv.app_name) # Output: MyApp
print(settings.kv.version) # Output: 1.0.0
Update settings
settings.kv.debug = False
Save settings
settings.file_write(settings.kv)



For more detailed usage instructions and examples, please refer to the [documentation](docs/usage.md).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
