from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Настройки CORS (если API будут вызывать из браузера)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешаем запросы от любого домена
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/company/{inn}")
async def get_company_data(inn: str):
    try:
        # Импортируем вашу основную функцию
        from main_script import main

        # Вызываем ваш существующий код
        result = main(inn)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
async def root():
    return {
        "message": "Добро пожаловать в API!",
        "available_endpoint": "/company/{inn}",
        "example": "http://103.88.242.226:8000/company/1234567890"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)