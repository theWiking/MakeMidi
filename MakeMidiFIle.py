import midiutil

#CONST

DRUM_CHANNEL=9


#CONST Drums
KICK=36
KICK_ACOUSTIC=35

SNARE=38
SNARE_RIM=40
SNARE_SIDE=37

TOM_VERY_LOW=41
TOM_LOW=43
TOM_MEDIUM=45
TOM_HIGH=48
TOM_VERY_HIGH=50

RIDE_MIDDLE=51
RIDE_EDGE=59
RIDE_BELL=53

HIHAT_CLOSE=42
HIHAT_HALF=0
HIHAT_OPEN=46
HIHAT_PEDAL=44

CRASH_MEDIUM=49
CRASH_HIGH=57

SPLASH=55

CHINA=52

COWBELL_HIGH=0
COWBELL_MEDIUM=0
COWBELL_LOW=0






MIDIFile=midiutil.MIDIFile(numTracks=1)
MIDIFile.addTempo(track=0,time=0,tempo=120)
#MIDIFile.addTrackName(track=1,trackName="Drums",time=0)
#MIDIFile.addTimeSignature(track=1)

MIDIFile.addNote(track=0,pitch=36,time=0,duration=1,volume=120,channel=DRUM_CHANNEL)
MIDIFile.addNote(track=0,pitch=38,time=0,duration=1,volume=120,channel=DRUM_CHANNEL)
MIDIFile.addNote(track=0,pitch=36,time=1,duration=2,volume=120,channel=DRUM_CHANNEL)
MIDIFile.addNote(track=0,pitch=36,time=3,duration=1,volume=120,channel=DRUM_CHANNEL)
MIDIFile.addProgramChange(tracknum=0,channel=DRUM_CHANNEL,program=0,time=0)
with open("test.mid",'wb') as output_file:
    MIDIFile.writeFile(output_file)