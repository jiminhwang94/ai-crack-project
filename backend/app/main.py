from fastapi import FastAPI
from app.database import Base, engine
from app.routers import canal, crack, analyze, user, log, upload

app = FastAPI()

# 테이블 자동 생성
@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

# 라우터 등록 - Azure Database
app.include_router(canal.router)
app.include_router(crack.router)
app.include_router(analyze.router)
app.include_router(user.router)
app.include_router(log.router)

# 라우터 등록 - Azure Blob Storage
app.include_router(upload.router)