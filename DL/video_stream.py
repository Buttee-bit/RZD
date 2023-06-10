import cv2

def get_video_stream():
    url = 'http://46.14.77.226:8880/mjpg/video.mjpg'
    
    # Открытие видеопотока с помощью OpenCV
    cap = cv2.VideoCapture(url)
    
    while True:
        # Чтение кадра из видеопотока
        ret, frame = cap.read()
        print(ret)
        print(frame)
        pass
        if not ret:
            # Если не удалось прочитать кадр, выход из цикла
            break
        
        # Обработка кадра, если необходимо
        
        # Отображение кадра
        cv2.imshow('Video Stream', frame)
        
        # Ожидание нажатия клавиши 'q' для выхода
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Закрытие видеопотока и окна отображения
    cap.release()
    cv2.destroyAllWindows()
get_video_stream()