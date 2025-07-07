import uuid
from fastapi import Request,WebSocket,HTTPException
from passlib.context import CryptContext
from http.cookies import SimpleCookie
from models import devdb




class SECURITY:
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
            if devdb.Select("SELECT * FROM users WHERE username=:username", {"username":username}):
                return False
            else:
                 devdb.Insert("INSERT INTO users (user_id,username,password) values (:user_id,:username,:password)",{"user_id":self.generate_unique_id(),"username":username,"password": self.get_password_hash(password)})
                 return True

    def  authenticate_user(self,username:str,password:str) -> bool :
        user=devdb.Select("SELECT * FROM users WHERE username=:username", {"username":username})
        if user and self.verify_password_hash(password,user["password"]):
            return True
        return False

    def create_session(self,username:str):
        session_id=self.generate_unique_id()
        user_id=devdb.Select("SELECT user_id FROM users WHERE username=:username", {"username":username})
        devdb.Insert("INSERT INTO dev_sessions (session_id,user_id) VALUES (:session_id,:user_id)",{"session_id":session_id, "user_id":user_id["user_id"]})
        return session_id
    
    def delete_session_fromDB(self,request)-> bool:
        session_id=request.cookies.get("session_id")

        if session_id:
            try:
                devdb.Delete("DELETE FROM dev_sessions WHERE session_id=:session_id",{"session_id":session_id})
            except:
                return False
            
            return True
    
        return False
            
            
        
    def get_userid(self,conn):

        session_id=None

        
        if isinstance(conn , Request):
            session_id=conn.cookies.get("session_id")
            
        elif isinstance(conn, WebSocket):
            session_id = conn.cookies.get("session_id")
            
        if session_id:
            result=devdb.Select(("SELECT user_id FROM dev_sessions WHERE session_id=:sid"), {"sid":session_id})
            return result["user_id"]
        
     
            

        
        
        

        
         
         
         
         


        
        

    