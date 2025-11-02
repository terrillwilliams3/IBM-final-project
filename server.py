"""Flask web server for emotion detection.

This module provides two endpoints:
1. `/` - Renders the web application's home page.
2. `/emotionDetector` - Accepts text input and returns the analyzed emotions
   and their corresponding scores using the Emotion Detection API.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def sent_analyzer():
    """Analyze the sentiment or emotion of input text.

    Retrieves the text from the request query string, sends it to the
    `emotion_detector` function, and returns a formatted string containing
    emotion scores and the dominant emotion. If no valid text is provided,
    an error message is returned.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid input! Please try again."

    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    result = (
        f"For the given statement, the system response is: "
        f"anger: {anger_score}, disgust: {disgust_score}, "
        f"fear: {fear_score}, joy: {joy_score}, sadness: {sadness_score}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return result


@app.route("/")
def render_index_page():
    """Render the home page of the web application."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)