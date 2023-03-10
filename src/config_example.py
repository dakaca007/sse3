class Config:
    DEBUG = False
    TESTING = False
    OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
    PORT = 40003
    HOST = "0.0.0.0"

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    pass
