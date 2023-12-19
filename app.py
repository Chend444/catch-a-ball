from redis_config import redis  # Import the 'redis' object
from flask import Flask
from models.user_registration import db as models_db  # Import db from models
from api.sports_handler import db as handlers_db  # Import db from handlers
from routes.sports.sports_routes import sports_bp  # Import your sports_bp Blueprint


app = Flask(__name__)
app.config['REDIS'] = redis
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:a123456@localhost:5432/catch_a_ball'


models_db.init_app(app)  # Initialize db instance in models
handlers_db = models_db   # Use the same db instance in handlers

app.register_blueprint(sports_bp, url_prefix='/sports')  # Register the sports_bp Blueprint

if __name__ == '__main__':
    app.run(debug=True)
