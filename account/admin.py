from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.contrib.auth.models import Permission


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phonenumber", "fullname", "address", "profilepix")
    search_fields = ("user", "phonenumber", "fullname", "address")

    def profilepix(self, obj):
        return format_html('<img src="/media/{}" style="width:30%; margin-left: 20%;" />'.format(obj.profilepix))

    profilepix.short_description = 'profilepix'


admin.site.register(Profile, ProfileAdmin)


class GettutorAdmin(admin. ModelAdmin):
    list_display = ("fullname", "phonenumber", "email", "Start", "address",
                    "kidsnum", "modeoftutor", "subjects", "duration", "goalofchild")
    list_filter = ("kidsnum", "modeoftutor", "subjects",
                   "duration", "goalofchild")
    search_fields = ("fullname", "phonenumber", "email", "Start", "address",
                     "kidsnum", "modeoftutor", "subjects", "duration", "goalofchild")


admin.site.register(Gettutor, GettutorAdmin)


class ActivetutorAdmin(admin. ModelAdmin):
    list_display = ("turorialkey", "amount", "expires_in", "paid")
    list_filter = ("turorialkey", "amount", "expires_in", "paid")
    search_fields = ("turorialkey", "amount", "expires_in", "paid")


admin.site.register(Activetutor, ActivetutorAdmin)


class WorkhistoryAdmin(admin. ModelAdmin):
    list_display = ("tutor", "organization", "country", "role", "stillactive")
    list_filter = ("tutor", "organization", "country", "role", "stillactive")
    search_fields = ("tutor", "organization", "country", "role", "stillactive")


admin.site.register(Workhistory, WorkhistoryAdmin)


class EducationalhistoryAdmin(admin. ModelAdmin):
    list_display = ("tutor", "school", "country", "course", "degrees", "grade")
    list_filter = ("tutor", "school", "country", "course", "degrees", "grade")
    search_fields = ("tutor", "school", "country",
                     "course", "degrees", "grade")


admin.site.register(Educationalhistory, EducationalhistoryAdmin)


class BecometutorAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "email", "phonenumber",
                    "dob", "sex", "primarylanguage", "state", "city", "teachingmode")
    list_filter = ("sex", "primarylanguage", "state", "city", "teachingmode")
    search_fields = ("firstname", "lastname", "email", "phonenumber",
                     "dob", "sex", "primarylanguage", "state", "city", "teachingmode")


admin.site.register(Becometutor, BecometutorAdmin)


class KYCAdmin(admin. ModelAdmin):
    list_display = ("tutor", "passportphoto", "valiedid")

    def passportphoto(self, obj):
        return format_html('<img src="/media/{}" style="width:30%; margin-left: 20%;" />'.format(obj.passportphoto))

    passportphoto.short_description = 'passportphoto'

    def valiedid(self, obj):
        return format_html('<img src="/media/{}" style="width:30%; margin-left: 20%;" />'.format(obj.profilepix))

    valiedid.short_description = 'profilepix'

# Register your models here.


admin.site.register(KYC, KYCAdmin)
