from pydantic_settings import BaseSettings, SettingsConfigDict


class SBAISettings(BaseSettings):
    environment: str = "development"
    service_name: str = "api-gateway"
    service_version: str = "0.1.0"
    debug: bool = False

    model_config = SettingsConfigDict(
        env_prefix="SBAI_",
        case_sensitive=False,
    )


settings = SBAISettings()
