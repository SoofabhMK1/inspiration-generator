from typing import List, Optional

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

# 导入我们创建的所有模块
import crud
import models
import schemas
from database import SessionLocal, engine

# 这行代码会在应用启动时，根据我们的模型在数据库中创建所有表。
# 注意：在生产环境中，我们更倾向于完全使用Alembic来管理数据库，
# 但在开发阶段，这对于快速启动非常方便。
# models.Base.metadata.create_all(bind=engine) 
# 更好的实践是让Alembic全权负责，所以我们注释掉这一行。

app = FastAPI()

# --- 中间件 (CORS配置保持不变) ---
from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost:5173", # 前端开发服务器地址
    "http://localhost",      # Docker Nginx 容器地址
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 数据库会话依赖项 ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# --- API Endpoints ---

@app.get("/random-idea", response_model=schemas.Idea)
def read_random_idea(db: Session = Depends(get_db)):
    """
    API接口：获取一条随机的灵感。
    - response_model=schemas.Idea 告诉FastAPI，返回的数据将符合Idea schema的结构。
    - db: Session = Depends(get_db) 是FastAPI的依赖注入系统。
      它会在处理这个请求之前，先调用 get_db() 函数，获取一个数据库会话，
      然后把它作为 'db' 参数传递给我们的函数。请求结束后，get_db() 的 finally 块会确保会话被关闭。
    """
    random_idea = crud.get_random_idea(db)
    return random_idea

@app.get("/ideas", response_model=List[schemas.Idea])
def read_ideas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    API接口：获取所有灵感列表，支持分页。
    - response_model=List[schemas.Idea] 表示返回的数据是一个列表，列表中的每个元素都符合Idea schema。
    """
    ideas = crud.get_ideas(db, skip=skip, limit=limit)
    return ideas

@app.post("/ideas", response_model=schemas.Idea)
def create_new_idea(idea: schemas.IdeaCreate, db: Session = Depends(get_db)):
    """
    API接口：创建一条新的灵感。
    - idea: schemas.IdeaCreate 告诉FastAPI，请求体(request body)的数据必须符合IdeaCreate schema的结构。
      FastAPI会自动解析和验证传入的JSON数据。
    """
    return crud.create_idea(db=db, idea=idea)