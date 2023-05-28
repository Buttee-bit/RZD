from fastapi import FastAPI

app = FastAPI()
import aiohttp


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/video-stream")
async def get_video_stream():
    url = "https://open.ivideon.com/embed/v2/?server=200-4721c6ffcb78953b724c195f01db1168&camera=327680&width=&height=&lang=ru"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.read()
            else:
                return {"error": "Failed to fetch video stream"}