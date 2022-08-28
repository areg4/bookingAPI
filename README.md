# BOOKING API

BOOKINGAPI for technical Interview


## Summary

API REST to book a space for an event.


## Features 
- There are N rooms with M capacity.
- There are two types of events: public and private.
- If the event is public, any customer can book a space.
- If the event is private, no one else can book a space in the room.
- A customer can book a space for an event, if the event is public and there is still space available.
- A customer can cancel its booking and their space should be available again.
- A customer cannot book a space twice for the same event.
- The business can create a room with M capacity
- The business can create events for every room.
- The business can delete a room if said room does not have any events.
- A customer can book a place for an event.
- A customer can cancel its booking for an event.
- A customer can see all the available public events.
- For now, there is only one event per day.
- Each room has a different capacity.


## Pre-requirements

Download or clone this repo and put the [.env](https://drive.google.com/file/d/1iRnz4tE4o15lCmWAKp0jXuIgAn3Wjzhv/view?usp=sharing) at the root of the project.

Is needed to get Make, Docker and Docker-Compose installed at local to run the project.

- Docker 
- Docker Compose
- Make


## Tech Stack

- Python
- Django
- Django Rest Framework
- PostgreSQL
- Docker
- Docker-compose


## Run with make

- Build
    ```sh
        $ make local-build
    ```
- Run
    ```sh
        $ make local-up
    ```

- Rebuild
    ```sh
        $ make local-rebuild
    ```

- Stop
    ```sh
        $ make local-stop
    ```

- Logs
    ```sh
        $ make local-backend-logs
    ```

- Run tests
    ```sh
        $ make local-test
    ```

## Run with Docker-Compose

- Build
    ```sh
        $ docker-compose -f docker-compose.yml build
    ```
- Run
    ```sh
        $ docker-compose -f docker-compose.yml up -d
    ```

- Rebuild
    ```sh
        $ docker-compose -f docker-compose.yml up -d --build
    ```

- Stop
    ```sh
        $ docker-compose -f docker-compose.yml stop
    ```

- Logs
    ```sh
        $ docker-compose -f docker-compose.yml logs -f backend
    ```


## Documentation

To see full project documentation Run the project and goto [API Swagger Docs](http://127.0.0.1:8080/api/v1/docs/)
