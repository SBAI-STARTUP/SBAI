from pydantic import BaseModel


class ServiceMetadata(BaseModel):
    service: str
    version: str
