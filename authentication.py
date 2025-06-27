import uuid
from db import DevDB
from passlib.context import CryptContext




class Security:

    __db=DevDB()
    __pwd_context=CryptContext(schemes=["bcrypt"] , deprecated="auto")

    def __init__(self):
         pass
    
    def generate_unique_id(self):
         return str(uuid.uuid4())
         

    def get_password_hash(self,password:str):
        return self.__pwd_context.hash(password)
    
    def verify_password_hash(self,plain_password, hashed_password)-> bool:
        return self.__pwd_context.verify(plain_password,hashed_password)
    
        
    def register_user(self,username:str,password:str) -> bool:
            if self.__db.Select("SELECT * FROM users WHERE username=:username", {"username":username}):
                return False
            else:
                 self.__db.Insert("INSERT INTO users (user_id,username,password) values (:user_id,:username,:password)",{"user_id":self.generate_unique_id(),"username":username,"password": self.get_password_hash(password)})
                 return True

    def  authenticate_user(self,username:str,password:str) -> bool :
        user=self.__db.Select("SELECT * FROM users WHERE username=:username", {"username":username})
        if user and self.verify_password_hash(password,user["password"]):
            return True
        return False

    def create_session(self,username:str):
        session_id=self.generate_unique_id()
        self.__db.Insert("INSERT INTO dev_sessions (session_id,username) VALUES (:session_id,:username)",{"session_id":session_id, "username":username})
        return session_id

        
        

    