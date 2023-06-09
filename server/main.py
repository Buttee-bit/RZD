import os
from fastapi import FastAPI, File, Response, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import requests
import cv2
from bs4 import BeautifulSoup

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


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

# @app.get("/video-stream1")
# def get_video_stream1():
#     try:
#         url = "https://176.99.128.10/embed/7"  # Замените на нужный URL видеопотока
#         response = requests.get(url, verify=False)
#         html_content = response.text

#             # Используем BeautifulSoup для парсинга HTML
#         soup = BeautifulSoup(html_content, "html.parser")

#             # Находим ссылку на видеопоток
#         video_element = soup.find('video')
#         video_url = video_element['src']
#         print(video_url)
#         # video_url = soup.find("video").source["src"]


#             # Загружаем видеопоток и передаем его в ответе FastAPI
#         response = requests.get(video_url, stream=True,verify=False)
#         return Response(response.iter_content(chunk_size=1024), media_type="video/mp4")
#     except:
#         print(video_element)
#         pass
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.get("/blob")
# def get_blob():
#     url = "https://176.99.128.10/54b11939-abf3-44dc-bd96-e1242ed4d20f"
#     response = requests.get(url, stream=True, verify=False)

#     headers = {
#         "Content-Type": response.headers.get("Content-Type"),
#         "Content-Disposition": response.headers.get("Content-Disposition"),
#     }

#     content_parts = []
#     for chunk in response.iter_content(chunk_size=1024):
#         content_parts.append(chunk)

#     content = b"".join(content_parts)

#     return Response(content=content, headers=headers)




# @app.get("/video")
# def get_video_stream():
#     url = "http://46.14.77.226:8880/mjpg/video.mjpg"
#     response = requests.get(url, stream=True)

#     # Set the appropriate content type for the video
#     headers = {
#         "Content-Type": "multipart/x-mixed-replace; boundary=frame"
#     }

#     # Create a generator function to stream the video content
#     def stream_video():
        
#         for chunk in response.iter_content(chunk_size=512):
#             print(chunk)
#             yield chunk

#     # Return the streaming response
#     return StreamingResponse(stream_video(), headers=headers)

@app.get("/video-stream")
def get_video_stream():
    url = "http://46.14.77.226:8880/mjpg/video.mjpg"
    response = requests.get(url, stream=True)
    print(response)

    # Set the appropriate content type for the video
    headers = {
        "Content-Type": "video/mjpeg"
    }

    content = b"".join(response.iter_content(chunk_size=None))

    # Возвращаем видеопоток в качестве ответа
    print(content)
    return Response(content=content, headers=headers)