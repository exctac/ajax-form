# ajax-form


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