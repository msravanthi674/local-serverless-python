from fastapi import FastAPI, Request
from dispatcher import dispatch_event
import uvicorn

app = FastAPI()

@app.post("/invoke/{function_name}")
async def invoke_function(function_name: str, request: Request):
    data = await request.json()
    result = dispatch_event(function_name, data)
    return result

def start_http_server():
    print("[HTTP] Starting HTTP trigger server on port 8000...")
    uvicorn.run(app, host="0.0.0.0", port=8000)

