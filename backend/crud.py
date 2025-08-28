from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func

import models
import schemas

# --- Read Operations ---

def get_random_idea(db: Session):
    """
    从数据库中随机获取一条Idea记录。
    """
    return db.query(models.Idea).order_by(func.random()).first()

def get_ideas(db: Session, skip: int = 0, limit: int = 100):
    """
    获取一个Idea记录的列表，支持分页。
    """
    return db.query(models.Idea).offset(skip).limit(limit).all()

# --- Create Operations ---

def create_idea(db: Session, idea: schemas.IdeaCreate):
    """
    在数据库中创建一条新的Idea记录。
    """
    # 将Pydantic模型转换为字典，然后用它来创建SQLAlchemy模型实例
    db_idea = models.Idea(**idea.dict())
    # 将实例添加到数据库会话中
    db.add(db_idea)
    # 提交事务，将更改写入数据库
    db.commit()
    # 刷新实例，以获取数据库自动生成的id和created_at等新数据
    db.refresh(db_idea)
    return db_idea