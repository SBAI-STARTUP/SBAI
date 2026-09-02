from sbai_api_gateway.core.config import SBAISettings


def test_default_debug_is_disabled():
    settings = SBAISettings()
    assert settings.debug is False


def test_environment_configuration(monkeypatch):
    monkeypatch.setenv("SBAI_ENVIRONMENT", "production")

    settings = SBAISettings()

    assert settings.environment == "production"


def test_debug_can_be_enabled_explicitly(monkeypatch):
    monkeypatch.setenv("SBAI_DEBUG", "true")

    settings = SBAISettings()

    assert settings.debug is True
