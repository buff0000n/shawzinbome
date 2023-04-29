from abc import ABC, abstractmethod
from io import TextIOBase

# Okay, so I originally wrote this in Java of all things
# That's why it looks weird and has almost no documentation

Bb1 = "Bb1"
Db2 = "Db2"
Eb2 = "Eb2"

Gb2 = "Gb2"
Ab2 = "Ab2"
Bb2 = "Bb2"

B2  = "B2"
C3  = "C3"
Cs3 = "Cs3"
Db3 = "Db3"
D3  = "D3"
Ds3 = "Ds3"
Eb3 = "Eb3"
E3  = "E3"
F3  = "F3"
Fs3 = "Fs3"
Gb3 = "Gb3"
G3  = "G3"
Gs3 = "Gs3"
Ab3 = "Ab3"
A3  = "A3"
As3 = "As3"
Bb3 = "Bb3"
B3  = "B3"
C4  = "C4"
Cs4 = "Cs4"
Db4 = "Db4"
D4  = "D4"
Ds4 = "Ds4"
Eb4 = "Eb4"
E4  = "E4"
F4  = "F4"
Fs4 = "Fs4"
Gb4 = "Gb4"
G4  = "G4"
Gs4 = "Gs4"
Ab4 = "Ab4"
A4  = "A4"
As4 = "As4"
Bb4 = "Bb4"
B4  = "B4"
C5  = "C5"
Cs5 = "Cs5"
Db5 = "Db5"
D5  = "D5"
Ds5 = "Ds5"
Eb5 = "Eb5"
E5  = "E5"
F5  = "F5"
Fs5 = "Fs5"
Gb5 = "Gb5"
G5  = "G5"
Gs5 = "Gs5"
Ab5 = "Ab5"
A5  = "A5"
As5 = "As5"
Bb5 = "Bb5"
B5  = "B5"
C6  = "C6"
Cs6 = "Cs6"
Db6 = "Db6"
D6  = "D6"
Ds6 = "Ds6"
Eb6 = "Eb6"
E6  = "E6"
F6  = "F6"
Fs6 = "Fs6"
Gb6 = "Gb6"
G6  = "G6"
Gs6 = "Gs6"
Ab6 = "Ab6"
A6  = "A6"
As6 = "As6"
Bb6 = "Bb6"
B6  = "B6"
C7  = "C7"
Cs7 = "Cs7"
Db7 = "Db7"
D7  = "D7"
Ds7 = "Ds7"
Eb7 = "Eb7"
E7  = "E7"
F7  = "F7"
Fs7 = "Fs7"
Gb7 = "Gb7"
G7  = "G7"
Gs7 = "Gs7"
Ab7 = "Ab7"
A7  = "A7"
As7 = "As7"
Bb7 = "Bb7"
B7  = "B7"

keyToNote = dict()

