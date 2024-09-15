"""
Flask application for emotion detection.
"""
from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the index.html page.
    
    Returns:
        str: HTML content of the index page.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Handle emotion detection requests.
    
    Receives a JSON payload with 'statement', processes it, and returns the 
    emotion analysis result or an error message if the input is invalid.

    Returns:
        Response: JSON response with the result of the emotion analysis or an error message.
    """
    data = request.json
    statement = data.get('statement')
    
    if not statement or not statement.strip():
        return jsonify({"message": "Invalid text! Please try again!"}), 400
    
    emotion_result = emotion_detector(statement)
    
    if emotion_result['dominant_emotion'] is None:
        return jsonify({"message": "Invalid text! Please try again!"}), 400
    
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {emotion_result['anger']}, 'disgust': {emotion_result['disgust']}, "
        f"'fear': {emotion_result['fear']}, 'joy': {emotion_result['joy']} and "
        f"'sadness': {emotion_result['sadness']}. The dominant emotion is "
        f"{emotion_result['dominant_emotion']}."
    )
    
    return jsonify({
        "message": response_text,
        "emotion_details": emotion_result
    })

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
