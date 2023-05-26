from deepface import DeepFace
import pathlib

# FeepFace doc: https://pypi.org/project/deepface/
# tutor: https://www.youtube.com/watch?v=n84hBgtzvxo

img_folder = pathlib.Path(__file__).parent.absolute() / "database"

DeepFace.stream(db_path=str(img_folder), source=0)