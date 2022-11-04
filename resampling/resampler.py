
from scipy.signal import resample
from scipy.io import wavfile
import librosa
import tempfile


def wave_down_sampling(content):
    data, sampling_rate = librosa.load(content, sr=None)
    number_of_samples = int((len(data) * 32000)/sampling_rate)
    new_data = resample(data, number_of_samples)
    return new_data


def mp3_down_sampling(file_uploaded):
    with tempfile.NamedTemporaryFile(mode='wb+') as tmp:
        for chunk in file_uploaded.chunks():
            tmp.write(chunk)
        data, sampling_rate = librosa.load(tmp.name, sr=None)
        number_of_samples = int((len(data) * 32000)/sampling_rate)
        new_data = resample(data, number_of_samples)
    return new_data    