from fastapi.responses import JSONResponse
from fastapi import Request


def exception_handler(request: Request, exc: Exception) -> JSONResponse:
    return JSONResponse(
        {
            "status": "error",
            "info": str(exc)
        },
        status_code=500
    )
