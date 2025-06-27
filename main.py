from fastapi import FastAPI,Request,Response,Depends,HTTPException,Form 
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from authentication import Security

app=FastAPI()
secure=Security()
template=Jinja2Templates(directory="templates")




@app.post("/login" , status_code=201, tags=["authentication"])
def handle_login(response:Response,username:str=Form(...),password:str=Form(...)):
     isauthenticated:bool=secure.authenticate_user(username,password)
     if isauthenticated:
           session_id = secure.create_session(username)
           response.set_cookie(
                 key="session_id",
                 value=session_id,
                 httponly=True,
                 samesite="strict"
           )

           return{"SUCCESFULL LOGIN"}
     else:
            raise HTTPException(status_code=401 , detail="INVALID REQUEST")
     


@app.post("/register" , status_code=201, tags=["authentication"])
def handle_registeration(username:str=Form(...) , password:str=Form(...)):
      if (username and password ) and secure.register_user(username,password):
            return{"succesful"}
      else:
            return {"unsucessful"}
      








       
      










app.add_middleware(
      CORSMiddleware,
      allow_origins=['http://localhost:3000'],
      allow_credentials=True,
      allow_methods=['*'],
      allow_headers=['*']
)