keyToNote[B2]  = 47
keyToNote[C3]  = 48
keyToNote[Cs3] = 49
keyToNote[Db3] = 49
keyToNote[D3]  = 50
keyToNote[Ds3] = 51
keyToNote[Eb3] = 51
keyToNote[E3]  = 52
keyToNote[F3]  = 53
keyToNote[Fs3] = 54
keyToNote[Gb3] = 54
keyToNote[G3]  = 55
keyToNote[Gs3] = 56
keyToNote[Ab3] = 56
keyToNote[A3]  = 57
keyToNote[As3] = 58
keyToNote[Bb3] = 58
keyToNote[B3]  = 59
keyToNote[C4]  = keyToNote[C3]  + 12
keyToNote[Cs4] = keyToNote[Cs3] + 12
keyToNote[Db4] = keyToNote[Db3] + 12
keyToNote[D4]  = keyToNote[D3]  + 12
keyToNote[Ds4] = keyToNote[Ds3] + 12
keyToNote[Eb4] = keyToNote[Eb3] + 12
keyToNote[E4]  = keyToNote[E3]  + 12
keyToNote[F4]  = keyToNote[F3]  + 12
keyToNote[Fs4] = keyToNote[Fs3] + 12
keyToNote[Gb4] = keyToNote[Gb3] + 12
keyToNote[G4]  = keyToNote[G3]  + 12
keyToNote[Gs4] = keyToNote[Gs3] + 12
keyToNote[Ab4] = keyToNote[Ab3] + 12
keyToNote[A4]  = keyToNote[A3]  + 12
keyToNote[As4] = keyToNote[As3] + 12
keyToNote[Bb4] = keyToNote[Bb3] + 12
keyToNote[B4]  = keyToNote[B3]  + 12
keyToNote[C5]  = keyToNote[C4]  + 12
keyToNote[Cs5] = keyToNote[Cs4] + 12
keyToNote[Db5] = keyToNote[Db4] + 12
keyToNote[D5]  = keyToNote[D4]  + 12
keyToNote[Ds5] = keyToNote[Ds4] + 12
keyToNote[Eb5] = keyToNote[Eb4] + 12
keyToNote[E5]  = keyToNote[E4]  + 12
keyToNote[F5]  = keyToNote[F4]  + 12
keyToNote[Fs5] = keyToNote[Fs4] + 12
keyToNote[Gb5] = keyToNote[Gb4] + 12
keyToNote[G5]  = keyToNote[G4]  + 12
keyToNote[Gs5] = keyToNote[Gs4] + 12
keyToNote[Ab5] = keyToNote[Ab4] + 12
keyToNote[A5]  = keyToNote[A4]  + 12
keyToNote[As5] = keyToNote[As4] + 12
keyToNote[Bb5] = keyToNote[Bb4] + 12
keyToNote[B5]  = keyToNote[B4]  + 12
keyToNote[C6]  = keyToNote[C5]  + 12
keyToNote[Cs6] = keyToNote[Cs5] + 12
keyToNote[Db6] = keyToNote[Db5] + 12
keyToNote[D6]  = keyToNote[D5]  + 12
keyToNote[Ds6] = keyToNote[Ds5] + 12
keyToNote[Eb6] = keyToNote[Eb5] + 12
keyToNote[E6]  = keyToNote[E5]  + 12
keyToNote[F6]  = keyToNote[F5]  + 12
keyToNote[Fs6] = keyToNote[Fs5] + 12
keyToNote[Gb6] = keyToNote[Gb5] + 12
keyToNote[G6]  = keyToNote[G5]  + 12
keyToNote[Gs6] = keyToNote[Gs5] + 12
keyToNote[Ab6] = keyToNote[Ab5] + 12
keyToNote[A6]  = keyToNote[A5]  + 12
keyToNote[As6] = keyToNote[As5] + 12
keyToNote[Bb6] = keyToNote[Bb5] + 12
keyToNote[B6]  = keyToNote[B5]  + 12
keyToNote[C7]  = keyToNote[C6]  + 12
keyToNote[Cs7] = keyToNote[Cs6] + 12
keyToNote[Db7] = keyToNote[Db6] + 12
keyToNote[D7]  = keyToNote[D6]  + 12
keyToNote[Ds7] = keyToNote[Ds6] + 12
keyToNote[Eb7] = keyToNote[Eb6] + 12
keyToNote[E7]  = keyToNote[E6]  + 12
keyToNote[F7]  = keyToNote[F6]  + 12
keyToNote[Fs7] = keyToNote[Fs6] + 12
keyToNote[Gb7] = keyToNote[Gb6] + 12
keyToNote[G7]  = keyToNote[G6]  + 12
keyToNote[Gs7] = keyToNote[Gs6] + 12
keyToNote[Ab7] = keyToNote[Ab6] + 12
keyToNote[A7]  = keyToNote[A6]  + 12
keyToNote[As7] = keyToNote[As6] + 12
keyToNote[Bb7] = keyToNote[Bb6] + 12
keyToNote[B7]  = keyToNote[B6]  + 12

keyToNote[Gb2] = keyToNote[Gb3] - 12
keyToNote[Ab2] = keyToNote[Ab3] - 12
keyToNote[Bb2] = keyToNote[Bb3] - 12

keyToNote[Bb1] = keyToNote[Bb3] - 24
keyToNote[Db2] = keyToNote[Db3] - 12
keyToNote[Eb2] = keyToNote[Eb3] - 12

# hex values should be in uppercase, so do it myself
HEXES = "0123456789ABCDEF"


def toHex(i):
    return HEXES[(i >> 4) & 0xF] + HEXES[i & 0xF]


note_down = [
    "KAM11000KSQ10001031",
    "KAM11000KSQ10001032",
    "KAM11000KSQ10001033"
]

note_up = [
    "KAM12100KSQ10001031",
    "KAM12100KSQ10001032",
    "KAM12100KSQ10001033",
]

beat_down = "KAM12100KSQ10001034"

