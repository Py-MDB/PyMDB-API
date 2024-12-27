# PyMDB-API

PyMDB-API is a simple API built with Flask to manage all your CMDB related needs. It includes endpoints for hardware, users, facilities, operating systems, and application tokens.

Features:
- Quick development setup with Docker compose
- Secure access with user and application tokens
- Basic data validation with defined schemas
- Unit tests for maintaining code quality

## Prerequisites

- Docker
- Docker Compose

## Setup Development Environment

1. Clone the repository:

    ```sh
    git clone https://github.com/Py-MDB/PyMDB-API
    cd PyMDB-API
    ```

2. Create the following environment variables in your build environment:

    ```sh
    export MONGO_INITDB_ROOT_USERNAME=PyMDB
    export MONGO_INITDB_ROOT_PASSWORD=112233445566
    export MONGO_HOST=172.20.0.2
    export MONGO_PORT=27017
    ```

3. Navigate to the `PyMDB-API` directory and start the services using Docker Compose:

    ```sh
    cd PyMDB-API
    docker-compose up --build -d
    ```

4. The API is secured by `User-Token` and `App-Token`s by default.  The intial build of the API will automatically generate a default admin user and app token.  You will need to either manually look for these values in the db or they should be printed to the docker compose logs `docker-compose logs pymdbapi-db`

5. The API should now be accessible at `http://localhost:5000`.

## Running Tests

To run the unit tests, use the following command:

```sh
python -m unittest discover -s tests
```

## Project Layout

### Directories

- `PyMDB-API/pymdbapi`: Contains the API code.
- `PyMDB-API/tests`: Contains unit tests

### Files

- `PyMDB-API/Dockerfile`: Dockerfile for building the API container.
- `PyMDB-API/docker-compose.yml`: Docker Compose file for running the API and MongoDB containers.
- `PyMDB-API/pymdbapi/__main__.py`: Entry point for the Flask application.
- `PyMDB-API/pymdbapi/routes.py`: Contains the API routes.
- `PyMDB-API/pymdbapi/route-helper.py`: Contains helper functions that connect the routes to the database. 
- `PyMDB-API/pymdbapi/mongodb.py`: Contains functions related to interacting with mongodb.
- `PyMDB-API/pymdbapi/schema.py`: Contains the schema definitions for data validation.
- `PyMDB-API/pymdbapi/init_db.py`: Contains the db init functions that will create initial access tokens.
- `PyMDB-API/pymdbapi/auth.py`: Contains the authentication function.
- `PyMDB-API/test.py`: Script for testing the API endpoints.

## API Endpoints

### Available endpoints:

- `/hardware`
- `/hardware/<id>`
- `/users`
- `/users/<id>`
- `/users/<id>/generate-token`
- `/facilities`
- `/facilities/<id>`
- `/operating_systems`
- `/operating_systems/<id>`
- `/app_tokens`
- `/app_tokens/<id>`
- `/app_tokens/<id>/generate_token`

### `GET /<endpoint>`

Returns a list of the endpoint data from the MongoDB collection.

### `POST /<endpoint>`

Adds a new entry to the MongoDB collection. The request body should be in JSON format and follow the schema defined in `pymdbapi/schema.py`.

### `PUT /<endpoint>`

Update an existing record.  Updates must still follow the schema defined in `pymdbapi/schema.py`.

### `DELETE /<endpoint>`

Delete an existing record.

## Example Request

### `POST /hardware`

```json
{
    "name": "MyComputer",
    "type": "Laptop",
    "specs": {
        "cpu": "Intel i7",
        "ram": "16GB",
        "storage": "512GB SSD"
    }
}
```

## Contributing

We welcome contributions to the project. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them with a clear message.
4. Push your changes to your fork.
5. Create a pull request to the main repository.

## License

This project is licensed under the Mozilla Public License, version 2.0 (MPL-2.0). For full terms and conditions, refer to the license linked above.
