# Task Management Backend API

## Description
A simple Task Management REST API built using Python and FastAPI.  
It supports creating, viewing, updating, and deleting tasks.

## Python Version
Python 3.8 or higher

## How to Run

1. Install dependencies
   pip install fastapi uvicorn

2. Run the server
   uvicorn main:app --reload

3. Open browser
   http://127.0.0.1:8000/docs

## API Endpoints

### Root
GET /

### Create Task
POST /tasks
```json
{
  "title": "Learn FastAPI",
  "description": "Backend assignment"
}
