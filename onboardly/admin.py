from django.contrib import admin
from .models import Poll, Answer, Question, UserResponse


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "poll", "depends_on")
    list_filter = ("poll", "depends_on")
    search_fields = ("text",)
    inlines = [AnswerInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "depends_on":
            kwargs["label"] = "Идет после"
        if db_field.name == "poll":
            kwargs["label"] = "Относится к опросу"
        if db_field.name == "text":
            kwargs["label"] = "Текст вопроса"
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class UserResponseAdmin(admin.ModelAdmin):
    list_display = ("user", "poll", "question", "answer")
    list_filter = ("user", "poll", "question")
    search_fields = ("user__username", "poll__name", "question__text")


admin.site.register(Question, QuestionAdmin)
admin.site.register(Poll)
admin.site.register(Answer)
admin.site.register(UserResponse, UserResponseAdmin)
