from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routes import chat_router , auth_router


app=FastAPI()
app.mount("/static", StaticFiles(directory="templates", html=True))



app.include_router(auth_router)
app.include_router(chat_router)



app.add_middleware(
      CORSMiddleware,
      allow_origins=['http://localhost:3000'],
      allow_credentials=True,
      allow_methods=['*'],
      allow_headers=['*']
)