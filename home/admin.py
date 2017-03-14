from django.contrib import admin
from .models import test, bootstrap_Carousel, owl_PhotoSlide, accordion1_content, accordion2_content, accordion3_content, accordion4_content

# Register your models here.
class HomeModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "timeStamp", "updated"]
    class Meta:
        model = test


class BootstrapCarouselModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "slider_title", "slider_fading_type", "timestamp"]
    class Meta:
        model = bootstrap_Carousel

class OwlCarouselModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "timestamp"]
    class Meta:
        model = owl_PhotoSlide

class Accordion1ModelAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    class Meta:
        model = accordion1_content

class Accordion2ModelAdmin (admin.ModelAdmin):
    list_display = ["__str__"]
    class Meta:
        model = accordion2_content

class Accordion3ModelAdmin (admin.ModelAdmin):
    list_display = ["__str__"]
    class Meta:
        model = accordion3_content

class Accordion4ModelAdmin (admin.ModelAdmin):
    list_display = ["__str__"]
    class Meta:
        model = accordion4_content


admin.site.register(test, HomeModelAdmin)
admin.site.register(bootstrap_Carousel, BootstrapCarouselModelAdmin)
admin.site.register(owl_PhotoSlide, OwlCarouselModelAdmin)
admin.site.register(accordion1_content, Accordion1ModelAdmin)
admin.site.register(accordion2_content, Accordion2ModelAdmin)
admin.site.register(accordion3_content, Accordion3ModelAdmin)
admin.site.register(accordion4_content, Accordion4ModelAdmin)