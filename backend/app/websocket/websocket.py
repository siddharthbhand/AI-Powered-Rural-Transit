from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.websocket.connection_manager import ConnectionManager

router = APIRouter()

manager = ConnectionManager()

connection_manager = manager


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await manager.connect(websocket)

    try:
        while True:

            data = await websocket.receive_text()

            await manager.broadcast(
                f"Message: {data}"
            )

    except WebSocketDisconnect:

        manager.disconnect(websocket)