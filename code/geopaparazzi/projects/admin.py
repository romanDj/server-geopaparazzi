from django.contrib.gis import admin

# Register your models here.
from geopaparazzi.projects.models import Subdivision, Project

admin.site.register(Subdivision)
admin.site.register(Project)