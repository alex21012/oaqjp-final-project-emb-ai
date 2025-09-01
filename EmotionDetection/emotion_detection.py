import requests
import json

def emotion_detector(text_to_analyze):
    # URL and headers for the API request
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    
    # JSON payload with the text to be analyzed
    json_payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Send the POST request
    response = requests.post(url, headers=headers, json=json_payload)

    # --- Error Handling Logic ---
    if response.status_code == 200:
        response_data = response.json()
        all_emotions = response_data['emotionPredictions'][0]['emotion']
        dominant_emotion = max(all_emotions, key=all_emotions.get)
        
        formatted_output = {
            'anger': all_emotions.get('anger'),
            'disgust': all_emotions.get('disgust'),
            'fear': all_emotions.get('fear'),
            'joy': all_emotions.get('joy'),
            'sadness': all_emotions.get('sadness'),
            'dominant_emotion': dominant_emotion
        }
        return formatted_output
    
    # New logic to handle blank input, which returns a 400 status code
    elif response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    else:
        # Handle other potential errors
        return {"error": f"Request failed with status code {response.status_code}"}