beat_up = "KAM12100KSQ10001034"

fret_down = [
    "KAM11000KSQ10001125",
    "KAM11000KSQ10001128",
    "KAM11000KSQ10001127",
]

fret_up = [
    "KAM12000KSQ10001125",
    "KAM12000KSQ10001128",
    "KAM12000KSQ10001127",
]

none = "None"

default_options = "Actv01Stop00OutO00"

chord_down_options = [
    "",
    "Actv01Stop00OutO00StMa00000001if(h1<3)h1=h1+1",
    "Actv01Stop00OutO00StMa00000001if(h1<3)h1=h1+2",
]

chord_up_options = [
    "",
    "Actv01Stop00OutO00StMa00000001if(h1>0)h1=h1-1",
    "Actv01Stop00OutO00StMa00000002if(h1>0)h1=h1-1if(h1>0)h1=h1-1",
]


def if_chord_options(c0, c1, c2):
    if c0 and c1 and c2:
        return default_options

    if not c0 and not c1 and not c2:
        return None

    if c0 and not c1 and not c2:
        return "Actv01Stop00OutO00StMa00000001if(h1!=0)noexecute"

    if not c0 and c1 and not c2:
        return "Actv01Stop00OutO00StMa00000001if(h1!=1)noexecute"

    if not c0 and not c1:
        return "Actv01Stop00OutO00StMa00000001if(h1<2)noexecute"

    if c0 and c1:
        return "Actv01Stop00OutO00StMa00000001if(h1>=2)noexecute"

    if c0:
        return "Actv01Stop00OutO00StMa00000001if(h1==1)noexecute"

    return "Actv01Stop00OutO00StMa00000001if(h1==0)noexecute"


timerStartAction = [
    "Tim0TimS0005fret11:2000:1",
    "Tim0TimS0005fret21:2000:1",
    "Tim0TimS0005fret31:2000:1"
]

timerKillAction = [
    "Tim0TimK0005fret1",
    "Tim0TimK0005fret2",
    "Tim0TimK0005fret3"
]

timerIncoming = [
    "Tim0TimT0005fret1",
    "Tim0TimT0005fret2",
    "Tim0TimT0005fret3"
]

key_space_down = "KAM11000KSQ10001020"
key_space_up = "KAM12100KSQ10001020"


def appendStaticHeader(buffer):
    buffer.write(
        "; ------- Bome MIDI Translator: Signed Project File\n" +
        "; ------- You can modify this file as you like, but that will invalidate\n" +
        "; ------- the signature so that it cannot be opened in MT Player anymore.\n" +
        ";\n")


def appendStaticPresets(buffer, presetCount):
    buffer.write(
        "[Preset." + str(presetCount) + "]\n" +
        "Name=Switch\n" +
        "Active=1\n" +
        "PresetSwitchIgnore=1\n" +
        "Name0=Next\n" +
        "Incoming0=MID3<Incoming Action=\"MIDI\"><Simple Type=\"PitchBend\"><Channel num=\"0\"/><Value1 num=\"0x1FFF\"/></Simple></Incoming>\n" +
        "Outgoing0=Pres000000\n" +
        "Options0=Actv01Stop00OutO00\n" +
        "Name1=Next\n" +
        "Incoming1=MID3<Incoming Action=\"MIDI\"><Simple Type=\"PitchBend\"><Channel num=\"0\"/><Value1 num=\"0x1FFF\"/></Simple></Incoming>\n" +
        "Outgoing1=KAM11000KSQ10001009\n" +
        "Options1=Actv01Stop00OutO00\n" +
        "Name2=Clear\n" +
        "Incoming2=MID3<Incoming Action=\"MIDI\"><Simple Type=\"PitchBend\"><Channel num=\"0\"/><Value1 num=\"0x00\"/></Simple></Incoming>\n" +
        "Outgoing2=KAM12100KSQ10001009\n" +
        "Options2=Actv01Stop00OutO00\n" +
        "Name3=First\n" +
        "Incoming3=MID3<Incoming Action=\"MIDI\"><Simple Type=\"PitchBend\"><Channel num=\"0\"/><Value1 num=\"0xFFFFE000\"/></Simple></Incoming>\n" +
        "Outgoing3=Pres020010Minor Pentatonic\n" +
        "Options3=Actv01Stop00OutO00\n" +
        "Name4=Clear\n" +
        "Incoming4=MID3<Incoming Action=\"MIDI\"><Simple Type=\"PitchBend\"><Channel num=\"0\"/><Value1 num=\"0x00\"/></Simple></Incoming>\n" +
        "Outgoing4=None\n" +
        "Options4=Actv01Stop00OutO00\n" +
        "\n")
    presetCount += 1

    return presetCount


