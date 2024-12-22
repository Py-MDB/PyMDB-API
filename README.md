# PyMDB-API

API Piece for PyMDB

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

3. Navigate to the `PyMDB-DB` directory and start the services using Docker Compose:

    ```sh
    cd PyMDB-DB
    docker-compose up --build
    ```

4. The API should now be accessible at `http://localhost:5000`.

## Project Layout

### Directories

- `PyMDB-API/`: Contains the API code.
- `PyMDB-DB/`: Contains the Docker Compose configuration for MongoDB and the API.

### Files

- `PyMDB-API/Dockerfile`: Dockerfile for building the API container.
- `PyMDB-API/docker-compose.yml`: Docker Compose file for running the API and MongoDB containers.
- `PyMDB-API/pymdbapi/__main__.py`: Entry point for the Flask application.
- `PyMDB-API/pymdbapi/routes.py`: Contains the API routes and MongoDB connection logic.
- `PyMDB-API/pymdbapi/schema.py`: Contains the schema definitions for data validation.
- `PyMDB-API/test.py`: Script for testing the API endpoints.

## API Endpoints

### `GET /`

Returns a welcome message.

### `GET /hardware`

Returns a list of hardware data from the MongoDB collection.

### `POST /hardware`

Adds a new hardware entry to the MongoDB collection. The request body should be in JSON format and follow the schema defined in `pymdbapi/schema.py`.

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
