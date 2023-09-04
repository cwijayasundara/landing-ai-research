from PIL import Image
from landingai.predict import Predictor

# Enter your API Key
endpoint_id = ""
api_key = ""

# Load your image
image = Image.open("beach-images/surfers_20230901-214027__14.png")
# Run inference
predictor = Predictor(endpoint_id, api_key=api_key)
predictions = predictor.predict(image)
# Print the predictions
print(predictions)