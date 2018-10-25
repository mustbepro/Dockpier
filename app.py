# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask_restful import Resource, Api, reqparse
import docker

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

class Index(Resource):
    def get(self):
        return "Index page"

class Info(Resource):
    def get(self):
        return client.info()

class Version(Resource):
    def get(self):
        return client.version()

## Image Section ##
class Images(Resource):
    def get(self):
        imagetable = []
        for image in client.images.list():
            imagetable.append(image.attrs)
        return imagetable

    def post(self):
        parser.add_argument('name', help='Package name')
        parser.add_argument('tag', help='Package Tag/Version')
        args = parser.parse_args()
        if args.tag == "":
            args.tag="latest"
        img = client.images.pull(args.name, args.tag)
        return img.attrs, 201

class Image(Resource):
    def get(self, image_id):
        return client.images.get(image_id).attrs

    def delete(self, image_id):
        return client.images.remove(image_id), 204

## Container Section ##
class Containers(Resource):
    def get(self):
        containertable = []
        for container in client.containers.list(all=True):
            containertable.append(container.attrs)
        return containertable



## Networks Section ##
class Networks(Resource):
    def get(self):
        networktable = []
        for network in client.networks.list():
            networktable.append(network.attrs)
        return networktable

class Network(Resource):
    def get(self, image_id):
        return client.networks.get(net_id)

    def delete(self, net_id):
        return client.networks.remove(net_id), 204



client = docker.from_env()
api.add_resource(Index, '/')
api.add_resource(Info, '/info')
api.add_resource(Version, '/version')

api.add_resource(Images, '/images')
api.add_resource(Image, '/images/<image_id>')

api.add_resource(Containers, '/containers')

api.add_resource(Networks, '/networks')
api.add_resource(Network, '/networks/<net_id>')

if __name__ == '__main__':
    print("############ Docker docking status ############")
    print(client.version())
    print("###############################################")
    app.run(debug=True, host='0.0.0.0')
