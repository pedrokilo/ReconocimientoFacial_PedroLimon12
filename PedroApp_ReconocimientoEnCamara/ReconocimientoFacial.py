import cv2
class Camara:
    def __init__(self):
        self.cascade_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        self.video_capture = cv2.VideoCapture(0)
    def run(self):
        while True:
            ret, frame = self.video_capture.read()
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.cascade_classifier.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=3,
                                                             minSize=(30, 30))
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.imshow("Deteccion de Rostros", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.video_capture.release()
        cv2.destroyAllWindows()
if __name__ == "__main__":
    camara = Camara()
    camara.run()