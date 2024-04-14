# Simple WebSockets Brocaster
import asyncio
import websockets

# A set to store all connected clients
clients = set()  # type: Set[websockets.WebSocketServerProtocol]

# Handler function for socket message activities
async def handler(websocket, path):
    # Add the new client to the set of clients only if it's not already present
    if websocket not in clients:
        clients.add(websocket)  # add new client to the set

    # Listen for messages from the client
    async for message in websocket:
        print(message, 'received from client')  # print to console
        await brocast(message)  # send message to all clients

    # Remove the client from the set when it disconnects
    clients.remove(websocket)


# Function to brocast message to all clients
async def brocast(message):
    for client in clients:
        if client.open:
            await client.send(message)
