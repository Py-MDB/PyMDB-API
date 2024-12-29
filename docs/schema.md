# PyMDB API Schemas

This document provides information about the schemas used in the PyMDB API, including examples of creating and updating objects adhering to these schemas.


## Table of Contents
- [Software Schema](#software-schema)
  - [Schema Definition](#schema-definition)
  - [Example - Creating a Software Object](#example---creating-a-software-object)
  - [Example - Updating a Software Object](#example---updating-a-software-object)
- [Racks Schema](#racks-schema)
  - [Schema Definition](#schema-definition-1)
  - [Example - Creating a Rack Object](#example---creating-a-rack-object)
  - [Example - Updating a Rack Object](#example---updating-a-rack-object)
- [Operating Systems Schema](#operating-systems-schema)
  - [Schema Definition](#schema-definition-2)
  - [Example - Creating an Operating System Object](#example---creating-an-operating-system-object)
  - [Example - Updating an Operating System Object](#example---updating-an-operating-system-object)
- [Manufacturers Schema](#manufacturers-schema)
  - [Schema Definition](#schema-definition-3)
  - [Example - Creating a Manufacturer Object](#example---creating-a-manufacturer-object)
  - [Example - Updating a Manufacturer Object](#example---updating-a-manufacturer-object)
- [Licenses Schema](#licenses-schema)
  - [Schema Definition](#schema-definition-4)
  - [Example - Creating a License Object](#example---creating-a-license-object)
  - [Example - Updating a License Object](#example---updating-a-license-object)
- [Interfaces Schema](#interfaces-schema)
  - [Schema Definition](#schema-definition-5)
  - [Example - Creating an Interface Object](#example---creating-an-interface-object)
  - [Example - Updating an Interface Object](#example---updating-an-interface-object)
- [Hardware Schema](#hardware-schema)
  - [Schema Definition](#schema-definition-6)
  - [Example - Creating a Hardware Object](#example---creating-a-hardware-object)
  - [Example - Updating a Hardware Object](#example---updating-a-hardware-object)
- [Facilities Schema](#facilities-schema)
  - [Schema Definition](#schema-definition-7)
  - [Example - Creating a Facility Object](#example---creating-a-facility-object)
  - [Example - Updating a Facility Object](#example---updating-a-facility-object)
- [App Tokens Schema](#app-tokens-schema)
  - [Schema Definition](#schema-definition-8)
  - [Example - Creating an App Token Object](#example---creating-an-app-token-object)
  - [Example - Updating an App Token Object](#example---updating-an-app-token-object)


## Software Schema

### Schema Definition
```python
software_schema = {
    // ...existing code...
}
```

### Example - Creating a Software Object
```json
{
    "name": "Example Software",
    "slug": "example-software",
    "state": "active",
    "version": "1.0.0",
    "type": "application",
    "license": {
        "href": "http://example.com/license",
        "id": "license-id"
    }
}
```

### Example - Updating a Software Object
```json
{
    "id": "software-id",
    "name": "Updated Software",
    "version": "1.1.0"
}
```

## Racks Schema

### Schema Definition
```python
racks_schema = {
    // ...existing code...
}
```

### Example - Creating a Rack Object
```json
{
    "name": "Rack 1",
    "slug": "rack-1",
    "u_space": 42,
    "facility": {
        "href": "http://example.com/facility",
        "id": "facility-id"
    }
}
```

### Example - Updating a Rack Object
```json
{
    "id": "rack-id",
    "name": "Updated Rack"
}
```

## Operating Systems Schema

### Schema Definition
```python
operating_systems_schema = {
    // ...existing code...
}
```

### Example - Creating an Operating System Object
```json
{
    "name": "Example OS",
    "slug": "example-os",
    "version": "1.0.0"
}
```

### Example - Updating an Operating System Object
```json
{
    "id": "os-id",
    "name": "Updated OS"
}
```

## Manufacturers Schema

### Schema Definition
```python
manufacturers_schema = {
    // ...existing code...
}
```

### Example - Creating a Manufacturer Object
```json
{
    "name": "Example Manufacturer",
    "slug": "example-manufacturer"
}
```

### Example - Updating a Manufacturer Object
```json
{
    "id": "manufacturer-id",
    "name": "Updated Manufacturer"
}
```

## Licenses Schema

### Schema Definition
```python
licenses_schema = {
    // ...existing code...
}
```

### Example - Creating a License Object
```json
{
    "name": "Example License",
    "slug": "example-license",
    "product_key": "XXXX-XXXX-XXXX-XXXX",
    "state": "active",
    "software": {
        "href": "http://example.com/software",
        "id": "software-id"
    }
}
```

### Example - Updating a License Object
```json
{
    "id": "license-id",
    "name": "Updated License"
}
```

## Interfaces Schema

### Schema Definition
```python
interfaces_schema = {
    // ...existing code...
}
```

### Example - Creating an Interface Object
```json
{
    "name": "eth0",
    "slug": "eth0",
    "state": "up",
    "type": "ethernet",
    "mac_address": "00:1A:2B:3C:4D:5E",
    "enabled": true,
    "management": true,
    "connected": true
}
```

### Example - Updating an Interface Object
```json
{
    "id": "interface-id",
    "name": "eth1"
}
```

## Hardware Schema

### Schema Definition
```python
hardware_schema = {
    // ...existing code...
}
```

### Example - Creating a Hardware Object
```json
{
    "name": "Example Hardware",
    "type": "server",
    "state": "active",
    "specs": {
        "cpu": "Intel Xeon",
        "ram": "32GB",
        "storage": [
            {
                "drive_type": "SSD",
                "capacity": "1TB",
                "interface": "SATA"
            }
        ]
    }
}
```

### Example - Updating a Hardware Object
```json
{
    "id": "hardware-id",
    "name": "Updated Hardware"
}
```

## Facilities Schema

### Schema Definition
```python
facilities_schema = {
    // ...existing code...
}
```

### Example - Creating a Facility Object
```json
{
    "name": "Example Facility",
    "slug": "example-facility",
    "location": "New York",
    "rack_capacity": 100,
    "state": "active"
}
```

### Example - Updating a Facility Object
```json
{
    "id": "facility-id",
    "name": "Updated Facility"
}
```

## App Tokens Schema

### Schema Definition
```python
app_tokens_schema = {
    // ...existing code...
}
```

### Example - Creating an App Token Object
```json
{
    "name": "Example Token",
    "privilege_level": 1
}
```

### Example - Updating an App Token Object
```json
{
    "id": "token-id",
    "name": "Updated Token"
}
