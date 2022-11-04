A django rest API for downsampling wav/mp3 files to 32kHz. The APIs recieve an arbitary mp3/wav file then return a resampled file

## Buidling the docker
```command
docker build . -t docker-django-resampler
```

## Running the server
```command
 docker run  -it -p 8000:8000 docker-django-resampler python manage.py runserver 0.0.0.0:8000
```

## API example
```python
import requests
url = http://127.0.0.1:8000/api/home/
file = {'file_uploaded': open('your-file.wav','rb')}
r = requests.post(url, files=file)
with open("resampled-file.wav", "wb") as f:
    f.write(r.content)
```


## Script
A python script `client/script.py` run a batch job using ray library to call API in a multi processing way. There are two folders called src_files and dst_files as subfolders. The former includes the audio files which we want to resample them and the later will include the resampled version after running the script.

```command
python script.py
```

Note that you need to have the server running to make the script working. In addition you need to have ray installed in your local machine.

```command
pip install ray[default]
```

