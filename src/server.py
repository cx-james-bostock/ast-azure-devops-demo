from flask import Flask, request

app = Flask(__name__)

@app.route('/sleep', methods=['POST'])
def execute_user_code_unsafe():
    user_code = request.args.get('code')
    result = eval(user_code)
    return result['value']
