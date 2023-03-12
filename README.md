# docker_openai_service_flask
Flask backend as a proxy for calling OpenAI API

# -- DEV Local--
$ docker compose -f docker-compose.dev.yml up --build

Running on http://localhost:40003/openai

# -- Build --
$ docker build -t flask_web_app .
# Run image
$ docker run --name flask_web_app -p 40003:40003 flask_web_app

# -- Post to Prompt --
curl -X POST http://localhost:40003/prompt \
-H "Content-Type: application/json" \
-d '{"prompt": "Say hello in Japanese", "max_tokens": 100}' \
-v


{"origins": app.config['CORS_ORIGINS']}}

# -- Call custom module --
1. Clone repository to 'custom_module' folder: eg /custom_module/repo/mymodule.py
2. In app.py call: from custom_module.repo import mymodule
3. Call function: mymodule.greeting("Name")
