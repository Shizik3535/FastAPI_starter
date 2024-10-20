from pydantic import BaseModel


class BaseSchema(BaseModel):
    status: str
    message: str
    data: dict | None

    class Config:
        orm_mode = True

    @classmethod
    def success(cls, message: str, data: dict | None = None):
        return cls(status="success", message=message, data=data)

    @classmethod
    def warning(cls, message: str, data: dict | None = None):
        return cls(status="warning", message=message, data=data)

    @classmethod
    def info(cls, message: str, data: dict | None = None):
        return cls(status="info", message=message, data=data)

    @classmethod
    def error(cls, message: str, data: dict | None = None):
        return cls(status="error", message=message, data=data)
