## Buidling the app
```
docker build . -t docker-django-resampler
```
## Running the app
```
 docker run  -it -p 8000:8000 docker-django-resampler python manage.py runserver 0.0.0.0:8000
 ```