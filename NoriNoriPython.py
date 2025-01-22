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

# scales as integers.
C_lower = -11
C_sharp_lower = -10
D_lower = -9
D_sharp_lower = -8
E_lower = -7
F_lower = -6
F_sharp_lower = -5
G_lower = -4
G_sharp_lower = -3
A_lower = -2
A_sharp_lower = -1
B_lower = 0
C = 1
C_sharp = 2
D = 3
D_sharp = 4
E = 5
F = 6
F_Sharp = 7
G = 8
G_sharp = 9
A = 10
A_sharp = 11
B = 12
C_upper = 13
C_sharp_upper = 14
D_upper = 15
D_sharp_upper = 16
E_upper = 17
F_upper = 18
F_sharp_upper = 19
G_upper = 20
G_sharp_upper = 21
A_upper = 22
A_sharp_upper = 23
B_upper = 24


# Pythagorean scale like(?)
pythagoras_tuning = np.hstack([0, 440 * 2 ** ((np.arange(36) - 20) / 12)])

notes = np.arange(36) - 11
dic = {}
for i, s in enumerate(notes):
    dic[s] = i

def playMusic(score: list, music_name: str) -> None:
    """A function that generates music with wav format by given list representing score.

    Args:
        score (list): list that represents score
        music_name (str): name of wav file
    """
    rate = 48000
    bpm = 180 * 4
    music = np.array([])
    for s in score:
        d = 60 / bpm * s[1]
        t = np.linspace(0, d, int(rate * d))
        f = pythagoras_tuning[dic[s[0]]]
        music = np.append(music, np.sin((np.pi + np.pi) * f * t))

    music = np.asarray(music, dtype = np.float32)
    write(music_name, rate = rate, data = music)


# score
unwelcome_schoole_1 = [
    [A, 4],
    [C_upper, 4],
    [D_sharp_upper, 3],
    [E_upper, 3],
    [G_sharp, 2],
    [A, 2],
    [C_upper, 2],
    [D_upper, 2],
    [C_upper, 2],
    [D_sharp_upper, 3],
    [E_upper, 5],
    [G_upper, 2],
    [F_sharp_upper, 2],
    [F_upper, 2],
    [E_upper, 2],
    [D_upper, 2],
    [C_upper, 2],
    [B, 2],
    [A_sharp, 2],
    [B, 2],
    [C_upper, 2],
    [D_upper, 2],
    [D_sharp_upper, 2],
    [E_upper, 4],
    [G_sharp, 4]
]

unwelcome_schoole_2 = [
    [A, 4],
    [C_upper, 4],
    [D_sharp_upper, 3],
    [E_upper, 3],
    [G_sharp, 2],
    [A, 2],
    [C_upper, 2],
    [D_upper, 2],
    [C_upper, 2],
    [D_sharp_upper, 3],
    [E_upper, 5],
    [G_upper, 2],
    [F_sharp_upper, 2],
    [F_upper, 2],
    [E_upper, 2],
    [E_upper, 2],
    [F_upper, 2],
    [F_sharp_upper, 2],
    [G_upper, 2],
    [G_sharp_upper, 2],
    [G_sharp_upper, 2],
    [A_upper, 2],
    [A_upper, 2],
    [B_upper, 8]
]

unwelcome_schoole_3 = [
    [E_upper, 2],
    [D_upper, 2],
    [E_upper, 2],
    [F_upper, 2],
    [E_upper, 2],
    [D_upper, 2],
    [C_upper, 2],
    [D_upper, 2],
    [E_upper, 2],
    [D_upper, 2],
    [E_upper, 2],
    [F_upper, 2],
    [E_upper, 2],
    [D_upper, 2],
    [C_upper, 2],
    [B, 2],
    [A, 4],
    [A_upper, 4],
    [G_sharp_upper, 4],
    [G_upper, 4],
    [F_upper, 4],
    [E_upper, 4],
    [D_sharp_upper, 4],
    [E_upper, 4]
]

unwelcome_schoole_4 = [
    [E_upper, 2],
    [D_upper, 2],
    [E_upper, 2],
    [F_upper, 2],
    [E_upper, 2],
    [D_upper, 2],
    [C_upper, 2],
    [D_upper, 2],
    [E_upper, 2],
    [D_upper, 2],
    [E_upper, 2],
    [F_upper, 2],
    [E_upper, 2],
    [D_upper, 2],
    [C_upper, 2],
    [D_upper, 2],
    [A_upper, 4],
    [A, 4],
    [B, 4],
    [C_upper, 4],
    [C_sharp_upper, 4],
    [D_upper, 4],
    [F_upper, 4],
    [E_upper, 4]
]

unwelcome_schoole_5 = [
    [E_upper, 2],
    [D_upper, 2],
    [E_upper, 2],
    [F_upper, 2],
    [E_upper, 2],
    [D_upper, 2],
    [C_upper, 2],
    [D_upper, 2],
    [E_upper, 2],
    [D_upper, 2],
    [E_upper, 2],
    [F_upper, 2],
    [E_upper, 2],
    [D_upper, 2],
    [C_upper, 2],
    [B, 2],
    [A, 4],
    [D_sharp_upper, 2],
    [C_upper, 2],
    [D_upper, 2],
    [C_upper, 2],
    [A, 2],
    [C_upper, 2],
    [D_sharp_upper, 2],
    [C_upper, 2],
    [D_upper, 2],
    [C_upper, 14],
    [D_sharp_upper, 2],
    [C_upper, 2],
    [D_upper, 2],
    [C_upper, 2],
    [A, 2],
    [C_upper, 2],
    [D_sharp_upper, 2],
    [C_upper, 2],
    [D_upper, 2],
    [C_upper, 10]
]

AE = [[A_lower, 2], [E, 2]]
FC = [[F_lower, 2], [C, 2]]
GB = [[G_lower, 2], [D, 2]]
CG = [[C, 2], [G, 2]]

sub_melody = (AE * 8 + FC * 4 + GB * 4) * 6 + (FC * 4 + GB * 4 + AE * 4 + CG * 4) * 3 + FC * 4 + GB * 4
main_melody = (unwelcome_schoole_1 + unwelcome_schoole_2) * 3 + unwelcome_schoole_3 + unwelcome_schoole_4 + unwelcome_schoole_3 + unwelcome_schoole_5


# Generate wav files
playMusic(main_melody, 'NoriNoriMain.wav')
playMusic(sub_melody, 'NoriNoriSub.wav')

# synthesis wav files
main_melody = AudioSegment.from_file('NoriNoriMain.wav')
sub_melody = AudioSegment.from_file('NoriNoriSub.wav')

output = main_melody.overlay(sub_melody, position = 0)
output.export('NoriNoriPython.wav', format = 'wav')


Audio('NoriNoriPython.wav')
