import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s"
)

from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.responses import JSONResponse
app = FastAPI()

log = logging.getLogger(__name__)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"text": f"Hello {name}"}

# 设置简单密码
PASSWORD = "123456"

# 一个 POST 接口，接收消息
@app.post("/message")
async def receive_message(request: Request, x_password: str = Header(...)):
    # 验证密码
    if x_password != PASSWORD:
        raise HTTPException(status_code=401, detail="Unauthorized")

    # 获取请求 JSON
    data = await request.json()
    log.info("this is log %s", data)
    print("Received message:", data)  # 打印收到的消息

    # 返回简单 JSON
    return JSONResponse(content={"status": "ok", "received": data})