def appendStaticFooter(buffer):
    buffer.write(
        "\n" +
        "[Project]\n" +
        "Version=2\n" +
        "Author=Buff00n\n" +
        "AuthorContact=\n" +
        "Comments=\n" +
        "AuthorWWW=https://www.youtube.com/@Buff00n\n" +
        "AuthorCopyright=\n" +
        # This is for my setup
        # you will have to change this in Bome for your MIDI device
        "DefaultInPorts=MIDA00010008FANTOM-X\n" +
        "DefaultOutPorts=MIDA0000"
    )


def presetStringForNote(index: int, name: str, note: int, on: bool, action: str, options: str = default_options) -> str:
    incoming = "MID3<Incoming Action=\"MIDI\"><Simple Type=\"" + ("NoteOn" if on else "NoteOff") + "\"><Channel num=\"0\"/><Value1 num=\"0x" + toHex(note) + "\"/><Value2 num=\"0x00\" Type=\"Any\"/></Simple></Incoming>"
    return presetString(index, name, incoming, action, options)


def presetString(index: int, name: str, incoming: str, action: str, options: str) -> str:
    return "Name" + str(index) + "=" + name + "\n" + \
           "Incoming" + str(index) + "=" + incoming + "\n" + \
           "Outgoing" + str(index) + "=" + action + "\n" + \
           "Options" + str(index) + "=" + options + "\n"


class FingeringSpec:
    def __init__(self, key: int, frets: [int]):
        self.key = key
        self.frets = frets


def f(string: int, *frets: int) -> FingeringSpec:
    return FingeringSpec(string, frets)


class Fingering(ABC):
    @abstractmethod
    def getFingeringSpec(self, index: int, chordType: int) -> FingeringSpec:
        pass

    @abstractmethod
    def getChordEnableNotes(self, chordType: int, scale: [str]) -> [int]:
        pass


class NoteFingering(Fingering):
    def __init__(self, specs: [[FingeringSpec]]):
        self.specs = specs

    def getFingeringSpec(self, index: int, chordType: int) -> FingeringSpec:
        if len(self.specs) <= chordType:
            return None

        if len(self.specs[chordType]) <= index:
            return None

        return self.specs[chordType][index]

    def getChordEnableNotes(self, chordType: int, scale: [str]) -> [int]:
        if chordType == 1:
            return [keyToNote.get(Ab2)]
        elif chordType == 2:
            return [keyToNote.get(Bb2)]

        return None


class SingleChordTypeFingering(NoteFingering):
    def __init__(self, specs):
        super().__init__(specs)

    def getChordEnableNotes(self, chordType: int, scale: [str]) -> [int]:
        # only one chord type
        if chordType != 1:
            return None

        # list of chord enabling notes
        notes = []

        # get the minimum note in the scale
        minNote = min([keyToNote[n] for n in scale])

        # subtract an octave from all notes and add the ones that are below the min note
        for note in [keyToNote[n] for n in scale]:
            if note - 12 < minNote:
                notes.append(note - 12)

        # get the maximum  note in the scale
        maxNote = max([keyToNote[n] for n in scale])

        # add an octave toall notes and add the ones that are above the max note
        for note in [keyToNote[n] for n in scale]:
            if note + 12 > maxNote:
                notes.append(note + 12)

        # convert to an int[]
        return notes

defaultFingering = NoteFingering([
    [f(1), f(2), f(3), f(1, 1), f(2, 1), f(3, 1), f(1, 2), f(2, 2), f(3, 2), f(1, 3), f(2, 3), f(3, 3)],
    [f(1, 1, 2), f(2, 1, 2), f(3, 1, 2), f(1, 2, 3), f(2, 2, 3), f(3, 2, 3)],
    [f(1, 1, 3), f(2, 1, 3), f(3, 1, 3), f(1, 1, 2, 3), f(2, 1, 2, 3), f(3, 1, 2, 3)]
])

