from django.apps import AppConfig


class EclinicPlatformConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'eclinic_platform'

    def ready(self):
        import eclinic_platform.signals.main_signal