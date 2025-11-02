from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function
    response = emotion_detector(text_to_analyze)
    # Extract the dominate emotion and emotion scores
    emotions = formatted_response["emotionPredictions"][0]["emotion"]
    anger_score = emotions["anger"]
    disgust_score = emotions["disgust"]
    fear_score = emotions["fear"]
    joy_score = emotions["joy"]
    sadness_score = emotions["sadness"]

    # Find dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Extract the dominate emotion and score from the response
    result = (
        "For the given statement, the system response is" 
        f"'anger': {anger_score}, 'disgust': {disgust_score}," 
        f"'fear': {fear_score}, 'joy': {joy_score} and" 
        f"'sadness': {sadness_score}. The dominant emotion is "
        f"{dominant_emotion}."
    )
    # Return a formatted string with the desired output
    return result

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)