class Config:
    DEBUG = False
    TESTING = False
    OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
    PORT = 40003
    HOST = "0.0.0.0"
    CORS_ORIGINS = ["http://localhost", "http://0.0.0.0"]
    LIMITER = ["60 per hour"]

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    pass
