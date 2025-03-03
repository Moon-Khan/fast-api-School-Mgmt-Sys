from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "YOUR_MONGO_URI"
client = AsyncIOMotorClient(MONGO_URI)

database = client["SchoolSys"]

