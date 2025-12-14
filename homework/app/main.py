import sys
import os

# 尝试从包中导入，如果失败则从当前目录导入
try:
    from app.config import get_config
except ImportError:
    # 添加当前目录到Python路径
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from config import get_config

from flask import Flask, jsonify

def create_app():
    """创建Flask应用实例"""
    # 获取配置
    config_class = get_config()
    
    # 创建应用实例
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # 注册路由
    @app.route('/')
    def index():
        env = os.environ.get('FLASK_ENV') or os.environ.get('APP_ENV') or 'default'
        return jsonify({
            'message': f'Hello from {env} environment!',
            'environment': env,
            'debug': app.config['DEBUG'],
            'database_uri': app.config['DATABASE_URI']
        })
    
    @app.route('/health')
    def health():
        return jsonify({'status': 'healthy'})
    
    @app.route('/config')
    def config_info():
        env = os.environ.get('FLASK_ENV') or os.environ.get('APP_ENV') or 'default'
        return jsonify({
            'environment': env,
            'database_uri': app.config['DATABASE_URI'],
            'redis_url': app.config['REDIS_URL'],
            'debug': app.config['DEBUG']
        })
    
    return app

if __name__ == '__main__':
    # 确保能够正确导入配置
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if current_dir not in sys.path:
        sys.path.insert(0, current_dir)
    
    app = create_app()
    env = os.environ.get('FLASK_ENV') or os.environ.get('APP_ENV') or 'default'
    print(f"Starting application in {env} mode")
    
    if env == 'production':
        # 生产环境使用0.0.0.0和更安全的设置
        app.run(host='0.0.0.0', port=5000, debug=False)
    else:
        # 开发/测试环境使用调试模式
        app.run(host='127.0.0.1', port=5000, debug=app.config['DEBUG'])