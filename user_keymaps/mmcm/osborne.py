
import board

from kmk.keys import KC, make_key
from kmk.kmk_keyboard import KMKKeyboard
from kmk.matrix import DiodeOrientation

from kmk.open_collector_matrix import OpenCollectorMatrixScanner

# TODO: This does not, in fact, work.
make_key(code=130, names=('LOCKING_CAPS', 'LCAP'))

_______ = KC.TRNS
XXXXXXX = KC.NO

keyboard = KMKKeyboard()
keyboard.debug_enabled = True

keyboard.matrix_scanner = OpenCollectorMatrixScanner

keyboard.row_pins = (
    board.A0,                   # A0 pin 3
    board.D10,                  # A1 pin 8
    board.A2,                   # A5 pin 7
    board.D11,                  # A2 pin 6
    board.D12,                  # A3 pin 4
    board.D13,                  # A4 pin 2
    board.A1,                   # A6 pin 5
    board.A3,                   # A7 pin 9
)
keyboard.col_pins = (
    board.D9,                   # D0 pin 10
    board.A4,                   # D1 pin 11
    board.D7,                   # D2 pin 12
    board.A5,                   # D3 pin 13
    board.D1,                   # D4 pin 14
    board.SCK,                  # D5 pin 15
    board.D0,                   # D6 pin 16
    board.D2,                   # D7 pin 17
)
keyboard.diode_orientation = DiodeOrientation.ROWS

#  +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+      +---+---+---+
#  |ESC| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 | - | = | [ | ⇧ |      | 7 | 8 | 9 |
#  +-----------------------------------------------------------+-+    +-----------+
#  | TAB | Q | W | E | R | T | Y | U | I | O | P | \ | ' | ⇦ | ⇨ |    | 4 | 5 | 6 |
# ++----------------------------------------------------------+--+    +-----------+
# |CTL|LCK| A | S | D | F | G | H | J | K | L | ; |RETURN | ⇩ |       | 1 | 2 | 3 |
# +---+---------------------------------------------------++--+       +-----------+
#     |SHIFT| Z | X | C | V | B | N | M | , | . | / |SHIFT|           | 0 | . |ENT|
#     +---------+-------------------------------+---+-----+           +---+---+---+
#               |             SPACE             |
#               +-------------------------------+
#
# Both SHIFTs are connected. Numpad keys are connected to the corresponding keys in the main section.
# Matrix given at https://archive.org/details/bitsavers_osborneosbne1TechnicalManual1982_19169707/page/n63/mode/1up

keyboard.keymap = [
    [
        KC.ESC,   KC.TAB,   KC.LCTRL, XXXXXXX,  KC.LSFT,  KC.ENTER, KC.QUOTE, KC.LBRC,
        KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,    KC.N6,    KC.N7,    KC.N8,
        KC.MO(1), KC.BSPC,  KC.N0,    KC.SPACE, KC.DOT,   KC.P,     KC.O,     KC.N9,
        KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,     KC.Y,     KC.U,     KC.I,
        KC.A,     KC.S,     KC.D,     KC.F,     KC.G,     KC.H,     KC.J,     KC.K,
        KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,     KC.N,     KC.M,     KC.COMMA,
        KC.DEL,   KC.MO(2), KC.MINUS, KC.SLASH, KC.SCLN,  KC.SLASH, KC.L,     KC.EQUAL,
        XXXXXXX,  XXXXXXX,  XXXXXXX,  KC.LCAP,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX
    ],
    [
        KC.GRV,   _______,  _______,  _______,  _______,  _______,  _______,  KC.RBRC,
        _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,
        _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,
        _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,
        _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,
        _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,
        _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,
        _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______
    ],
    [
        _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,
        KC.END,   KC.DOWN,  KC.PGDN,  KC.LEFT,  _______,  KC.RGHT,  KC.HOME,  KC.UP,
        _______,  _______,  KC.INS,   _______,  KC.DEL,   _______,  _______,  KC.PGUP,
        _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,
        _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,
        _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,
        _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,
        _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______
    ]
]

if __name__ == '__main__':
    keyboard.go()
