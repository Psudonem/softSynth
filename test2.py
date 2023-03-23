import mido
mid = mido.MidiFile('hydlide 3 - out of freedom arrange.mid')
track = mid.tracks[1]


def noteToFreq(note):
    a = 440 #frequency of A (common value is 440Hz)
    return (a / 32) * (2 ** ((note - 9) / 12))

midi_notes = list(range(128))
midi_freqs = [noteToFreq(note) for note in midi_notes]
print(midi_freqs)

##lookup={
##      50:146.83,
##      48:
##      }
##
##
##
for i in track:
      if(i.type=="note_on" or i.type=="note_off"):
            print(i)
            print(midi_freqs[i.note])
##
##
##
