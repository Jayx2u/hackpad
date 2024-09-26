print("Starting ~w~")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

jaypad = KMKKeyboard()

jaypad.col_pins = (board.D0, board.D1, board.D2, board.D3)
jaypad.row_pins = (board.D9, board.D8, board.D7)
jaypad.diode_orientation = DiodeOrientation.COL2ROW

jaypad.keymap = [
    [KC.A,]
]

if __name__ == '__main__':
    jaypad.go()