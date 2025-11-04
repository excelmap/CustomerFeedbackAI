from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to CustomerFeedbackAI!"

@app.route('/feedback', methods=['POST'])
def feedback():
    data = request.json
    feedback_text = data.get('feedback', '')
    # Placeholder for future AI sentiment analysis logic
    return jsonify({"message": "Feedback received!", "feedback": feedback_text})

if __name__ == '__main__':
    app.run(debug=True)
