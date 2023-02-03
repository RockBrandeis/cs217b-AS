from flask import Flask, jsonify, request

app = Flask(__name__)

# Note the methods argument, the default is a list with just GET, if you do not
# add POST then the resource will not accept POST requests.
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.get_json()
        # Using jsonify to create proper JSON, but you could just return the
        # dictionary object that you got from get_json(). The optional second
        # parameter will override the standard 200 response.
        return jsonify({'returning': user_input}), 418
    else:
        return jsonify('Howdy')

# Instead of @app.route you can use @app.get and @app.post

@app.get('/help')
def help():
    # Call this one with "curl http://127.0.0.1:5000/help"
    return "<p>Getting extremely minimal help</p>"

@app.post('/help')
def help_post():
    # Call this one with "curl --request POST http://127.0.0.1:5000/help"
    return "<p>Posting extremely minimal help</p>"

# This uses a typed subpath of multiply, in effect creating an unlimited amount
# of resources. Call this with "curl http://127.0.0.1:5000/multiply/5"
@app.route('/multiply/<int:num>')
def multiply(num):
    return jsonify({'result': num * 10})

# A variant of the above, where you only have one resource, but you hand it a
# query parameter. Call this with "curl http://127.0.0.1:5000/multiply2?num=5"
@app.route('/multiply2')
def multiply2(num=1):
    # The parameter has to be a default parameter, otherwise you get an error
    return jsonify({'result': num * 10})

# You can also hand in the number via the POST attachment.
# curl http://127.0.0.1:5000/multiply3 -H "Content-Type: application/json" -d '{"number": 5}'
@app.route('/multiply3', methods=['POST'])
def multiply3():
    some_json = request.get_json()
    return jsonify({'result': some_json['number'] * 10})

# The request object also gives access to the raw data of the POST request
@app.route('/bounce', methods=['POST'])
def bounce():
    answer = '\nContent-Type: %s\n\n' % request.headers['Content-Type']
    answer += str(request.data) + '\n\n'
    return answer


if __name__ == '__main__':
    app.run(debug=True)


'''

Two ways of sending the content of the POST request:

$ curl -H "Content-Type: application/json" -X POST -d '{"name": "sue"}'  http://127.0.0.1:5000/
$ curl -H "Content-Type: application/json" -X POST -d @input/message.json http://127.0.0.1:5000/

When you use -d the POST method is implied so you can shorten this a bit:

$ curl http://127.0.0.1:5000/ -H "Content-Type: application/json" -d '{"name": "sue"}'
$ curl http://127.0.0.1:5000/ -H "Content-Type: application/json" -d @input/message.json

We can send something that is not JSON:

$ curl http://127.0.0.1:5000/bounce -H "Content-Type: application/json" -d @input/message.json
$ curl http://127.0.0.1:5000/bounce -H "Content-Type: text/plain" -d @input/message.txt
$ curl http://127.0.0.1:5000/bounce -H "Content-Type: text/xml" -d @input/message.xml

'''
