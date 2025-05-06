import os
from pathlib import Path
from typing import Optional, Dict, Any

from pydantic import Field, BaseModel
from pydantic_settings import BaseSettings

from src.utils import ConfigReaderInstance


class AppConfig(BaseModel):
    """Application configurations."""

    BASE_DIR: Path = Path(__file__).resolve().parent.parent

    SETTINGS_DIR: Path = BASE_DIR / "settings"
    SETTINGS_DIR.mkdir(parents=True, exist_ok=True)

    LOGS_DIR: Path = BASE_DIR / "logs"
    LOGS_DIR.mkdir(parents=True, exist_ok=True)

    MODELS_DIR: Path = BASE_DIR / "models"
    MODELS_DIR.mkdir(parents=True, exist_ok=True)

    BI_ENCODER_PATH: str = str(MODELS_DIR / "vietnamese-sbert")

    CACHE_DIR: Path = BASE_DIR / "cache"
    CACHE_DIR.mkdir(parents=True, exist_ok=True)


class GlobalConfig(BaseSettings):
    """Global configurations."""

    APP_CONFIG: AppConfig = AppConfig()

    API_NAME: Optional[str] = Field(None, env="API_NAME")
    API_DESCRIPTION: Optional[str] = Field(None, env="API_DESCRIPTION")
    API_VERSION: Optional[str] = Field(None, env="API_VERSION")
    API_DEBUG_MODE: Optional[bool] = Field(None, env="API_DEBUG_MODE")
    API_KEY: Optional[str] = Field(None, env="API_KEY")

    LOG_CONFIG_FILENAME: Optional[str] = Field(None, env="LOG_CONFIG_FILENAME")
    DEV_HOST: Optional[str] = Field(None, env="DEV_HOST")
    DEV_PORT: Optional[str] = Field(None, env="DEV_PORT")
    LANGSMITH_API_KEY: Optional[str] = Field(None, env="LANGSMITH_API_KEY")

    ENV_STATE: Optional[str] = Field("dev", env="ENV_STATE")
    LOG_LEVEL: Optional[str] = Field(None, env="LOG_LEVEL")
    PYTHONPATH: Optional[str] = Field(None, env="PYTHONPATH")  # Allow PYTHONPATH explicitly

    HOST: Optional[str] = None
    PORT: Optional[str] = None

    MONGO_CONF: Dict[str, Any] = ConfigReaderInstance.yaml.read_config_from_file(
        "example/ava_example/settings/mongo.yaml")
    API_CONF: Dict[str, Any] = ConfigReaderInstance.yaml.read_config_from_file(
        "example/ava_example/settings/api.yaml")
    ELK_CONF: Dict[str, Any] = ConfigReaderInstance.yaml.read_config_from_file(
        "example/ava_example/settings/elk_logging.yaml")
    LLM_CONF: Dict[str, Any] = ConfigReaderInstance.yaml.read_config_from_file(
        "example/ava_example/settings/llm.yaml")
    LANGFUSE_CONF: Dict[str, Any] = ConfigReaderInstance.yaml.read_config_from_file(
        "example/ava_example/settings/langfuse.yaml")
    DIFY_CONF: Dict[str, Any] = ConfigReaderInstance.yaml.read_config_from_file(
        "example/ava_example/settings/dify.yaml")
    AVA_CORE_CONF: Dict[str, Any] = ConfigReaderInstance.yaml.read_config_from_file(
        "example/ava_example/settings/ava_core.yaml")

    WORKFLOWS: Dict[str, Any] = DIFY_CONF.get("workflows", {})
    WORKFLOW_URL: str = DIFY_CONF.get("workflow_url", "")

    MISA_CRM_SEARCH_KNOWLEDGE_API_KEY: Optional[str] = Field(None, env="MISA_CRM_SEARCH_KNOWLEDGE_API_KEY")
    MISA_CRM_SEARCH_KNOWLEDGE_CONF: Dict[str, Any] = DIFY_CONF.get("misa_crm_search_knowledge", {})

    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "forbid"  # Prevent loading unexpected env vars unless defined


class DevConfig(GlobalConfig):
    class Config:
        env_prefix = "DEV_"


class ProdConfig(GlobalConfig):
    class Config:
        env_prefix = "PROD_"


class FactoryConfig:
    def __init__(self, env_state: Optional[str]):
        self.env_state = env_state

    def __call__(self):
        if self.env_state == "dev":
            return DevConfig()
        elif self.env_state == "prod":
            return ProdConfig()
        else:
            raise ValueError(f"Unsupported ENV_STATE: {self.env_state}")


settings = FactoryConfig(GlobalConfig().ENV_STATE)()
