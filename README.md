# docker_openai_service_flask
Flask backend as a proxy for calling OpenAI API

# -- DEV Local--
$ docker compose -f docker-compose.dev.yml up --build

Running on http://localhost:40003/openai

# -- Build --
$ docker build -t flask_web_app .
# Run image
$ docker run --name flask_web_app -p 40003:40003 flask_web_app
