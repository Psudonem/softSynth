import math
import pyaudio
import mido

class instrument:
      def __init__(self,func):
            self.WAVEDATA = ''
            self.function=func

class softSynth:
      def __init__(self):
            self.BITRATE = 24000
            self.instruments=[]

      
