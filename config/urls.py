from django.contrib import admin
from django.urls import path
from app.views import near_hundred, string_splosion, cat_dog, lone_sum

urlpatterns = [
    path('Warmup-1/near-hundred/<int:n>', near_hundred),
    path('Warmup-2/string-splosion/<str>', string_splosion),
    path('String-2/cat-dog/<str>', cat_dog),
    path('Logic-2/lone-sum/<int:a>/<int:b>/<int:c>', lone_sum),
    path('admin/', admin.site.urls),

]
