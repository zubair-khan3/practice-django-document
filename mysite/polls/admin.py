from django.contrib import admin
from polls.models import Question, Choice


# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')

    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
