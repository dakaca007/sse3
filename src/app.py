from flask import Flask, jsonify, request
import openai
from config import DevelopmentConfig as app_config

app = Flask(__name__)
# app.config.from_object(DevelopmentConfig)
app.config.from_object(app_config)
openai.api_key = app.config['OPENAI_API_KEY']

def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

    Animal: Cat
    Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
    Animal: Dog
    Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
    Animal: {}
    Names:""".format(animal.capitalize())

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/openai', methods=['POST'])
def openai_endpoint():
    # prompt = "Hello, OpenAI!"
    # return prompt

    prompt_params = request.json

    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = prompt_params.get('prompt','Hello world!'),
        temperature = prompt_params.get('temperature',0.7),
        max_tokens = prompt_params.get('max_tokens',2000),
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0
    )

    # print(response)
    return jsonify(response.choices)

if __name__ == '__main__':
    app.run(debug=True, host=app.config['HOST'], port = app.config['PORT'])
