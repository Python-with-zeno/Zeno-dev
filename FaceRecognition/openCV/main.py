import cv2
import pathlib

# tutor: https://www.youtube.com/watch?v=5cg_yggtkso

print("Face detection with OpenCV")
cascade_path = pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"
print("Classifier file path: " + str(cascade_path))

clf = cv2.CascadeClassifier(str(cascade_path))

camera = cv2.VideoCapture(0)
# camera = cv2.VideoCapture('video.mp4')

while True:
  _, frame = camera.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  faces = clf.detectMultiScale(
    gray,
    scaleFactor = 1.1,
    minNeighbors = 5,
    minSize = (100, 100),
    flags = cv2.CASCADE_SCALE_IMAGE
  )

  for (x, y, w, h) in faces:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

  cv2.imshow('frame', frame)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

camera.release()
cv2.destroyAllWindows()