from kb import KMKKeyboard

from kmk.extensions.rgb import RGB
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType
from kmk.modules.capsword import CapsWord
from kmk.modules.modtap import ModTap
from kmk.handlers.sequences import send_string, simple_key_sequence

from hidden import PASSWORD, USER_PASS_SEQ

keyboard = KMKKeyboard()

################ MODULES #########################

# Auto recognize split side based on the drive name
# KEEBL - Left
# KEEBR - Right
split = Split(split_type=SplitType.UART, data_pin=keyboard.rx_pin, data_pin2=keyboard.tx_pin, use_pio=True)
layers_ext = Layers()
caps_word=CapsWord()
modtap = ModTap()
# TODO: write oled extension
# TODO: write wpm module

# add to keyboard
keyboard.modules = [layers_ext, split, caps_word, modtap]

############### OLED ###########################

# Main group
## layer group
## animation group
## wpm group
## keylocks group

############### CUSTOM KEYS ####################
_______ = KC.TRNS
XXXXXXX = KC.NO

# layers
SYMB = KC.MO(1)
NUMB = KC.MO(2)
NAV_M = KC.MO(3)
NAV_W = KC.MO(4)
FUNC = KC.MO(5)
CUST = KC.MO(6)
PASS = KC.MO(7)

# password
PWRD = send_string(PASSWORD)
UPS = simple_key_sequence(USER_PASS_SEQ)

# Homerow modtap
F_GUI = KC.MT(KC.F, KC.LGUI)
D_ALT = KC.MT(KC.D, KC.LALT)
S_CTL = KC.MT(KC.S, KC.LCTRL)
J_GUI = KC.MT(KC.J, KC.RGUI)
K_ALT = KC.MT(KC.K, KC.RALT)
L_CTL = KC.MT(KC.L, KC.RCTRL)

############## KEYMAP ########################

# TODO: get keymap from other keyboard
keyboard.keymap = [
    [  #QWERTY
        KC.ESC,    KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                         KC.Y,    KC.U,    KC.I,    KC.O,   KC.P,  KC.GRV,\
        KC.LCTL,   KC.A,   S_CTL,    D_ALT,  F_GUI,    KC.G,                         KC.H,   J_GUI,   K_ALT,   L_CTL, KC.SCLN, KC.ENT,\
        KC.CW,     KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,                         KC.N,    KC.M, KC.COMM,  KC.DOT, KC.SLSH, KC.BSLS,\
                                             NAV_M,    SYMB,  KC.LSFT,   KC.BSPC,  KC.SPC,    NUMB,
    ],
    [  #SYMB
        KC.ESC,   KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,                         KC.N6,     KC.N7,   KC.N8,   KC.N9,   KC.N0, _______,\
        _______, _______, KC.LCTL, KC.LALT, KC.LGUI, _______,                        _______, KC.RGUI, KC.RALT,KC.RCTRL, _______, _______,\
        _______, _______, _______, _______, _______, _______,                        _______, _______, _______, _______, _______, _______,\
                                               FUNC,    CUST,  _______,   _______,   _______, NUMB,
    ],
    [  #NUM
        KC.ESC, KC.EXLM,   KC.AT, KC.HASH,  KC.DLR, KC.PERC,                         KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN, KC.BSPC,\
        KC.LCTL, _______, _______, _______, _______, _______,                        KC.MINS,  KC.EQL, KC.LCBR, KC.RCBR, KC.PIPE,  KC.GRV,\
        KC.LSFT, _______, _______, _______, _______, _______,                        KC.UNDS, KC.PLUS, KC.LBRC, KC.RBRC, KC.BSLS, KC.TILD,\
                                            KC.LGUI,   LOWER,  ADJUST,     KC.ENT,   RAISE,  KC.RALT,
    ],
    [  #NAV_M (mac navigation)
        _______,  _______,  _______,  _______, _______, _______,                        _______, _______, _______, _______, _______, _______,\
        _______,  _______,  _______,  _______, _______, _______,                        _______, _______, _______, _______, _______, _______,\
        _______, _______, _______, _______, _______, _______,                        _______, _______, _______, _______, _______, _______,\
                                            KC.LGUI,   LOWER,  ADJUST,     KC.ENT,   RAISE,  KC.RALT,
    ]
    ,
    [  #NAV_W (windows navigation)
        _______,  _______,  _______,  _______, _______, _______,                        _______, _______, _______, _______, _______, _______,\
        _______,  _______,  _______,  _______, _______, _______,                        _______, _______, _______, _______, _______, _______,\
        _______, _______, _______, _______, _______, _______,                        _______, _______, _______, _______, _______, _______,\
                                            KC.LGUI,   LOWER,  ADJUST,     KC.ENT,   RAISE,  KC.RALT,
    ],
    [  #FUNC
        _______,  _______,  _______,  _______, _______, _______,                        _______, _______, _______, _______, _______, _______,\
        _______,  _______,  _______,  _______, _______, _______,                        _______, _______, _______, _______, _______, _______,\
        _______, _______, _______, _______, _______, _______,                        _______, _______, _______, _______, _______, _______,\
                                            KC.LGUI,   LOWER,  ADJUST,     KC.ENT,   RAISE,  KC.RALT,
    ],
    [  #CUST
        _______,  _______,  _______,  _______, _______, _______,                        _______, _______, _______, _______, _______, _______,\
        _______,  _______,  _______,  _______, _______, _______,                        _______, _______, _______, _______, _______, _______,\
        _______, _______, _______, _______, _______, _______,                        _______, _______, _______, _______, _______, _______,\
                                            KC.LGUI,   LOWER,  ADJUST,     KC.ENT,   RAISE,  KC.RALT,
    ],
    [  #PASS
        _______,  _______,  _______,  _______, _______, _______,                        _______, _______, _______, _______, _______, _______,\
        _______,  _______,  _______,  _______, _______, _______,                        _______, _______, _______, _______, _______, _______,\
        _______, _______, _______, _______, _______, _______,                        _______, _______, _______, _______, _______, _______,\
                                            KC.LGUI,   LOWER,  ADJUST,     KC.ENT,   RAISE,  KC.RALT,
    ]
]

if __name__ == '__main__':
    keyboard.go()