singleChordTypeFingering = SingleChordTypeFingering([
    [f(1), f(2), f(3), f(1, 1), f(2, 1), f(3, 1), f(1, 2), f(2, 2), f(3, 2), f(1, 3), f(2, 3), f(3, 3)],
    [f(1, 1, 2), f(2, 1, 2), f(3, 1, 2), f(1, 2, 3), f(2, 2, 3), f(3, 2, 3), f(1, 1, 3), f(2, 1, 3), f(3, 1, 3), f(1, 1, 2, 3), f(2, 1, 2, 3), f(3, 1, 2, 3)]
])

corbuMinorFingering = NoteFingering([
    [f(1), f(2), f(3), f(1, 1), f(2, 1), f(3, 1), f(1, 2), f(2, 2), f(3, 2), f(1, 3), f(2, 3), f(3, 3)],
    # Corbu minor scale chords skip the D base
    [f(1, 1, 2), None, f(2, 1, 2), f(3, 1, 2), f(1, 2, 3), f(2, 2, 3), f(3, 2, 3)],
    [f(1, 1, 3), None, f(2, 1, 3), f(3, 1, 3), f(1, 1, 2, 3), f(2, 1, 2, 3), f(3, 1, 2, 3)]
])

corbuHexFingering = NoteFingering([
    [f(1), f(2), f(3), f(1, 1), f(2, 1), f(3, 1), f(1, 2), f(2, 2), f(3, 2), f(1, 3), f(2, 3), f(3, 3)],
    # Corbu hex scale chords skip the F# base
    [f(1, 1, 2), f(2, 1, 2), f(3, 1, 2), None, f(1, 2, 3), f(2, 2, 3), f(3, 2, 3)],
    [f(1, 1, 3), f(2, 1, 3), f(3, 1, 3), None, f(1, 1, 2, 3), f(2, 1, 2, 3), f(3, 1, 2, 3)]
])

corbuFridgeFingering = NoteFingering([
    [f(1), f(2), f(3), f(1, 1), f(2, 1), f(3, 1), f(1, 2), f(2, 2), f(3, 2), f(1, 3), f(2, 3), f(3, 3)],
    # Corbu phrygian scale chords skip the E base
    [f(1, 1, 2), f(2, 1, 2), None, f(3, 1, 2), f(1, 2, 3), f(2, 2, 3), f(3, 2, 3)],
    [f(1, 1, 3), f(2, 1, 3), None, f(3, 1, 3), f(1, 1, 2, 3), f(2, 1, 2, 3), f(3, 1, 2, 3)]
])


class FingeringProvider(ABC):
    @abstractmethod
    def getFingering(self, presetName: str) -> Fingering:
        pass


class GenericFingeringProvider(FingeringProvider):
    def getFingering(self, presetName: str) -> Fingering:
        if presetName == "Chromatic":
            return singleChordTypeFingering
        else:
            return defaultFingering

genericFingering = GenericFingeringProvider()


class TiamatFingeringProvider(FingeringProvider):
    def getFingering(self, presetName: str) -> Fingering:
        return singleChordTypeFingering

tiamatFingering = TiamatFingeringProvider()

class CorbuFingeringProvider(FingeringProvider):
    def getFingering(self, presetName: str) -> Fingering:
        if presetName == "Chromatic":
            return singleChordTypeFingering
        elif presetName == "Minor":
            return corbuMinorFingering
        elif presetName == "Hexatonic":
            return corbuHexFingering
        elif presetName == "Phrygian":
            return corbuFridgeFingering
        else :
            return defaultFingering

corbuFingering = CorbuFingeringProvider()


def addStaticTranslators(buffer: TextIOBase, index: int, scale: [str], fingering: Fingering) -> int:
    for i in range(3):
        buffer.write(presetString(index, "fret" + str(i + 1) + "-off", timerIncoming[i], fret_up[i], default_options))
        index += 1

    chord1EnabledNotes = fingering.getChordEnableNotes(1, scale)
    if chord1EnabledNotes is not None:
        for chord1EnabledNote in chord1EnabledNotes:
            buffer.write(presetStringForNote(index, "chords1-on", chord1EnabledNote, True, none, chord_down_options[1]))
            index += 1
            buffer.write(presetStringForNote(index, "chords1-off", chord1EnabledNote, False, none, chord_up_options[1]))
            index += 1

    chord2EnabledNotes = fingering.getChordEnableNotes(2, scale)
    if chord2EnabledNotes is not None:
        for chord2EnabledNote in chord2EnabledNotes:
            buffer.write(presetStringForNote(index, "chords2-on", chord2EnabledNote, True, none, chord_down_options[2]))
            index += 1
            buffer.write(presetStringForNote(index, "chords2-off", chord2EnabledNote, False, none, chord_up_options[2]))
            index += 1

    buffer.write(presetStringForNote(index, "Whammy-on", keyToNote.get(Gb2), True, key_space_down))
    index += 1
    buffer.write(presetStringForNote(index, "Whammy-off", keyToNote.get(Gb2), False, key_space_up))
    index += 1

    buffer.write(presetStringForNote(index, "beat-key-on", keyToNote.get(Bb1), True, beat_down))
    index += 1
    buffer.write(presetStringForNote(index, "beat-key-off", keyToNote.get(Bb1), False, beat_up))
    index += 1

    return index


