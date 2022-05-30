from django.contrib import admin
from .models import Attendance,StudentExtra,TeacherExtra,Notice,Country,City,State,Village

class StudentExtraAdmin(admin.ModelAdmin):
   list_display = ['id', 'user', 'profile_pic', 'roll', 'mobile', 'fee', 'email','gender','branch','cl','status','country','state','city','village']
admin.site.register(StudentExtra, StudentExtraAdmin)
class TeacherExtraAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'salary', 'joindate', 'mobile', 'status', 'branch1','teacher_profile']
admin.site.register(TeacherExtra, TeacherExtraAdmin)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['roll', 'date', 'cl', 'present_status']
    
admin.site.register(Attendance, AttendanceAdmin)
class NoticeAdmin(admin.ModelAdmin):
     list_display = ['date', 'by', 'message']
admin.site.register(Notice, NoticeAdmin)
class CountryAdmin(admin.ModelAdmin):
     list_display = ['name']
admin.site.register(Country,CountryAdmin)
class CityAdmin(admin.ModelAdmin):
    list_display = ['state', 'city_name']
admin.site.register(City, CityAdmin)
class StateAdmin(admin.ModelAdmin):
  list_display = ['country', 'state_name']
admin.site.register(State, StateAdmin)
class VillageAdmin(admin.ModelAdmin):
   list_display = ['city', 'village_name']
admin.site.register(Village, VillageAdmin)


