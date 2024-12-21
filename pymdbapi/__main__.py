from flask import Flask
from flask_cors import CORS
from pymdbapi.routes import routes

app = Flask(__name__)
CORS(app)

app.register_blueprint(routes)

def main():
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    main()
