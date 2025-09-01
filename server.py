"""
This module contains a Flask web application that serves an emotion detection tool.
"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Analyzes text provided in a query parameter and returns the emotion analysis.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    # --- New Error Handling Logic ---
    # Check if the dominant_emotion is None, which indicates an error
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # If no error, format the successful response string
    dominant_emotion = response.pop('dominant_emotion')
    formatted_response = ", ".join([f"'{k}': {v}" for k, v in response.items()])

    return (f"For the given statement, the system response is {formatted_response}. "
            f"The dominant emotion is <strong>{dominant_emotion}</strong>.")

@app.route("/")
def render_index_page():
    """
    Renders the main HTML page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
