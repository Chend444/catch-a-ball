from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserRegistration(db.Model):
    __tablename__ = 'user_registration'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    city = db.Column(db.String(100))
    registration_date = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (db.UniqueConstraint('email', 'city', name='_email_city_uc'),)

    def __repr__(self):
        return f'<UserRegistration {self.email} - {self.city}>'
