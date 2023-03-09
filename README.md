# docker_openai_service_flask
Flask backend as a proxy for calling OpenAI API



# -- Build --
$ docker build -t flask_web_app .
# Run image
$ docker run --name flask_web_app -p 40002:40002 flask_web_app
