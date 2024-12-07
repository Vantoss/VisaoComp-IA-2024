from roboflow import Roboflow
import supervision as sv
import cv2

#Carrega o modelo a ser usado
rf = Roboflow(api_key="OdzI2sc8lOkvP9TQxJLg")
project = rf.workspace().project("animals-detection-bsbbi")
model = project.version(3).model

#Define o vídeo a ser utilizado
VIDEO_PATH = "videos/urso.mp4"

#Guarda as informações do vídeo
video_info = sv.VideoInfo.from_video_path(video_path=VIDEO_PATH)

#Cria um gerador de frames do vídeo
frame_generator = sv.get_video_frames_generator(VIDEO_PATH)

#Guarda cada frame do gerador de frames
frame = next(iter(frame_generator))

#Faz uma iteração para cada frame do vídeo, mostrando a detecção no terminal
for frame in sv.get_video_frames_generator(source_path=VIDEO_PATH, stride=2):
    result = model.predict(image_path=frame).json()
    detections = sv.Detections.from_inference(result)
    print(detections)

