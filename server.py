#simple websockets brocaster
import asyncio
import websockets

# A list to store all connected clients
clients = []  # type: List[websockets.WebSocketServerProtocol]

# Handler function for socket message activities
async def handler(websocket, path):
    #print(path)  # path is not used currently
    
    # Add the new client to the list of clients only if it's not already present
    if websocket not in clients:
        clients.append(websocket)  # append new client to the array

    # Listen for messages from the client
    async for message in websocket:
        print(message, 'received from client')  # print to console
        await brocast(message)  # send message to all clients

