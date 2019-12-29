import subprocess
import numpy as np
import librosa.display
import os
import librosa
from pydub import AudioSegment
from pydub.utils import make_chunks
from sklearn.preprocessing import normalize


def mp3ToMatrix(song):

    try:
        subprocess.call(['ffmpeg', '-i', "input_mp3/"+song[:3]+"/"+song+".mp3",
                     "tempWav/"+song+"_stereo.wav"])
        sound_mono = AudioSegment.from_wav("tempWav/"+song+"_stereo.wav")
        sound_mono = sound_mono.set_channels(1)
        sound_mono.export("tempWav/"+song+"_mono.wav", format="wav")

        sound = AudioSegment.from_wav("tempWav/"+song+"_mono.wav")
        y, sr = librosa.load("tempWav/"+song+"_mono.wav")


        chroma = librosa.feature.chroma_stft(y=y,sr=sr)
        chroma = normalize(chroma, axis=0)
        chroma_fnl = chroma[:,chroma.shape[1]/2:chroma.shape[1]/2+500]

        mfcc = librosa.feature.mfcc(y=y, sr=sr, hop_length=512, n_mfcc=12)
        mfcc = normalize(mfcc, axis=0)
        mfcc_fnl = mfcc[:,mfcc.shape[1]/2:mfcc.shape[1]/2+500]
        # mfcc_fnl = mfcc[:, mfcc.shape[1] / 2:mfcc.shape[1] / 2 + 100]


        chunk_length = 1000/(mfcc.shape[1]/sound.duration_seconds)


        loudness = [chunk.dBFS for chunk in make_chunks(sound, chunk_length)]
        loudness = np.array(loudness)
        loudness_count = loudness.shape[0]
        loudness_fnl=np.ndarray((loudness_count,1),buffer=np.array(loudness))[loudness_count/2:loudness_count/2+500]

        final_data = np.concatenate((np.transpose(chroma_fnl),np.transpose(mfcc_fnl)),axis=1)
        final_data = np.concatenate((loudness_fnl,final_data),axis=1)
        # final_data_nw = np.reshape(final_data, (1, final_data.shape[0] * final_data.shape[1]))

        # print final_data_nw.shape
        os.remove("tempWav/"+song+"_mono.wav")
        os.remove("tempWav/"+song+"_stereo.wav")

        print final_data.shape

        return final_data,True

    except:
        return None, False

