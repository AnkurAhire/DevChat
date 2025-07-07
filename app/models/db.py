from sqlalchemy import create_engine,text


class DevDB:
    __url="mysql+mysqlconnector://root:@localhost:3306/DevChatDB"
    __engine=create_engine(__url)
  
    def Select(self,query,data):
            with self.__engine.connect() as conn:
                result=conn.execute(text(query),data)
                row=result.fetchone()

            return dict(row._mapping) if row else None
    
    
    def Insert(self,query,data):
        with self.__engine.connect() as conn:
              conn.execute(text(query),data)
              conn.commit()


    def Delete(self,query,data):
        with self.__engine.connect() as conn:
              conn.execute(text(query),data)
              conn.commit()

              
