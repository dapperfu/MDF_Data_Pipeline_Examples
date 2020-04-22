# import the Flask class from the flask module
from flask import Flask, request

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/', defaults={'u_path': ''}, methods = ["GET", 'POST'])
@app.route('/<path:u_path>', methods = ['POST', "GET"])
def catch_all(u_path):
    print(repr(u_path))
    print(request.get_json())
    return "[This Space Intentionally Left Blank]"  # return a string

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

