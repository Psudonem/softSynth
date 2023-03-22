# based on https://stackoverflow.com/a/33880295/20226323

import math
import pyaudio
PyAudio = pyaudio.PyAudio
BITRATE = 24000

FREQUENCY = 500     #Hz, waves per second, 261.63=C4-note.
LENGTH = 1     #seconds to play sound

BITRATE = max(BITRATE, FREQUENCY+100)


NUMBEROFFRAMES = int(BITRATE * LENGTH)
RESTFRAMES = NUMBEROFFRAMES % BITRATE
WAVEDATA = ''

def wave(t):
    f1 = 261.63
    #f2 = 329.63
    y = math.sin(t / ((BITRATE/f1) * (1/math.pi)))*127 + 128
    #y += math.sin(t / ((BITRATE/f2) * (1/math.pi)))*127 + 128
    
    return y
    
for x in range(NUMBEROFFRAMES):
    WAVEDATA = WAVEDATA+chr(int(wave(x)))
    #WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))    

while int(x)>1:
    x-=(x/10)
    #print(x)
    WAVEDATA = WAVEDATA+chr(int(x))


p = PyAudio()

stream = p.open(format = p.get_format_from_width(1), 
                channels = 1, 
                rate = BITRATE, 
                output = True)



stream.write(WAVEDATA)
stream.stop_stream()
stream.close()
p.terminate()





