# catch-a-ball

**RESTful API** providing user city registrations for sports event notifications.

## Overview

The **Catch-A-Ball** project allows users to register for sports event notifications in specific cities.

### External APIs Used

None

### Technologies Used

- **Flask**: Framework used to build the RESTful API.
- **SQLAlchemy**: ORM used for database interactions.

## Setup Instructions

To set up the project locally, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Chend444/catch-a-ball.git
    ```

2. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application**:

    ```bash
    python app.py
    ```

## API Endpoints

- `POST /sports/register`: Register a user for sports notifications in a city.
- `GET /sports/register/<email>`: Get user's city registrations by email.
- `DELETE /sports/register/<id>`: Delete a user's city registration by ID.

### Example for `POST /sports/register`

#### Request

```json
{
    "email": "example@gmail.com",
    "city": "london"
}

## Contributing

Contributions are welcome! Feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
