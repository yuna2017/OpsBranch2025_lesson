# Docker Compose 教学示例

## 文件说明
这个 `docker-compose-example.yml` 文件展示了 Docker Compose 的基本用法，包含了常见的服务配置。

## 主要特性

### 1. 多服务编排
- **web**: Nginx Web 服务器
- **db**: MySQL 数据库
- **redis**: Redis 缓存服务

### 2. 关键概念演示
- **服务依赖**: web 服务依赖于 db 服务
- **端口映射**: 将容器端口映射到主机端口
- **数据卷**: 持久化数据库数据
- **网络**: 服务间通信网络

## 使用命令

```bash
# 启动所有服务
docker-compose -f docker-compose-example.yml up -d

# 查看服务状态
docker-compose -f docker-compose-example.yml ps

# 停止服务
docker-compose -f docker-compose-example.yml down

# 查看日志
docker-compose -f docker-compose-example.yml logs [服务名]
```

## 教学要点

1. **YAML 语法**: 注意缩进和格式
2. **服务定义**: 每个服务都是一个独立的容器
3. **镜像使用**: 使用官方镜像快速部署
4. **环境变量**: 通过 environment 配置数据库
5. **网络隔离**: 服务在同一个网络中可以相互访问
6. **数据持久化**: 使用 volumes 保存重要数据

## 扩展练习
- 添加更多的服务（如 MongoDB、PostgreSQL）
- 修改端口映射避免冲突
- 添加健康检查配置
- 配置环境变量文件