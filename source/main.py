from roboflow import Roboflow
import supervision as sv
import cv2

#Carrega o modelo a ser usado
rf = Roboflow(api_key="OdzI2sc8lOkvP9TQxJLg")
project = rf.workspace().project("animals-detection-bsbbi")
model = project.version(3).model

#Faz a inferência na imagem passada
result = model.predict("./source/bear.jpg", confidence=40, overlap=30).json()

#Carrega o rótulo a ser colocado na imagem
labels = [item["class"] for item in result["predictions"]]

#Guarda as detecções da inferência
detections = sv.Detections.from_inference(result)

#Inicializa a caixa e o rótulo
label_annotator = sv.LabelAnnotator()
bounding_box_annotator = sv.BoxAnnotator()

#Define a imagem a ser mostrada
image = cv2.imread("./source/bear.jpg")

#Aplica a caixa e o rótulo na imagem
annotated_image = bounding_box_annotator.annotate(
    scene=image, detections=detections)
annotated_image = label_annotator.annotate(
    scene=annotated_image, detections=detections, labels=labels)

#Mostra a imagem
sv.plot_image(image=annotated_image, size=(16, 16))