from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.websocket.connection_manager import ConnectionManager


router = APIRouter()

manager = ConnectionManager()


@router.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket,
):
    await manager.connect(websocket)

    try:
        while True:

            data = await websocket.receive_text()

            await manager.send_personal_message(
                f"You wrote: {data}",
                websocket,
            )

    except WebSocketDisconnect:

        manager.disconnect(websocket)