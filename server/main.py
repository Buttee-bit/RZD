import os
from fastapi import FastAPI, File, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import requests
import cv2

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import requests


app = FastAPI()
import aiohttp
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8081"],  # Укажите домен или порт, с которого разрешены запросы
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# @app.post("/process-video")
# async def process_video(url: str, video_file: bytes = File('temp_video.mp4')):
#     # Загрузка видео с удаленного сайта
#     response = requests.get(url, stream=True)
#     response.raise_for_status()

#     # Сохранение видео во временный файл
#     with open("temp_video.mp4", "wb") as file:
#         for chunk in response.iter_content(chunk_size=8192):
#             file.write(chunk)

#     # Открытие видео с помощью OpenCV
#     video = cv2.VideoCapture("temp_video.mp4")

#     # Обработка каждого кадра видео
#     while True:
#         ret, frame = video.read()

#         if not ret:
#             break

#         # Обработка кадра видео

#     # Закрытие видео
#     video.release()

#     # Удаление временного файла
#     os.remove("temp_video.mp4")

#     # Возвращение результата обработки видео
#     return {"status": "Video processed successfully"}

@app.get("/video")
async def stream_video():
    cap = cv2.VideoCapture('http://46.14.77.226:8880/mjpg/video.mjpg')
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        _, img_encoded = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + img_encoded.tobytes() + b'\r\n')

@app.get("/")
async def root():
    return {"message": "Hello World"}