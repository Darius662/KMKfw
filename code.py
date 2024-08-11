print("Starting")

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())

# Define the pin configurations for the columns and rows
keyboard.col_pins = (
    board.GP16, #board.GP17, 
   # board.GP18, board.GP19, 
   # board.GP20, board.GP21, 
   # board.GP22,
    )
keyboard.row_pins = (
    board.GP0, board.GP1, board.GP2, board.GP3,
    board.GP4, board.GP5, board.GP6, board.GP7,
    board.GP8, board.GP9, board.GP10, board.GP11,
    board.GP12, board.GP13, board.GP14,board.GP15,
    )
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Define the keymap
keyboard.keymap = [
    [
        KC.C,
        KC.LSFT(KC.C),
        KC.LALT(KC.C),
        KC.LCTRL(KC.C),
        KC.RSFT(KC.C),
        KC.KP_MINUS,
        KC.HASH,
        KC.LSFT(KC.I),
    ]
]

if __name__ == '__main__':
    keyboard.go()
