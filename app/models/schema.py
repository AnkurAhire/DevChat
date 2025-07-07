from pydantic import BaseModel,Field , field_validator


class UserBase(BaseModel):
    username: str=Field(..., min_length=4 , max_length=50 , description="Username  must contain Atleast 4 characters" , examples=["Ankur"] )
    password: str=Field(..., min_length=4, max_length=50 , description="Password must contain atleast 4 characters" , examples=["2643"] )


class MessageBase(BaseModel):
    content: str
    sender_id: str
    receiver_id: str

