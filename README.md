# ajax-form

1. Скопируйте папку приложения "app" в директорию вашего проекта.
2. Далее как обычно:

INSTALLED_APPS = (

    ...
    'app'
    ...
)

urlpatterns = [

    ...
    url(r'^app/', include('app.urls', app_name="app", namespace="app")),
    ...
]

./manage.py migrate app