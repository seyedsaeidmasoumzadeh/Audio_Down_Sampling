import glob
import ntpath
import requests
import ray

API_URL = "http://127.0.0.1:8000/api/home/"


def chunk(slice, n):
    """
    This function chunks a list, numpy array or DataFrame to a given size
    """
    for i in range(0, len(slice), int(n)):
        yield slice[i : i + int(n)]

@ray.remote
def resample(file):
    file_uploaded = {'file_uploaded': open(file,'rb')}
    r = requests.post(API_URL, files=file_uploaded)
    if r.status_code == 200:
        file_name = ntpath.basename(file)
        with open("dst_files/{}".format(file_name), "wb") as f:
            f.write(r.content)
            print("{} sucessfully resampled".format(file_name))

def main():
    ray.init()

    files = glob.glob('src_files/*')
    chunks = chunk(files, 5)
    for ch in chunks:
        ray.get([resample.remote(file) for file in ch])


if __name__ == "__main__":
    main()        
