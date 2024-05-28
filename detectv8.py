import cv2
from ultralytics import YOLO


def onButtonPressv8(frame):
    """Performs object detection, extracts unique labels, and writes them to a text file."""
    cap = cv2.VideoCapture(0)  # Assuming webcam stream at index 0
    model = YOLO("D:/ENGG/SEM 8/B.TECH PROJECT/yolov5v8streamlit/bestv8.pt")
    unique_classes_v8 = set()  # Create a set to store unique classes
    last_label = None  # Variable to keep track of the last label encountered

    with open("unique_labels_v8_1.txt", "w") as labels_file:  # Open file with write mode
        while True:
            ret, image = cap.read()
            if not ret:
                break

            # Perform object detection
            results = model.predict(source=image, show=False)


            # Extract and store unique labels
            for result in results:
                for box in result.boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 1)
                    label = result.names[int(box.cls)]
                    confidence = box.conf[0]
                    cv2.putText(image, f"{label}: {confidence:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                    # Check if the current label is different from the last one
                    if label != last_label:
                        unique_classes_v8.add(label)
                        labels_file.write(f"{label}\n")  # Write each label to the file
                        last_label = label  # Update last_label

            # Update frame in Streamlit (optional, comment out if not needed)
            frame.image(image, channels="BGR")

    cap.release()


