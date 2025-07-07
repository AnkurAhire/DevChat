from sqlalchemy import create_engine,text
from dotenv import load_dotenv
import os



load_dotenv()

class DevDB:
    _USER = os.getenv("DB_USER")
    _PASSWORD = os.getenv("DB_PASSWORD")
    _HOST = os.getenv("DB_HOST")
    _PORT = os.getenv("DB_PORT")
    _DBNAME = os.getenv("DB_NAME")
    _DATABASE_URL = f"postgresql+psycopg2://{_USER}:{_PASSWORD}@{_HOST}:{_PORT}/{_DBNAME}?sslmode=require"
    _engine=create_engine(_DATABASE_URL)
  
    def Select(self,query,data):
            with self._engine.connect() as conn:
                result=conn.execute(text(query),data)
                row=result.fetchone()

            return dict(row._mapping) if row else None
    
    
    def Insert(self,query,data):
        with self._engine.connect() as conn:
              conn.execute(text(query),data)
              conn.commit()


    def Delete(self,query,data):
        with self._engine.connect() as conn:
              conn.execute(text(query),data)
              conn.commit()

              
