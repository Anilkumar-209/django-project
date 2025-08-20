from django.apps import AppConfig  # import base app configuration class

class ParagraphsConfig(AppConfig):  # configuration for paragraphs app
    default_auto_field = 'django.db.models.BigAutoField'  # default primary key type
    name = 'paragraphs'  # app name
