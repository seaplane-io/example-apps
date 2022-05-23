from flask import Flask, send_file
from flask_restful import reqparse, abort, Api, Resource
import os


app = Flask(__name__)
api = Api(app)

# all available status codes and corresponding images
STATUS_CODES = {
    "200" : "./seaplane_200.jpeg",
    "404" : "./seaplane_404.jpeg",
    "500" : "./seaplane_500.jpeg",
}

# check to make sure the requested status code is available. Otherwise return 404
def abort_if_status_doesnt_exist(status_code):
    if status_code not in STATUS_CODES:
        abort(404, message="Status code {} doesn't exist".format(status_code))

# return the requested status code
class ResponseCodes(Resource):
    def get(self, status_code):

        # check to make sure the status code exists
        abort_if_status_doesnt_exist(status_code)
        return send_file(STATUS_CODES[status_code], mimetype="image/png")


# API routing
api.add_resource(ResponseCodes, '/statuscode/<status_code>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=80)
