from pydantic.dataclasses import dataclass
from src.utils.config_loader.read_json import JsonConfigReader
from src.utils.config_loader.read_yaml import YamlConfigReader

@dataclass
class ConfigReaderInstance:
    json = JsonConfigReader()
    yaml = YamlConfigReader()