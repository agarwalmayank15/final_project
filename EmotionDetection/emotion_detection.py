import requests
import json

def emotion_detector(text_to_analyze):
    # Check if the input text is empty
    if not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(URL, json=input_json, headers=header)
    formatted_response = json.loads(response.text)

    # If the response is successful, extract emotions and find the dominant one
    if response.status_code == 200:
        emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion_predictions, key=emotion_predictions.get)
        result = {
            'anger': emotion_predictions.get('anger', 0),
            'disgust': emotion_predictions.get('disgust', 0),
            'fear': emotion_predictions.get('fear', 0),
            'joy': emotion_predictions.get('joy', 0),
            'sadness': emotion_predictions.get('sadness', 0),
            'dominant_emotion': dominant_emotion
        }
    # Handle cases where the API response is an error (e.g., status 400)
    elif response.status_code == 400:
        result = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    return result
