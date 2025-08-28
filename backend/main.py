# 1. 导入我们需要的工具
import random
from typing import Optional
from fastapi import FastAPI
# 新增导入：从FastAPI的中间件中导入CORS中间件
from fastapi.middleware.cors import CORSMiddleware

# 2. 创建一个FastAPI应用实例
app = FastAPI()

# 3. 新增CORS配置
# -------------------------------------------------------------
# 定义一个我们允许访问的来源（前端地址）列表
# 在开发阶段，我们的Vue应用会运行在 http://localhost:5173
origins = [
    "http://localhost:5173",
]

# 将CORS中间件添加到应用中
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 允许访问的来源
    allow_credentials=True,  # 是否支持携带cookie
    allow_methods=["*"],  # 允许所有的请求方法（GET, POST等）
    allow_headers=["*"],  # 允许所有的请求头
)
# -------------------------------------------------------------


# 4. 创建一个“模拟数据库”
mock_database = {
    "fortune": [
        "今天会遇到一件意想不到的好事。",
        "你的创造力今天会达到顶峰，适合开始新项目。",
        "一个许久未见的朋友可能会联系你。",
        "财运不错，但要避免冲动消费。",
    ],
    "lunch": [
        "试试新开的那家越南河粉店。",
        "来一份健康的鸡胸肉沙拉，补充能量。",
        "豪华便当是对自己辛勤工作的最好奖励。",
        "简单的三明治和一杯咖啡，享受片刻宁静。",
    ],
    "movie": [
        "经典科幻片《银翼杀手》值得重温。",
        "轻松愉快的动画电影《疯狂动物城》。",
        "悬疑烧脑的《看不见的客人》。",
        "温情感人的《寻梦环游记》。",
    ]
}

# 5. 创建我们的API接口 (Endpoint)
@app.get("/api/random-idea")
async def get_random_idea(category: Optional[str] = None):
    if not category:
        category = random.choice(list(mock_database.keys()))

    if category in mock_database:
        idea = random.choice(mock_database[category])
        return {"category": category, "idea": idea}
    else:
        return {"error": f"Category '{category}' not found. Available categories are: {list(mock_database.keys())}"}