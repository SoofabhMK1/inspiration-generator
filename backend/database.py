import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量 (主要用于本地开发)
load_dotenv()

# 从环境变量中读取数据库连接URL
# 我们在 docker-compose.yml 中定义了这个环境变量
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# 创建SQLAlchemy引擎。引擎是与数据库进行通信的核心接口。
# connect_args 是专门为SQLite准备的，对于PostgreSQL可以忽略，但保留也无妨。
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

# 创建一个数据库会话工厂(SessionLocal)。
# 每个SessionLocal实例都是一个数据库会话，你应该为每个请求创建一个独立的会话。
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建一个 DeclarativeMeta 基类。
# 我们之后创建的所有数据模型(ORM models)都将继承这个类。
Base = declarative_base()

# 创建一个依赖项函数，用于在API请求中获取数据库会话
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()