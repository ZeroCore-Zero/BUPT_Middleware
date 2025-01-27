import json
import os


class ConfigItem:
    def __init__(self, config: dict):
        self.config = config
        for key in config:
            if not isinstance(self.config[key], dict):
                continue
            self.config[key] = ConfigItem(self.config[key])

    def __getattr__(self, name):
        return self.config.get(name, None)


class Config(ConfigItem):
    def __init__(self, folder_path):
        files = os.listdir(folder_path)
        config = {}
        for file in files:
            with open(os.path.join(folder_path, file)) as f:
                config[file.split(".")[0]] = ConfigItem(json.load(f))
        self.config = config

