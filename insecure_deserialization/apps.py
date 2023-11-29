from django.apps import AppConfig


class InsecureDeserializationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'insecure_deserialization'
