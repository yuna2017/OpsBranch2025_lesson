# 教学辅助系统后端服务

这是一个简单的Python后端服务，支持多种环境配置（开发、生产）。

## 目录结构

```
├── app/
│   ├── main.py          # 主应用文件
│   └── config.py        # 配置文件
├── requirements.txt     # Python依赖配置文件
└── README.md           # 说明文档
```

## 环境配置

系统支持两种环境：
- 开发环境 (development)
- 生产环境 (production)

通过设置环境变量 `FLASK_ENV` 或 `APP_ENV` 来切换环境：
```bash
# 设置开发环境
export FLASK_ENV=development

# 设置生产环境
export APP_ENV=production
```

## 依赖管理

使用pip和requirements.txt管理Python依赖：
```bash
# 安装依赖
pip install -r requirements.txt
```

## 运行服务

```bash
# 激活环境后运行
python app/main.py
```

## API接口

- `GET /` - 返回欢迎信息和当前环境
- `GET /health` - 健康检查接口
- `GET /config` - 返回当前配置信息

## 配置说明

不同环境有不同的配置：
- 数据库URI不同
- Redis连接地址不同
- 调试模式开关不同