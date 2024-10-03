from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('app.config.Config')

# Initialize the database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import your models here
from app.user.model import User  # Adjust the import according to your project structure

if __name__ == '__main__':
    app.run(debug=True)