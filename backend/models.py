from sqlalchemy import Column, Integer, String, DateTime, func
from database import Base

# 定义一个名为 Idea 的数据模型类，它继承自我们创建的 Base
# SQLAlchemy 会将这个类映射到数据库中一张名为 'ideas' 的表
class Idea(Base):
    __tablename__ = "ideas"

    # 定义表的字段 (列)
    # id: 主键，自增整数
    id = Column(Integer, primary_key=True, index=True)

    # category: 类别，字符串类型，不能为空，建立索引以加快查询速度
    category = Column(String, nullable=False, index=True)

    # content: 灵感内容，字符串类型，不能为空
    content = Column(String, nullable=False)

    # created_at: 创建时间，日期时间类型，默认值为当前数据库服务器时间
    created_at = Column(DateTime(timezone=True), server_default=func.now())