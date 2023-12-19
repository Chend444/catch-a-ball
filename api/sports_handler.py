from flask import jsonify

from models.user_registration import UserRegistration, db


def create_registration(data):
    email = data.get('email')
    city = data.get('city')

    # Check if this city for the email already exists
    existing_registration = UserRegistration.query.filter_by(email=email, city=city).first()

    if existing_registration:
        return 'This city has already been registered for this email.'

    new_reg = UserRegistration(**data)
    db.session.add(new_reg)
    db.session.commit()

    if new_reg:
        return 'Registration created successfully'
    return jsonify(new_reg)


def get_user_city_registration_by_email(email):
    # Query the database to find all user registrations by email
    registrations = UserRegistration.query.filter_by(email=email).all()

    if registrations:
        # Build a list to store all registration details
        response_data = []
        for registration in registrations:
            registration_data = {
                'id': registration.id,
                'email': registration.email,
                'city': registration.city,
                'registration_date': registration.registration_date.strftime("%Y-%m-%d %H:%M:%S")
                # Include other fields as needed
            }
            response_data.append(registration_data)

        return jsonify({'registrations': response_data})
    else:
        return jsonify({'message': 'User registrations not found for the given email'}), 404


def delete_registration_by_id(registration_id):
    registration = UserRegistration.query.get(registration_id)
    if registration:
        db.session.delete(registration)
        db.session.commit()
        return 'Registration deleted successfully'
    else:
        return 'Registration not found'
