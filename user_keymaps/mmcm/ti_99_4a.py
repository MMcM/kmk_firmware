
import board

from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.matrix import DiodeOrientation

from kmk.open_collector_matrix import OpenCollectorMatrixScanner

_______ = KC.TRNS
XXXXXXX = KC.NO

keyboard = KMKKeyboard()
keyboard.debug_enabled = True

keyboard.matrix_scanner = OpenCollectorMatrixScanner
keyboard.row_pins = (
    board.SCK,                  # pin 7
    board.D11,                  # pin 10
    board.A2,                   # pin 3
    board.D10,                  # pin 11
    board.A1,                   # pin 2
    board.A0,                   # pin 1
    board.A3,                   # pin 4
    board.A4,                   # pin 5
)
keyboard.col_pins = (
    board.A5,                   # pin 6
    board.D2,                   # pin 8
    board.D7,                   # pin 13
    board.D1,                   # pin 14
    board.D0,                   # pin 15
    board.D12,                  # pin 9
    board.D9,                   # pin 12
)
keyboard.diode_orientation = DiodeOrientation.ROWS

# +---+---+---+---+---+---+---+---+---+---+---+
# | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 | = |
# +-+-----------------------------------------+-+
#   | Q | W | E | R | T | Y | U | I | O | P | / |
#   ++------------------------------------------++
#    | A | S | D | F | G | H | J | K | L | ; |ENT|
#  +-+-------------------------------------------+
#  |SHF| Z | X | C | V | B | N | M | , | . |SHIFT|
#  +-------------------------------------------+-+
#  |CAP|CTL|             SPACE             |FCN|
#  +---+---+-------------------------------+---+
#
# Both SHIFTs are connected.
# Matrix given at http://www.mainbyte.com/ti99/keyboard/keyboard.html

def layout(
        k1,  k2,  k3,  k4,  k5,  k6,  k7,  k8,  k9, k10, k11,
        k12, k13, k14, k15, k16, k17, k18, k19, k20, k21, k22,
        k23, k24, k25, k26, k27, k28, k29, k30, k31, k32, k33,
        k34, k35, k36, k37, k38, k39, k40, k41, k42, k43,
        k45, k46, k47, k48
):
    return [
        k45,    k1,     k2,     k3,     k4,     k5,     k48,
        KC.NO,  k12,    k13,    k14,    k15,    k16,    k46,
        KC.NO,  k23,    k24,    k25,    k26,    k27,    k34,
        KC.NO,  k35,    k36,    k37,    k38,    k39,    KC.NO,
        KC.NO,  k10,    k9,     k8,     k7,     k6,     KC.NO,
        KC.NO,  k21,    k20,    k19,    k18,    k17,    k33,
        KC.NO,  k32,    k31,    k30,    k29,    k28,    k47,
        KC.NO,  k22,    k43,    k42,    k41,    k40,    k11
    ]

keyboard.keymap = [
    layout(
        KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,    KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.EQUAL,
        KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,     KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,     KC.SLASH,
        KC.A,     KC.S,     KC.D,     KC.F,     KC.G,     KC.H,     KC.J,     KC.K,     KC.L,     KC.SCLN,  KC.ENTER,
        KC.LSFT,  KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,     KC.N,     KC.M,     KC.COMMA, KC.DOT,
        KC.CAPS,  KC.LCTRL, KC.SPACE, KC.MO(1)
    ),
    layout(
        _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,
        _______,  KC.TILDE, KC.UP,    KC.LBRC,  KC.RBRC,  _______,  KC.UNDS,  KC.QUES,  KC.QUOTE, KC.DQUO,  _______,
        KC.PIPE,  KC.LEFT,  KC.RIGHT, KC.LCBR,  KC.RCBR,  _______,  _______,  _______,  _______,  _______,  _______,
        _______,  KC.BSLS,  KC.DOWN,  KC.GRAVE, _______,  _______,  _______,  _______,  _______,  _______,
        _______,  _______,  _______,  _______
    )
]

if __name__ == '__main__':
    keyboard.go()
