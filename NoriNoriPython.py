# ============================================================= #
# References                                                    #
# https://zenn.dev/kaityo256/articles/python_play_sound         #
# https://3pysci.com/python-sound-1/                            #
# https://tat-pytone.hatenablog.com/entry/2022/10/16/150017     #
# ============================================================= #

import numpy as np
from scipy.io.wavfile import write
from pydub import AudioSegment
from IPython.display import Audio

L = 8; T = 4

# scales as integers.
Cu = -11
CuS = -10
Du = -9
DuS = -8
Eu = -7
Fu = -6
FuS = -5
Gu = -4
GuS = -3
Au = -2
AuS = -1
Bu = 0
C = 1
CS = 2
D = 3
DS = 4
E = 5
F = 6
FS = 7
G = 8
GS = 9
A = 10
AS = 11
B = 12
C1 = 13
C1S = 14
D1 = 15
D1S = 16
E1 = 17
F1 = 18
F1S = 19
G1 = 20
G1S = 21
A1 = 22
A1S = 23
B1 = 24


# Pythagorean scale like(?)
PythagorasTuning = np.hstack([0, 440 * 2 ** ((np.arange(36) - 20) / 12)])

Notes = np.arange(36) - 11
dic = {}
for i, s in enumerate(Notes):
    dic[s] = i


# Generates music
def PlayMusic(Score, name):
    rate = 48000
    BPM = 180 * T
    music = np.array([])
    for s in Score:
        d = 60 / BPM * s[1]
        t = np.linspace(0, d, int(rate * d))
        f = PythagorasTuning[dic[s[0]]]
        music = np.append(music, np.sin((np.pi + np.pi) * f * t))

    music = np.asarray(music, dtype = np.float32)
    write(name, rate = rate, data = music)


# score
UnwelcomeSchool1 = [
    [A, 4],
    [C1, 4],
    [D1S, 3],
    [E1, 3],
    [GS, 2],
    [A, 2],
    [C1, 2],
    [D1, 2],
    [C1, 2],
    [D1S, 3],
    [E1, 5],
    [G1, 2],
    [F1S, 2],
    [F1, 2],
    [E1, 2],
    [D1, 2],
    [C1, 2],
    [B, 2],
    [AS, 2],
    [B, 2],
    [C1, 2],
    [D1, 2],
    [D1S, 2],
    [E1, 4],
    [GS, 4]
]

UnwelcomeSchool2 = [
    [A, 4],
    [C1, 4],
    [D1S, 3],
    [E1, 3],
    [GS, 2],
    [A, 2],
    [C1, 2],
    [D1, 2],
    [C1, 2],
    [D1S, 3],
    [E1, 5],
    [G1, 2],
    [F1S, 2],
    [F1, 2],
    [E1, 2],
    [E1, 2],
    [F1, 2],
    [F1S, 2],
    [G1, 2],
    [G1S, 2],
    [G1S, 2],
    [A1, 2],
    [A1, 2],
    [B1, 8]
]

UnwelcomeSchool3 = [
    [E1, 2],
    [D1, 2],
    [E1, 2],
    [F1, 2],
    [E1, 2],
    [D1, 2],
    [C1, 2],
    [D1, 2],
    [E1, 2],
    [D1, 2],
    [E1, 2],
    [F1, 2],
    [E1, 2],
    [D1, 2],
    [C1, 2],
    [B, 2],
    [A, 4],
    [A1, 4],
    [G1S, 4],
    [G1, 4],
    [F1, 4],
    [E1, 4],
    [D1S, 4],
    [E1, 4]
]

UnwelcomeSchool4 = [
    [E1, 2],
    [D1, 2],
    [E1, 2],
    [F1, 2],
    [E1, 2],
    [D1, 2],
    [C1, 2],
    [D1, 2],
    [E1, 2],
    [D1, 2],
    [E1, 2],
    [F1, 2],
    [E1, 2],
    [D1, 2],
    [C1, 2],
    [D1, 2],
    [A1, 4],
    [A, 4],
    [B, 4],
    [C1, 4],
    [C1S, 4],
    [D1, 4],
    [F1, 4],
    [E1, 4]
]

UnwelcomeSchool5 = [
    [E1, 2],
    [D1, 2],
    [E1, 2],
    [F1, 2],
    [E1, 2],
    [D1, 2],
    [C1, 2],
    [D1, 2],
    [E1, 2],
    [D1, 2],
    [E1, 2],
    [F1, 2],
    [E1, 2],
    [D1, 2],
    [C1, 2],
    [B, 2],
    [A, 4],
    [D1S, 2],
    [C1, 2],
    [D1, 2],
    [C1, 2],
    [A, 2],
    [C1, 2],
    [D1S, 2],
    [C1, 2],
    [D1, 2],
    [C1, 14],
    [D1S, 2],
    [C1, 2],
    [D1, 2],
    [C1, 2],
    [A, 2],
    [C1, 2],
    [D1S, 2],
    [C1, 2],
    [D1, 2],
    [C1, 10]
]

AE = [[Au, 2], [E, 2]]
FC = [[Fu, 2], [C, 2]]
GB = [[Gu, 2], [D, 2]]
CG = [[C, 2], [G, 2]]

UnwelcomeSchoolSub = (AE * 8 + FC * 4 + GB * 4) * 6 + (FC * 4 + GB * 4 + AE * 4 + CG * 4) * 3 + FC * 4 + GB * 4
UnwelcomeSchool = (UnwelcomeSchool1 + UnwelcomeSchool2) * 3 + UnwelcomeSchool3 + UnwelcomeSchool4 + UnwelcomeSchool3 + UnwelcomeSchool5


# Generate wav files
PlayMusic(UnwelcomeSchool, 'NoriNoriMain.wav')
PlayMusic(UnwelcomeSchoolSub, 'NoriNoriSub.wav')


# synthesis wav files
Main = AudioSegment.from_file('NoriNoriMain.wav')
Sub = AudioSegment.from_file('NoriNoriSub.wav')

output = Main.overlay(Sub, position = 0)
output.export('NoriNoriPython.wav', format = 'wav')


Audio('NoriNoriPython.wav')
