import uvicorn
import fastapi

app =  fastapi.FastAPI()
total_requests = 0


@app.get("/health_check")
def health_check():
    return {"status":"ok"}

@app.get("/total_requests")
def request_counter():
    global total_requests

    total_requests+=1
    return {"total_reqeusts": total_requests}


if __name__ == "__main__":
    uvicorn.run(app=app, port=8000)
