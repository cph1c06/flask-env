from flask import Flask
from flask_restful import Resource, Api
import os

app = Flask(__name__)
api = Api(app)
user=os.environ['USER']

class HelloWorld(Resource):
    def get(self):
        return {'hello': user}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
