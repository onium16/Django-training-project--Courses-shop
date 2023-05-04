from django.contrib import admin
from .models import Course, Category


admin.site.site_header = "Courses Admin"
admin.site.site_title = "My Courses"
admin.site.index_title = "Welcome to the Courses admin panel"

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category')

class CoursesInline(admin.TabularInline):
    model = Course
    exclude = ['creat_at']
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'creat_at')
    fieldsets = [
        (None, {"fields": ['title']}),
        ('Dates', {
               'fields' : ['creat_at'],
               'classes': ['collapse']
            })
    ]
    inlines = [CoursesInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)