class Entry:
    def __init__(self, name: str, note: int, specs: [FingeringSpec]):
        self.name = name
        self.note = note
        self.specs = specs


def addTranslators(buffer: TextIOBase, index: int, entry: Entry) -> int:
    # kill any outstanding fret off timers
    for i in range(3):
        buffer.write(presetStringForNote(index, entry.name + "-timer-" + str(i + 1) + "-cancel", entry.note, True, timerKillAction[i]))
        index += 1

    for i in range(3):
        fretsOn = [
            entry.specs[0] is not None and i+1 in entry.specs[0].frets,
            entry.specs[1] is not None and i+1 in entry.specs[1].frets,
            entry.specs[2] is not None and i+1 in entry.specs[2].frets
        ]
        on_options = if_chord_options(fretsOn[0], fretsOn[1], fretsOn[2])
        off_options = if_chord_options(not fretsOn[0], not fretsOn[1], not fretsOn[2])

        if on_options is not None:
            buffer.write(presetStringForNote(index, entry.name + "-fret-" + str(i + 1) + "-on", entry.note, True, fret_down[i], on_options))
            index += 1
            buffer.write(presetStringForNote(index, entry.name + "-timer-" + str(i + 1) + "-start", entry.note, True, timerStartAction[i], on_options))
            index += 1

        if off_options is not None:
            buffer.write(presetStringForNote(index, entry.name + "-fret-" + str(i + 1) + "-off", entry.note, True, fret_up[i], off_options))
            index += 1

    # figure out if all the non-None specs have the same key
    oneKey = -1
    for i in range(3):
        if entry.specs[i] is not None:
            if oneKey == -1:
                oneKey = entry.specs[i].key
            elif oneKey != entry.specs[i].key:
                oneKey = -1
                break

    if oneKey > 0:
        # simple case: all chord types are on the same string
        note_options = if_chord_options(entry.specs[0] is not None, entry.specs[1] is not None, entry.specs[2] is not None)

        # kill any down keys
        for i in range(1, 4):
            buffer.write(presetStringForNote(index, entry.name + "-note-" + str(i) + "-off", entry.note, True, note_up[i - 1], note_options))
            index += 1

        # note on
        buffer.write(presetStringForNote(index, entry.name + "-note-" + str(oneKey) + "-on", entry.note, True, note_down[oneKey - 1], note_options))
        index += 1

        # note off
        buffer.write(presetStringForNote(index, entry.name + "-note-" + str(oneKey) + "-off", entry.note, False, note_up[oneKey - 1], note_options))
        index += 1

    else:
        # complicated case, THANKS CORBU
        # should be equivalent to the simple case when all present specs have the same key
        # build a mapping from each key to the chord types that trigger it
        key_ct_mapping = [None for _ in range(3)]
        for i in range(3):
            if entry.specs[i] is not None:
                if key_ct_mapping[entry.specs[i].key - 1] is None:
                    key_ct_mapping[entry.specs[i].key - 1] = [False for _ in range(3)]

                key_ct_mapping[entry.specs[i].key - 1][i] = True

        for k in range(3):
            if key_ct_mapping[k] is not None:
                # key
                oneKey = k + 1

                # get note options for the combination of chord types
                note_options = if_chord_options(key_ct_mapping[k][0], key_ct_mapping[k][1], key_ct_mapping[k][2])

                # kill any down keys
                for i in range(1, 4):
                    buffer.write(presetStringForNote(index, entry.name + "-note-" + str(i) + "-off", entry.note, True, note_up[i - 1], note_options))
                    index += 1

                # note on
                buffer.write(presetStringForNote(index, entry.name + "-note-" + str(oneKey) + "-on", entry.note, True, note_down[oneKey - 1], note_options))
                index += 1

                # note off
                buffer.write(presetStringForNote(index, entry.name + "-note-" + str(oneKey) + "-off", entry.note, False, note_up[oneKey - 1], note_options))
                index += 1

    return index


