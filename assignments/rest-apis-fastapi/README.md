# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Build a simple RESTful web service using the FastAPI framework in Python.

## 📝 Tasks

### 🛠️	Set up a FastAPI application

#### Description
Create a new Python project and install FastAPI and an ASGI server (such as Uvicorn). Write the code to start a FastAPI app that can be run locally.

#### Requirements
Completed application should:

- Include a working `main.py` (or similar) with a FastAPI instance
- Start a server with a default route (e.g., `/`) that returns a welcome message
- Be runnable with `uvicorn` or equivalent

### 🛠️	Implement REST endpoints

#### Description
Add several endpoints to your FastAPI application to handle CRUD operations for a simple resource.

#### Requirements
Completed application should:

- Define a Pydantic model for the resource (e.g., `Item` with `id`, `name`, `price`)
- Provide routes for `GET`, `POST`, `PUT`, and `DELETE` on `/items`
- Use an in-memory list or dictionary to store items during runtime
- Return appropriate status codes and JSON responses

### 🛠️	Document and test your API

#### Description
Take advantage of FastAPI's automatic documentation and verify your endpoints manually.

#### Requirements
Completed program should:

- Be accessible via the interactive docs at `/docs`
- Allow the user to test each endpoint from the browser or `curl`
- Include brief comments explaining key parts of the code
