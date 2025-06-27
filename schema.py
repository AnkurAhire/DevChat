from pydantic import BaseModel,Field    


class UserBase(BaseModel):
    user_id:str
    username: str=Field(..., min_length=1 , max_length=10)
    password: str=Field(..., min_length=6, max_length=20)
    is_active: bool = False 

class MessageBase(BaseModel):
    content: str
    sender_id: str
    receiver_id: str

