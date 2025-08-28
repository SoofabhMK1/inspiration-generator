from pydantic import BaseModel
from datetime import datetime

# --- Idea Schemas ---

# 用于创建新Idea的基础模型 (从API接收数据时使用)
# 它不包含id和created_at，因为这些是由数据库自动生成的
class IdeaBase(BaseModel):
    category: str
    content: str

# 用于API创建Idea时使用的模型
class IdeaCreate(IdeaBase):
    pass

# 用于从API读取Idea时返回数据的模型 (发送数据给前端时使用)
# 它包含了所有数据库字段
class Idea(IdeaBase):
    id: int
    created_at: datetime

    # from_attributes = True 告诉Pydantic模型要从ORM模型(SQLAlchemy模型)中读取数据
    class Config:
        from_attributes = True