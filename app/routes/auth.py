from fastapi import APIRouter,Request,Response,Form
from fastapi.responses import JSONResponse
from security import secure
from models import UserBase

router=APIRouter(prefix="/api" , tags=["Auth"])


@router.post("/login" , tags=["Auth"])
def handle_login(response:Response, user:UserBase=Form(...)):
     isauthenticated:bool=secure.authenticate_user(user.username,user.password)
     if isauthenticated:
           session_id = secure.create_session(user.username)
           response.set_cookie(
                 key="session_id",
                 value=session_id,
                 httponly=True,
                 samesite="strict"
           )
           return {"success":True}
     
     return JSONResponse({"success":False, "message":"Invalid_Credentials"}, status_code=401)
     


@router.post("/register" , tags=["Auth"])
def handle_registeration(username:str=Form(...) , password:str=Form(...)):
      if (username and password ) and secure.register_user(username,password):
            return JSONResponse({"success":True})
      else:
              return JSONResponse({"success":False,"message":"Registration_Failed"}, status_code=400)
      

@router.delete("/logout" , tags=["Auth"])
def handle_logout(request:Request,response:Response):

      isSessionRemoved:bool= secure.delete_session_fromDB(request)

      if isSessionRemoved:
            response.delete_cookie("session_id")
            return JSONResponse({"success":True})
      else:
            return JSONResponse({"success":False,"message":"Session_Not_Found"}, status_code=400)



@router.get("/user_id")
def get_user(request:Request):
      return{secure.get_userid(request)}
