from django.contrib import admin
from django.urls import path
from app.views import near_hundred, string_splosion, cat_dog, lone_sum

urlpatterns = [
    path('near-hundred/<int:n>', near_hundred),
    path('string_splosion/<str>', string_splosion),
    path('cat_dog/<str>', cat_dog),
    path('lone_sum/<int:a>/<int:b>/<int:c>', lone_sum),
    path('admin/', admin.site.urls),

]
