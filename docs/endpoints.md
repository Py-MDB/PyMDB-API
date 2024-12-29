# API Endpoints Documentation

## Table of Contents

- [User Routes](#user-routes)
- [App Token Routes](#app-token-routes)
- [Software Routes](#software-routes)
- [Network Routes](#network-routes)
- [Manufacturer Routes](#manufacturer-routes)
- [Location Routes](#location-routes)
- [Hardware Routes](#hardware-routes)

## User Routes

- `GET /users`
  - Description: Retrieve all users.
  - Required Privilege: 4

- `GET /users/<id>`
  - Description: Retrieve a user by ID.
  - Required Privilege: 4

- `POST /users`
  - Description: Create a new user.
  - Required Privilege: 5
  - Input Data: Must adhere to the user schema definition.

- `DELETE /users/<id>`
  - Description: Delete a user by ID.
  - Required Privilege: 5

- `POST /users/<id>/generate-token`
  - Description: Generate a token for a user by ID.
  - Required Privilege: 5

- `PUT /users/<id>`
  - Description: Update a user by ID.
  - Required Privilege: 5
  - Input Data: Must adhere to the user schema definition.

## App Token Routes

- `GET /app-tokens`
  - Description: Retrieve all app tokens.
  - Required Privilege: 3

- `GET /app-tokens/<id>`
  - Description: Retrieve an app token by ID.
  - Required Privilege: 3

- `POST /app-tokens`
  - Description: Create a new app token.
  - Required Privilege: 5
  - Input Data: Must adhere to the app token schema definition.

- `DELETE /app-tokens/<id>`
  - Description: Delete an app token by ID.
  - Required Privilege: 5

- `POST /app-tokens/<id>/generate-token`
  - Description: Generate a token for an app token by ID.
  - Required Privilege: 5

- `PUT /app-tokens/<id>`
  - Description: Update an app token by ID.
  - Required Privilege: 5
  - Input Data: Must adhere to the app token schema definition.

## Software Routes

- `GET /operating-systems`
  - Description: Retrieve all operating systems.
  - Required Privilege: 1

- `GET /operating-systems/<id>`
  - Description: Retrieve an operating system by ID.
  - Required Privilege: 1

- `POST /operating-systems`
  - Description: Create a new operating system.
  - Required Privilege: 3
  - Input Data: Must adhere to the operating system schema definition.

- `DELETE /operating-systems/<id>`
  - Description: Delete an operating system by ID.
  - Required Privilege: 4

- `PUT /operating-systems/<id>`
  - Description: Update an operating system by ID.
  - Required Privilege: 3
  - Input Data: Must adhere to the operating system schema definition.

- `GET /licenses`
  - Description: Retrieve all licenses.
  - Required Privilege: 1

- `GET /licenses/<id>`
  - Description: Retrieve a license by ID.
  - Required Privilege: 1

- `POST /licenses`
  - Description: Create a new license.
  - Required Privilege: 3
  - Input Data: Must adhere to the license schema definition.

- `DELETE /licenses/<id>`
  - Description: Delete a license by ID.
  - Required Privilege: 4

- `PUT /licenses/<id>`
  - Description: Update a license by ID.
  - Required Privilege: 3
  - Input Data: Must adhere to the license schema definition.

- `GET /software`
  - Description: Retrieve all software.
  - Required Privilege: 1

- `GET /software/<id>`
  - Description: Retrieve software by ID.
  - Required Privilege: 1

- `POST /software`
  - Description: Create new software.
  - Required Privilege: 3
  - Input Data: Must adhere to the software schema definition.

- `DELETE /software/<id>`
  - Description: Delete software by ID.
  - Required Privilege: 4

- `PUT /software/<id>`
  - Description: Update software by ID.
  - Required Privilege: 3
  - Input Data: Must adhere to the software schema definition.

## Network Routes

- `GET /interfaces`
  - Description: Retrieve all interfaces.
  - Required Privilege: 1

- `GET /interfaces/<id>`
  - Description: Retrieve an interface by ID.
  - Required Privilege: 1

- `POST /interfaces`
  - Description: Create a new interface.
  - Required Privilege: 3
  - Input Data: Must adhere to the interface schema definition.

- `DELETE /interfaces/<id>`
  - Description: Delete an interface by ID.
  - Required Privilege: 4

- `PUT /interfaces/<id>`
  - Description: Update an interface by ID.
  - Required Privilege: 3
  - Input Data: Must adhere to the interface schema definition.

## Manufacturer Routes

- `GET /manufacturers`
  - Description: Retrieve all manufacturers.
  - Required Privilege: 1

- `GET /manufacturers/<id>`
  - Description: Retrieve a manufacturer by ID.
  - Required Privilege: 1

- `POST /manufacturers`
  - Description: Create a new manufacturer.
  - Required Privilege: 3
  - Input Data: Must adhere to the manufacturer schema definition.

- `DELETE /manufacturers/<id>`
  - Description: Delete a manufacturer by ID.
  - Required Privilege: 4

- `PUT /manufacturers/<id>`
  - Description: Update a manufacturer by ID.
  - Required Privilege: 3
  - Input Data: Must adhere to the manufacturer schema definition.

## Location Routes

- `GET /facilities`
  - Description: Retrieve all facilities.
  - Required Privilege: 1

- `GET /facilities/<id>`
  - Description: Retrieve a facility by ID.
  - Required Privilege: 1

- `POST /facilities`
  - Description: Create a new facility.
  - Required Privilege: 3
  - Input Data: Must adhere to the facility schema definition.

- `DELETE /facilities/<id>`
  - Description: Delete a facility by ID.
  - Required Privilege: 4

- `PUT /facilities/<id>`
  - Description: Update a facility by ID.
  - Required Privilege: 3
  - Input Data: Must adhere to the facility schema definition.

- `GET /racks`
  - Description: Retrieve all racks.
  - Required Privilege: 1

- `GET /racks/<id>`
  - Description: Retrieve a rack by ID.
  - Required Privilege: 1

- `POST /racks`
  - Description: Create a new rack.
  - Required Privilege: 3
  - Input Data: Must adhere to the rack schema definition.

- `DELETE /racks/<id>`
  - Description: Delete a rack by ID.
  - Required Privilege: 4

- `PUT /racks/<id>`
  - Description: Update a rack by ID.
  - Required Privilege: 3
  - Input Data: Must adhere to the rack schema definition.

## Hardware Routes

- `GET /hardware`
  - Description: Retrieve all hardware.
  - Required Privilege: 1

- `GET /hardware/<id>`
  - Description: Retrieve hardware by ID.
  - Required Privilege: 1

- `POST /hardware`
  - Description: Create new hardware.
  - Required Privilege: 3
  - Input Data: Must adhere to the hardware schema definition.

- `DELETE /hardware/<id>`
  - Description: Delete hardware by ID.
  - Required Privilege: 4

- `PUT /hardware/<id>`
  - Description: Update hardware by ID.
  - Required Privilege: 3
  - Input Data: Must adhere to the hardware schema definition.

- `POST /hardware/<id>/link-interfaces`
  - Description: Link interfaces to hardware by ID.
  - Required Privilege: 3

- `POST /hardware/<id>/unlink-interfaces`
  - Description: Unlink interfaces from hardware by ID.
  - Required Privilege: 3
