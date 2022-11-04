
import librosa
from pydub import AudioSegment
from scipy.io import wavfile
import tempfile


def out_signal(sampled_data, target_sr):
    
    """ the sampled data needs to be converted first to wav signal and then being converted to mp3.
    in order to avoid writing into the disk and make the API faster we use SpooledTemporaryFile which
    makes a virtual file in memory"""
   
    with tempfile.SpooledTemporaryFile(mode="wb+") as out_wav:
        wavfile.write(out_wav, target_sr, sampled_data)
        with tempfile.SpooledTemporaryFile(mode="wb+") as out_mp3:
            AudioSegment.from_file(out_wav).export(out_mp3, format='mp3')
            return out_mp3.read()
                     


def down_sampling(uploaded_file, target_sr=32000):
    with tempfile.NamedTemporaryFile(mode='wb+') as tmp:
        for chunk in uploaded_file.chunks():
            tmp.write(chunk)
        data, sampling_rate = librosa.load(tmp.name, sr=None)
        if sampling_rate <= target_sr:
            return None
        else:    
            sampled_data = librosa.resample(data, orig_sr=sampling_rate, target_sr=target_sr)
            return out_signal(sampled_data, target_sr)
            