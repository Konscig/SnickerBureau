from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn


class Settings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWD: str
    POSTGRES_DB: str

    @property
    def POSTGRES_DSN(self) -> PostgresDsn:
        return (
            f'postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWD}'
            f'@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}'
            f'/{self.POSTGRES_DB}'
        )

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
