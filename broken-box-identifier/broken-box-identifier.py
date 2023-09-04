from PIL import Image
from landingai.predict import Predictor

# Enter your API Key
endpoint_id = ""
api_key = ""

# Load your image
image = Image.open("boxes/box-13.jpeg")
# Run inference
predictor = Predictor(endpoint_id, api_key=api_key)
predictions = predictor.predict(image)
print(predictions)