define({ "api": [
  {
    "type": "post",
    "url": "/users",
    "title": "Predict positive rate",
    "version": "0.1.0",
    "name": "List",
    "group": "Predict",
    "description": "<p>Returns the predicted positive rate</p>",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"success\": true,\n    \"result\":{\n        \"email\": \"admin@example.com\",\n        \"groups\": [],\n        \"url\": \"http://localhost:8000/users/1/\",\n        \"username\": \"paul\"\n        },\n        {\n        \"email\": \"tom@example.com\",\n        \"groups\": [                ],\n        \"url\": \"http://127.0.0.1:8000/users/2/\",\n        \"username\": \"tom\"\n        }\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200\n{\n    \"success\": false,\n    \"errors\":{\n        \"global_error\":{\n            \"code\": 3066431594,\n            \"message\": \"Not found\"\n        }\n    }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "quickstart/views.py",
    "groupTitle": "Predict"
  }
] });
