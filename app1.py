from flask import Flask, request, jsonify
from flask_cors import CORS
from run_code_in_docker import run_code

app = Flask(__name__)
CORS(app)

@app.route('/run', methods=['POST'])
def run():
    data = request.get_json()
    code = data.get('code')
    language = data.get('language')

    if not code or not language:
        return jsonify({'output': '', 'error': 'Missing code or language'}), 400

    try:
        output, error = run_code(code, language)
        return jsonify({'output': output, 'error': error})
    except Exception as e:
        return jsonify({'output': '', 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
