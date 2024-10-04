from app import create_app
from flask_cors import CORS

app = create_app()
CORS(app)


if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"An error occurred: {e}")
