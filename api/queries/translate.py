from pydantic import BaseModel


class Translation(BaseModel):
    text: str
    target_lang: str
