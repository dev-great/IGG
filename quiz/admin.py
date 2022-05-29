from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.contrib.auth.models import Permission


class QuizTakerAdmin(admin. ModelAdmin):
    list_display = ("user", "quiz", "score", "completed", "date_completed")
    list_filter = ("user", "quiz", "score", "completed", "date_completed")
    search_fields = ("user", "quiz", "score", "completed", "date_completed")


admin.site.register(QuizTaker, QuizTakerAdmin)


class UsersAnswerAdmin(admin. ModelAdmin):
    list_display = ("quiz_taker", "question", "answer")
    list_filter = ("quiz_taker", "question", "answer")
    search_fields = ("quiz_taker", "question", "answer")


admin.site.register(UsersAnswer, UsersAnswerAdmin)


class QuizAdmin(admin. ModelAdmin):
    list_display = ("name", "slug", "roll_out", "timestamp")
    list_filter = ("name", "slug", "roll_out", "timestamp")
    search_fields = ("name", "slug", "roll_out", "timestamp")


admin.site.register(Quiz, QuizAdmin)


class AnswerAdmin(admin. ModelAdmin):
    list_display = ("question", "label", "is_correct")
    list_filter = ("question", "label", "is_correct")
    search_fields = ("question", "label", "is_correct")


admin.site.register(Answer, AnswerAdmin)


class QuestionAdmin(admin. ModelAdmin):
    list_display = ("quiz", "label", "order")
    list_filter = ("quiz", "label", "order")
    search_fields = ("quiz", "label", "order")


admin.site.register(Question, QuestionAdmin)
# Register your models here.
