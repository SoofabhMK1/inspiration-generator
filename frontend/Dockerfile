# --- 构建阶段 (Build Stage) ---
# 使用一个包含完整Node.js环境的镜像，我们叫它 "builder"
FROM node:18-alpine AS builder

# 设置工作目录
WORKDIR /app

# 复制 package.json 和 package-lock.json 文件
# 同样是为了利用缓存
COPY package*.json ./

# 安装所有开发依赖
RUN npm install

# 复制所有前端源代码
COPY . .

# 运行构建命令，这会把我们的Vue应用编译成纯静态的HTML/CSS/JS文件
# 编译后的文件会放在 /app/dist 目录里
RUN npm run build

# --- 运行阶段 (Production Stage) ---
# 现在，我们换一个非常轻量级的Nginx服务器镜像
FROM nginx:1.25-alpine

# 将我们刚刚在 "builder" 阶段编译好的静态文件，
# 从 /app/dist 目录复制到Nginx的默认网站根目录 /usr/share/nginx/html
COPY --from=builder /app/dist /usr/share/nginx/html

# Nginx镜像会自动启动服务，所以我们不需要CMD命令
# 但是，我们需要一份自定义的Nginx配置文件，下一步创建