def buildEntries(scale: [str], fingering: Fingering) -> [Entry]:
    entryList = []

    for i in range(len(scale)):
        note = keyToNote.get(scale[i])
        entryList.append(Entry(scale[i], note, [
                    fingering.getFingeringSpec(i, 0),
                    fingering.getFingeringSpec(i, 1),
                    fingering.getFingeringSpec(i, 2)
        ]))

    return entryList


def writePreset(buffer: TextIOBase,
                presetName: str,
                scale: [str],
                fingering: [Fingering],
                presetCount: int) -> None:
        buffer.write("[Preset." + str(presetCount) + "]\n" +
                      "Name=" + presetName + "\n" +
                      "Active=" + ("1" if presetCount == 0 else"0") + "\n" +
                      "PresetSwitchIgnore=0\n")

        entries = buildEntries(scale, fingering)
        count = addStaticTranslators(buffer, 0, scale, fingering)
        for entry in entries:
            count = addTranslators(buffer, count, entry)


def writePresets(buffer, fingeringProvider):
    presetCount = 0

    writePreset(buffer, "Minor Pentatonic", [
            C3, Eb3, F3,
            G3, Bb3, C4,
            Eb4, F4, G4,
            Bb4, C5, Eb5
    ], fingeringProvider.getFingering("Minor Pentatonic"), presetCount)
    presetCount += 1

    writePreset(buffer, "Major Pentatonic", [
            C3, D3, E3,
            G3, A3, C4,
            D4, E4, G4,
            A4, C5, D5
    ], fingeringProvider.getFingering("Major Pentatonic"), presetCount)
    presetCount += 1

    writePreset(buffer, "Chromatic", [
            C3, Cs3, D3,
            Ds3, E3, F3,
            Fs3, G3, Gs3,
            A3, As3, B3
    ], fingeringProvider.getFingering("Chromatic"), presetCount)
    presetCount += 1

    writePreset(buffer, "Hexatonic", [
            C3, Eb3, F3,
            Fs3, G3, Bb3,
            C4, Eb4, F4,
            Fs4, G4, Bb4,
    ], fingeringProvider.getFingering("Hexatonic"), presetCount)
    presetCount += 1

    writePreset(buffer, "Major",[
            C3, D3, E3,
            F3, G3, A3,
            B3, C4, D4,
            E4, F4, G4
    ], fingeringProvider.getFingering("Major"), presetCount)
    presetCount += 1

    writePreset(buffer, "Minor", [
            C3, D3, Eb3,
            F3, G3, Ab3,
            Bb3, C4, D4,
            Eb4, F4, G4
    ], fingeringProvider.getFingering("Minor"), presetCount)
    presetCount += 1

    writePreset(buffer, "Hirajoshi",[
            C3, Cs3, F3,
            Fs3, Bb3, C4,
            Cs4, F4, Fs4,
            A4, C5, Cs5
    ], fingeringProvider.getFingering("Hirajoshi"), presetCount)
    presetCount += 1

    writePreset(buffer, "Phrygian", [
            C3, Cs3, E3,
            F3, G3, Ab3,
            Bb3, C4, Cs4,
            E4, F4, G4
    ], fingeringProvider.getFingering("Phrygian"), presetCount)
    presetCount += 1

    writePreset(buffer, "Yo", [
            Db3, Eb3, Gb3,
            Ab3, Bb3, Db4,
            Eb4, Gb4, Ab4,
            Bb4, Db5, Eb5
    ], fingeringProvider.getFingering("Yo"), presetCount)
    presetCount += 1

    return presetCount


def writeFile(fileName: str, fingeringProvider: FingeringProvider) -> None:
    buffer = open(fileName, "w")

    appendStaticHeader(buffer)

    presetCount = writePresets(buffer, fingeringProvider)

    appendStaticPresets(buffer, presetCount)

    appendStaticFooter(buffer)

    buffer.close()


writeFile("shawzin-generic-v7.bmtp", genericFingering)
writeFile("shawzin-tiamat-v7.bmtp", tiamatFingering)
writeFile("shawzin-corbu-v7.bmtp", corbuFingering)
