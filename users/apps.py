from django.apps import AppConfig # import base app configuration class


class UsersConfig(AppConfig): # configuration for users app
    default_auto_field = 'django.db.models.BigAutoField' # default primary key type
    name = 'users' # app name
