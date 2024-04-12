from flask_restful import Resource, Api, reqparse, marshal_with, fields
from .models import Playlists, db

api = Api(prefix='/api')
parser = reqparse.RequestParser()
parser.add_argument('playlist_name', type=str, help='Song name is required and should be a string', required=True)
parser.add_argument('playlist_description', type=str, help='Lyrics is required and should be a string', required=True)

playlists_fields = {
    'id': fields.Integer,
    'playlist_name': fields.String,
    'playlist_description': fields.String
}


class Play_lists(Resource):
    query = None

    @marshal_with(playlists_fields)
    def get(self):
        all_playlists = Playlists.query.all()
        if len(all_playlists) == 0:
            return {"message": "no playlists found"}, 404
        return all_playlists

    def post(self):
        args = parser.parse_args()
        playlists = Playlists(**args)
        db.session.add(playlists)
        db.session.commit()
        return {"message": "Playlists created"}


api.add_resource(Play_lists, '/play_lists')