import cv2
import os
import uuid
import threading
import time
from datetime import datetime

def capture_and_save(cap, camera_index, save_folder):    
    start_time = time.time()
    end_time = start_time + 1

    # Obter data e hora atuais
    agora = datetime.now()

    # Extrair a data, hora e segundos
    data_atual = agora.strftime("%Y-%m-%d")
    hora_atual = agora.strftime("%H:%M:%S")

    print("start_time camera:", camera_index)
    print(f"{data_atual} {hora_atual}")

    while start_time <= end_time:
        start_time = time.time()
        # Lê um frame da câmera
        ret, frame = cap.read()

        if ret:
            # Gira o frame em 90 graus
            rotated_frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

            # Salva a imagem
            cv2.imwrite(os.path.join(save_folder, f"webcam{camera_index}_{str(uuid.uuid4())}.jpg"), rotated_frame)

        # Sai do loop quando a tecla 'q' for pressionada
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libera o objeto de captura
    cap.release()

def capture_from_two_cameras(duration=1):
    # Verifica se a pasta "Imagens" existe na área de trabalho
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    save_folder = os.path.join(desktop_path, "Imagens")
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # Cria um semáforo com contagem inicial de zero

    # Inicializa a câmera 1
    cap1 = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Usando DirectShow como backend
    # Define a resolução desejada (1080x720)
    cap1.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
    cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    # Inicializa a câmera 2
    cap2 = cv2.VideoCapture(1, cv2.CAP_DSHOW)  # Usando DirectShow como backend
    # Define a resolução desejada (1080x720)
    cap2.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
    cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    # Inicializa as threads para cada câmera
    thread1 = threading.Thread(target=capture_and_save, args=(cap1, 0, save_folder))
    thread2 = threading.Thread(target=capture_and_save, args=(cap2, 1, save_folder))

    # Inicia as threads
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    # Fecha as janelas
    cv2.destroyAllWindows()

# Chamada da função para capturar vídeo de duas câmeras por 1 segundo
capture_from_two_cameras(duration=1)