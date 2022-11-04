## Buidling the app
```
docker build . -t docker-django-resampler
```

## Running the app
```
 docker run  -it -p 8000:8000 docker-django-resampler python manage.py runserver 0.0.0.0:8000
```

## API example
```python
 file = {'file_uploaded': open('your-file.wav','rb')}
 r = requests.post(url, files=file)
 with open("resampled-file.wav", "wb") as f:
     f.write(r.content)
```