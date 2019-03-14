from flask_restplus import Api
from .users import api as users_api
from .email_list import api as email_list_api
from .auth import api as auth_api
from .role import api as role_api

api = Api(
    title='Otter Pond Web API',
    version='0.0.1',
    description='Web API for the Otter Pond',
)

api.add_namespace(users_api, path="/users")
api.add_namespace(email_list_api, path="/email_lists")
api.add_namespace(auth_api, path="/auth")
api.add_namespace(role_api, path="/roles")
