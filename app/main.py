from flask import Flask
from flask_restplus import Resource, Api
import socket, os
import json



app = Flask(__name__)
api = Api(app)

@api.route('/ping')
class PingWorld(Resource):
    def get(self):
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)

        outPut={
            'release': 'r1',
            'hostname': host_name,
            'host_ip': host_ip
        }
        # return json.dumps(outPut)
        return outPut


if __name__ == '__main__':
    app.run(host="0.0.0.0",port="8080",debug=True)
