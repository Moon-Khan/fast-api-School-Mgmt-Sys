from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb+srv://mamoonkhan:EFKKjfzN1REexVGn@cluster0.kravb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = AsyncIOMotorClient(MONGO_URI)

database = client["SchoolSys"]

