import configparser


class ConfigParser:
    def __init__(self, config_path: str):
        self._config_path = config_path
        self._config = self._read_config()

    def _read_config(self):
        config = configparser.ConfigParser()
        with open(self._config_path, 'r') as file:
            config.read_file(file)
        return config

    def get_value(self, section: str, option: str):
        return self._config.get(section, option)
