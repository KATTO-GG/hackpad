import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

# ---- 4 keys, direct GPIO (no matrix, each switch straight to a pin + shared GND) ----
# EDIT: swap board.Dx for real GPIO net names from KiCad (hover pin1 pad on each switch)
keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3)  # SW1, SW2, SW3, SW4 in order
keyboard.row_pins = None
keyboard.diode_orientation = None

# ---- Keymap ----
keyboard.keymap = [
    [KC.W, KC.A, KC.S, KC.D]  # match order of col_pins above to SW1-4
]

# ---- Rotary encoder (A/B only, no push button) ----
encoder_handler = EncoderHandler()
# EDIT: swap for real A/B net names (hover A and B pads on SW5)
encoder_handler.pins = ((board.D5, board.D6, None),)
encoder_handler.map = [
    ((KC.VOLU, KC.VOLD),)
]
keyboard.modules.append(encoder_handler)

if __name__ == '__main__':
    keyboard.go()

