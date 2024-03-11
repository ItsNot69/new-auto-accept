from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "28726816"))
    API_HASH = getenv("API_HASH", "45edf74203ecf6ff14b394a9e47dca34")
    BOT_TOKEN = getenv("BOT_TOKEN", "6891263386:AAGdH44TNWeShyBn0qma1DEcpXBAAGksl9A")
    FSUB = getenv("FSUB", "born4movies7")
    CHID = int(getenv("CHID", "-1001654163482"))
    SUDO = list(map(int, getenv("SUDO", "5521380948").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://m0921594:Rohit44@cluster0.qbze22i.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()
