import base64
import requests


# Your Clarifai API key
import os
api_key = os.getenv("CLARIFAI_API_KEY")

# Path to your local image
image_path = r"/Users/lipikaprasad/Downloads/Classroom.jpg"

# Read the image and encode it to base64
with open(image_path, "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

headers = {
    "Authorization": f"Key {api_key}",
    "Content-Type": "application/json"
}

data = {
    "inputs": [
        {
            "data": {
                "image": {
                    "base64": encoded_image
                }
            }
        }
    ]
}

response = requests.post(
    "https://api.clarifai.com/v2/models/general-image-recognition/outputs",
    headers=headers,
    json=data
)

# Parse and display the predictions
predictions = response.json()

# Show concepts with names and confidence values
for concept in predictions['outputs'][0]['data']['concepts']:
    print(f"{concept['name']}: {round(concept['value'] * 100, 2)}% confidence")
