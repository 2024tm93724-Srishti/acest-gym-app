from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return "Gym Management System Running"

    @app.route('/members')
    def members():
        return jsonify({"members": ["Aman", "Riya", "John"]})

    @app.route('/plans')
    def plans():
        return jsonify({"plans": ["Basic", "Premium", "Pro"]})

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)