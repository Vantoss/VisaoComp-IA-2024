from roboflow import Roboflow
import supervision as sv
import cv2

rf = Roboflow(api_key="OdzI2sc8lOkvP9TQxJLg")
project = rf.workspace().project("animals-detection-bsbbi")
model = project.version(3).model

result = model.predict("./source/bear.jpg", confidence=40, overlap=30).json()

labels = [item["class"] for item in result["predictions"]]

detections = sv.Detections.from_inference(result)

label_annotator = sv.LabelAnnotator()
bounding_box_annotator = sv.BoxAnnotator()

image = cv2.imread("./source/bear.jpg")

annotated_image = bounding_box_annotator.annotate(
    scene=image, detections=detections)
annotated_image = label_annotator.annotate(
    scene=annotated_image, detections=detections, labels=labels)

sv.plot_image(image=annotated_image, size=(16, 16))