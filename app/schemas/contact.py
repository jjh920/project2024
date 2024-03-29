from datetime import datetime

from pydantic import BaseModel


class Contact(BaseModel):
    cno: int
    title: str
    userid: str
    regdate: datetime
    views: int
    contents: str

    class Config:
        from_attributes = True


class NewContact(BaseModel):
    title: str
    userid: str
    contents: str
    response: str




