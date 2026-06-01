# REST API Client using Python Requests Library

## Objective

Build a Python-based REST API Client that demonstrates:

- HTTP request handling (GET, POST, PUT, DELETE)
- Headers and JSON payload handling
- API key simulation
- HTTP response code handling
- Error handling
- Postman testing
- CLI-based interaction

---
## Project Structure

```text
rest-api-client/

├── core/
│   ├── config.py
│   └── exceptions.py
│
├── api/
|      ├──client.py
├── services/
|      ├──sevices.py
├── main.py
│
├── requirements.txt
├── README.md
├── .gitignore

```

---

## Technologies Used

- Python
- Requests Library
- JSONPlaceholder API
- Postman
- Git & GitHub
- Virtual Environment (venv)
---
## Virtual Environment Setup

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```
## API Used  


Base URL:

https://jsonplaceholder.typicode.com

Resource:

```text
/posts
```

---

## Features Implemented

### GET
- Fetch all posts
- Fetch post by ID

### POST
- Create new post

### PUT
- Update existing post

### DELETE
- Delete post

### Additional Features

- Custom headers
- API key simulation
- JSON request handling
- Status code handling
- Exception handling
- CLI menu system

---

## Status Codes Handled

| Code | Description |
|--------|-------------|
| 200 | Success |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Not Found |
| 500 | Server Error |

---

## Error Handling

Implemented handling for:

- Connection errors
- Timeout errors
- Invalid user input
- Unexpected responses

---

## Postman Testing

Tested API endpoints:

- GET
- POST
- PUT
- DELETE

Verified:

- Headers
- JSON request body
- Response codes
- Response output

## How to Run

Install dependencies:

```bash
pip install requests
```

Run project:

```bash
python main.py
```

---

## Key Learnings

- HTTP and HTTPS concepts
- Request-response architecture
- REST API communication
- CRUD operations
- Python requests library
- Headers and API authentication
- Exception handling
- Postman testing
- Modular project structure