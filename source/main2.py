from ultralytics import YOLO
import cv2

# Carregar o modelo YOLO
model = YOLO("yolov5su.pt")

# Caminho do vídeo de entrada
video_path = "videos/bear.mp4"

# Caminho do vídeo de saída
# Mude o nome do arquivo para o qual você quiser
output_path = "../VisaoComp-IA-2024/videos_output/bear_output.mp4"


# Inicializar o OpenCV para leitura do vídeo
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Erro ao abrir o vídeo.")
    exit()

# Configurar o VideoWriter para salvar o vídeo anotado
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Processar cada frame do vídeo
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Fim do vídeo.")
        break

    # Realizar a detecção no frame atual
    results = model(frame)
    
    # Adicionar as anotações no frame
    annotated_frame = results[0].plot()

    # Exibir o frame com detecções (opcional)
    cv2.imshow("Deteccoes", annotated_frame)

    # Escrever o frame anotado no arquivo de saída
    out.write(annotated_frame)

    # Pressione 'q' para interromper a execução
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
out.release()
cv2.destroyAllWindows()

print("Processamento concluído. Vídeo salvo em:", output_path)
