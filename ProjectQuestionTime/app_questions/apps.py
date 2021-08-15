from django.apps import AppConfig


class AppQuestionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_questions'
    
    def ready(self):
        import app_questions.signals
