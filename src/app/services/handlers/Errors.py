from flask import Response
from werkzeug.exceptions import HTTPException

def handle_exception(e):
    """Return JSON response instead of HTML for HTTP errors.

    Args:
        e (HTTPException): exception
    """
    if isinstance(e, HTTPException):
        response = e.get_response()
        response.content = {
            "success": False,
            "status": e.code,
            "name": e.name,
            "description": e.description
        }
        print(e.description)
    else:
        print(e)
        response = Response()
        response.status_code = 500
        response.content = {
            "status": 500,
            "success": False,
            "message": "An unexpected non http error has occurred",
        }
        response.content_type = "application/json"
        return response.content