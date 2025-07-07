from fastapi import APIRouter, HTTPException, WebSocket
from service import WS,RG
from security import secure


router=APIRouter(prefix="", tags=["Chat"])
rg=RG()

@router.websocket("/chat")
async def handle_chat(websocket:WebSocket):
      try:

            user_id=secure.get_userid(websocket)
            ws=WS(user_id,websocket)

            await ws.connect()
            rg.Register_user(user_id,websocket)
            rg.show()


            while True:
                  try:
                        message= await websocket.receive_json()
                        await rg.unicast_message(message)
                  except Exception as e:
                        print(f"ERROR {e}")
                        break

      except Exception as e:
            raise HTTPException(detail=e)     
      finally:
            await ws.disconnect()
            rg.unregister_user(user_id)