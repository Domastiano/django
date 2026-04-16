from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission  # dodaj Submission

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['content', 'course', 'grade']  # dodaj list_display

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'course']  # dodaj odpowiednie pola

admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)  # dodaj rejestrację
