import uvicorn
import os

SERVER_HOST = os.environ.get("SERVER_HOST", "127.0.0.1")
SERVER_PORT = int(os.environ.get("SERVER_PORT", 8000))

if __name__ == "__main__":
    uvicorn.run("app.main:app", host=SERVER_HOST, port=SERVER_PORT, reload=True)
