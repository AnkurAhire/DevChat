
class WEBSOCKET:

    def __init__(self,user_id,websocket):
        self.websocket=websocket
        self.user_id=user_id

    async def connect(self):
        await self.websocket.accept()

    async def disconnect(self):
        await self.websocket.close()
