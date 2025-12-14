import os

class Config:
    """基础配置类"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True
    DATABASE_URI = 'sqlite:///dev.db'
    REDIS_URL = 'redis://localhost:6379/0'

class ProductionConfig(Config):
    """生产环境配置"""
    DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///prod.db'
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://localhost:6379/1'

class TestingConfig(Config):
    """测试环境配置"""
    TESTING = True
    DATABASE_URI = 'sqlite:///test.db'
    REDIS_URL = 'redis://localhost:6379/2'

# 配置字典
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

def get_config():
    """根据环境变量获取对应配置"""
    env = os.environ.get('FLASK_ENV') or os.environ.get('APP_ENV') or 'default'
    return config.get(env, config['default'])