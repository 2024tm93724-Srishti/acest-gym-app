from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to ACEest Fitness & Gym!"

@app.route('/members')
def members():
    return jsonify(["John", "Alice", "Bob"])

@app.route('/plans')
def plans():
    return jsonify(["Basic", "Premium", "Pro"])

if __name__ == '__main__':
    app.run(debug=True)