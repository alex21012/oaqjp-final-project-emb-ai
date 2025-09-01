import requests
import json

def emotion_detector(text_to_analyze):
    # URL for the emotion prediction API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers required for the API request
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    
    # The JSON payload containing the text to be analyzed
    json_payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Send the POST request to the API
    response = requests.post(url, headers=headers, json=json_payload)
    
    # Parse the JSON response into a Python dictionary
    response_data = json.loads(response.text)

    # Extract the emotion predictions from the response
    # The API returns a dictionary, and we need to navigate it to get the emotion scores.
    emotions = response_data['emotionPredictions'][0]['emotion']
    
    # Find the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    emotions['dominant_emotion'] = dominant_emotion

    return emotions