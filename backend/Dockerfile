# --- 阶段 1: 使用官方Python镜像作为基础 ---
# 我们选择一个特定版本的Python镜像，以确保环境一致性
FROM python:3.11-slim

# --- 阶段 2: 设置工作环境 ---
# 在容器内创建一个叫 /app 的文件夹，并把它设置为我们的工作目录
WORKDIR /app

# --- 阶段 3: 安装依赖 ---
# 先把记录依赖的 requirements.txt 文件复制进去
# 这样做可以利用Docker的缓存机制，如果这个文件没变，就不用重新安装依赖，加快构建速度
COPY requirements.txt .

# 运行pip命令，在容器内安装所有我们需要的库
RUN pip install --no-cache-dir -r requirements.txt

# --- 阶段 4: 复制项目代码 ---
# 把当前目录（backend文件夹）下的所有文件都复制到容器的 /app 目录里
COPY . .

# --- 阶段 5: 设置启动命令 ---
# 当容器启动时，默认执行这个命令来运行我们的应用
# "0.0.0.0" 表示监听所有网络接口，这样Docker外部才能访问到它
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]