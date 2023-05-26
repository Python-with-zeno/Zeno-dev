from deepface import DeepFace
import matplotlib.pyplot as plt
import pandas as pd
import cv2
import pathlib
import os

# FeepFace doc: https://pypi.org/project/deepface/
# tutor: https://www.youtube.com/watch?v=n84hBgtzvxo

img_folder = pathlib.Path(__file__).parent.absolute() / "img"
files = os.listdir(img_folder)

image_nr = 0

image_to_analyze = str(img_folder / files[image_nr])
print("Image to analyze: " + image_to_analyze)

backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface', 'mediapipe']


faces = DeepFace.extract_faces(img_path = image_to_analyze, target_size=(224, 224), detector_backend = backends[0])
print("Face: " + str(faces))

results = DeepFace.analyze(img_path = image_to_analyze)
print("Result: " + str(results))

image = cv2.imread(image_to_analyze)

font = cv2.FONT_HERSHEY_COMPLEX
font_scale = 0.7
font_size = 24 * font_scale
line_height = font_size * 1.25
color = (255, 0, 0) # Blue in BGR format
frame_width = 2

for f_index, face in enumerate(faces):
  print("face: " + str(face['facial_area']))
  x = face['facial_area']['x']
  y = face['facial_area']['y']
  w = face['facial_area']['w']
  h = face['facial_area']['h']
  x2 = x + w
  y2 = y + h
  cv2.rectangle(
    image,
    (x, y),
    (x2, y2),
    color,
    frame_width
  )

  for e_index, emotion in enumerate(results[f_index]["emotion"].keys()):
    value = results[f_index]["emotion"][emotion]
    position = (int(x + w + 10), y + int(e_index * line_height + 10))
    cv2.putText(
      image,
      emotion
      + ": "
      + f'{value:.2f}',
      position,
      font,
      font_scale,
      color
    )

cv2.imshow(files[image_nr], image)

# pd.DataFrame(result["emotion"], index=[0].T.plot(kind='bar'))

while True:
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
  if cv2.getWindowProperty(files[image_nr], cv2.WND_PROP_VISIBLE) < 1:
    break

cv2.destroyAllWindows()