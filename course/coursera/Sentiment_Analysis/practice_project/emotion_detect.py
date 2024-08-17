import requests
import json


def emotion_detector(text_to_analyse):
    # Define the URL for the sentiment analysis API
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    # Define headers for the request
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Define input JSON for the request
    input_json = {"raw_document": {"text": text_to_analyse}}

    # Make a POST request to the Emotion Detection service
    response = requests.post(url, headers=headers, json=input_json)

    # Parse the response from the API
    formatted_response = json.loads(response.text)
    
    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']

    return anger_score
