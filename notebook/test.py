import os
import time
import pickle
import whisper
from pprint import pprint

import warnings
warnings.filterwarnings('ignore')

audio_path = '../data/audio/'
text_path = '../data/text/large'
audio_files = ['test.wav', 'APO9752808204.mp3', 'ktppgajunmopzorr9b83mzd5j24k.mp3']

model = whisper.load_model('large')

for i, audio_file in enumerate(audio_files):
    start = time.time()
    file_path = os.path.join(audio_path, audio_file)
    result = model.transcribe(file_path)
    
    with open(os.path.join(text_path, str(i) + '.pkl'), 'wb') as file: 
        pickle.dump(result, file) 
    
    print('{} took {} s'.format(audio_file, round(time.time() - start, 2)))
    
    
'''
tiny.en:
    test.wav took 1.70 s
    APO9752808204.mp3 took 75.31 s
    ktppgajunmopzorr9b83mzd5j24k.mp3 took 359.67 s
large:
    test.wav took 51.91 s
    APO9752808204.mp3 took 5799.65 s
    ktppgajunmopzorr9b83mzd5j24k.mp3 took 12976.4 s
'''