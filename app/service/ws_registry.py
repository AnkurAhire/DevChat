

class Registry:
    __active_connections={}
    
    def Register_user(self,user_id,websocket):
        self.__active_connections[user_id]=websocket
    
    def unregister_user(self,user_id):
        if user_id in self.__active_connections:
            del self.__active_connections[user_id]
    
    def  show(self):
        print(self.__active_connections.items())

    async def unicast_message(self,meassage):
        to_user=meassage["to"]
        content=meassage["content"]

        if to_user not in  self.__active_connections:
            print("USER NOT FOUND")
            return
        
        await self.__active_connections[to_user].send_text(content)
        