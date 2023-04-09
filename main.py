from kb import KMKKeyboard

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
modtap = ModTap()
# TODO: write oled extension
# TODO: write wpm module

# add to keyboard
keyboard.modules = [layers_ext, split, modtap]

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
NUMB = KC.MO(1)
SYMB = KC.MO(2)
NAV_M = KC.MO(3)
NAV_W = KC.MO(4)
FUNC = KC.MO(5)
CUST = KC.MO(6)
PASS = KC.MO(7)

# password
PWRD = send_string(PASSWORD)
UPS = simple_key_sequence(USER_PASS_SEQ)

# Homerow modtap
F_GUI = KC.MT(KC.F, KC.LGUI, tap_interrupted=False, prefer_hold=False)
D_ALT = KC.MT(KC.D, KC.LALT, tap_interrupted=False, prefer_hold=False)
S_CTL = KC.MT(KC.S, KC.LCTRL, tap_interrupted=False, prefer_hold=False)
J_GUI = KC.MT(KC.J, KC.RGUI, tap_interrupted=False, prefer_hold=False)
K_ALT = KC.MT(KC.K, KC.RALT, tap_interrupted=False, prefer_hold=False)
L_CTL = KC.MT(KC.L, KC.RCTRL, tap_interrupted=False, prefer_hold=False)

# Combo modifiers
CAT = KC.LALT(KC.TAB)
CATH = KC.LCA(KC.TAB)
CSE = KC.LCS(KC.ESC)
CAD = KC.LCA(KC.DEL)

############## CAPS WORDS ####################

# Configuration constants
IGNORE_CAPS_WORD_KEYS = [F_GUI,D_ALT,S_CTL,J_GUI,K_ALT,L_CTL]

caps_word=CapsWord()

caps_word.keys_ignored = IGNORE_CAPS_WORD_KEYS
keyboard.modules.append(caps_word)

############## KEYMAP ########################

# TODO: get keymap from other keyboard
keyboard.keymap = [
    [  #QWERTY
        KC.ESC,    KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                         KC.Y,    KC.U,    KC.I,    KC.O,   KC.P,  KC.GRV,\
        KC.TAB,    KC.A,   S_CTL,    D_ALT,  F_GUI,    KC.G,                         KC.H,   J_GUI,   K_ALT,   L_CTL, KC.SCLN, KC.ENT,\
        KC.CW,     KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,                         KC.N,    KC.M, KC.COMM,  KC.DOT, KC.SLSH, KC.BSLS,\
                                             NAV_M,    SYMB,  KC.LSFT,   KC.BSPC,  KC.SPC,    NUMB,
    ],
    [  #NUM
        _______,   KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,                         KC.N6,     KC.N7,   KC.N8,   KC.N9,   KC.N0, _______,\
        _______, _______, KC.LCTL, KC.LALT, KC.LGUI, _______,                        _______, KC.RGUI, KC.RALT,KC.RCTRL, _______, _______,\
        _______, _______, _______, _______, _______, _______,                        _______, _______, _______, KC.COMM, _______, _______,\
                                               FUNC,    CUST,  KC.LSFT,   _______,   _______, NUMB,
    ],
    [  #SYMB
        KC.ESC, KC.EXLM,   KC.AT, KC.HASH,  KC.DLR, KC.PERC,                         KC.MINS, KC.LCBR, KC.RCBR, _______, _______, KC.PIPE,\
        KC.LCTL, _______, _______,KC.AMPR, KC.CIRC, KC.ASTR,                         KC.EQL,  KC.LPRN, KC.RPRN, KC.UNDS, KC.DQUO,  KC.QUOT,\
        KC.LSFT, _______, _______, _______, _______, _______,                        KC.PLUS, KC.LBRC, KC.RBRC, _______, KC.QUES, _______,\
                                            _______,   SYMB,  _______,     KC.DEL,   _______,    CUST,
    ],
    [  #NAV_M (mac navigation)
        _______,   KC.F1,    KC.F2,  KC.F3,   KC.F4,   KC.F5,                     KC.F6,     KC.F7,   KC.F8,    KC.F9,  KC.F10,     CAD,\
        _______, KC.LSFT,  KC.LCTL,KC.LALT, KC.LGUI, _______,                     KC.LEFT, KC.DOWN,   KC.UP, KC.RIGHT, _______,     CSE,\
        _______, _______, _______, _______, _______, _______,                     KC.HOME, KC.PGDN, KC.PGUP,   KC.END, _______, _______,\
                                            NAV_M,   _______,  _______,      CAT,    CATH,    CUST,
    ]
    ,
    [  #NAV_W (windows navigation) TODO
        _______,  _______,  _______,  _______, _______, _______,                        _______, _______, _______, _______, _______, _______,\
        _______,  _______,  _______,  _______, _______, _______,                        _______, _______, _______, _______, _______, _______,\
        _______, _______, _______, _______, _______, _______,                        _______, _______, _______, _______, _______, _______,\
                                              NAV_M, _______,  _______,  _______, _______,    CUST,
    ],
    [  #FUNC
        _______,   KC.F1,    KC.F2,  KC.F3,   KC.F4,   KC.F5,                          KC.F6,   KC.F7,   KC.F8,   KC.F9,  KC.F10,  KC.F11,\
        _______, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI, _______,                        _______, KC.RGUI, KC.RALT,KC.RCTRL, KC.RSFT, _______,\
        _______, _______, _______, _______, _______, _______,                        _______, _______, _______, _______, _______, _______,\
                                               FUNC, _______,  _______,  _______,    _______,    FUNC,
    ],
    [  #CUST
        _______, _______,  _______,  _______, _______, _______,                        _______, _______, _______, _______, _______, _______,\
        _______,    PASS,  _______,  _______, _______, _______,                        _______, _______, _______, _______, _______, _______,\
        _______, _______,  _______,  _______, _______, _______,                        _______, _______, _______, _______, _______, _______,\
                                              _______,    CUST,  _______,  _______,    _______,  CUST,
    ],
    [  #PASS
        _______,  _______,  _______,  _______, _______, _______,                        _______, _______, _______, _______, _______, _______,\
        _______,  _______,  _______,     PWRD,     UPS, _______,                        _______, _______, _______, _______, _______, _______,\
        _______, _______, _______, _______, _______, _______,                        _______, _______, _______, _______, _______, _______,\
                                              _______,    CUST,  _______,  _______,    _______,  CUST,
    ]
]

if __name__ == '__main__':
    keyboard.go()
