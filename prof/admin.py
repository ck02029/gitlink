from django.contrib import admin

from prof import models

admin.site.register(models.WorkExperience)
admin.site.register(models.Education)

class EndorsementInline(admin.TabularInline):
    model = models.Endorsement

class SkillAdmin(admin.ModelAdmin):
    inlines = [
        EndorsementInline,
    ]


admin.site.register(models.Skill, SkillAdmin)

admin.site.register(models.SocialProfile)
admin.site.register(models.ProfileView)
admin.site.register(models.JobVacancy)
admin.site.register(models.JobApplication)