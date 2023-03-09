from flask import Flask, jsonify
# import openai

app = Flask(__name__)
# openai.api_key = "YOUR_API_KEY"

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/openai')
def openai_endpoint():
    prompt = "Hello, OpenAI!"
    # response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=10)
    # return jsonify(response.choices[0].text)

    return prompt

if __name__ == '__main__':
    # port = 5000
    # host='0.0.0.0'
    app.run(debug=True, host='0.0.0.0', port = 40003)
