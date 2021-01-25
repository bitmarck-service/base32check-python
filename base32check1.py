#!/usr/bin/env python3
#
# Copyright © 2021 BITMARCK Service GmbH
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
def validate(payload):
    return compute(payload) == 'A'


def compute(payload):
    return _compute(payload.replace(' ', '').upper())


def _compute(payload):
    len_payload = len(payload)
    sum = 0
    for i in range(len_payload):
        sum ^= _mat_mul((_INDEX[payload[i]],), _PRIMITIVE_POWERS[(i + 1) % (_CARDINAL - 1)])[0]
    exp = (_CARDINAL - len_payload - 2) % (_CARDINAL - 1)
    if exp < 0:
        exp += _CARDINAL - 1
    return _ALPHABET[_mat_mul((sum,), _PRIMITIVE_POWERS[exp])[0]]


def _primitive_powers(primitive):
    mat = [[], primitive]
    for i in range(2, _CARDINAL):
        values = _mat_mul(mat[i - 1], primitive)
        if i < _CARDINAL - 1:
            mat.append(values)
        else:
            mat[0] = values
    return tuple(mat)


def _mat_mul(a, b):
    mat = []
    for i in range(len(a)):
        mat.append(0)
        len_b = len(b)
        for j in range(len_b):
            if a[i] & (1 << (len_b - 1 - j)):
                mat[i] ^= b[j]
    return tuple(mat)


_CARDINAL = 1 << 5
_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
_INDEX = dict(zip(_ALPHABET, range(len(_ALPHABET))))
_PRIMITIVE_POWERS = _primitive_powers((0x01, 0x11, 0x08, 0x05, 0x03))

if __name__ == '__main__':
    from sys import _getframe

    line = _getframe().f_lineno + 2
    tests = (
        'A',
        'AA',
        'ABQ',
        'ABCj',
        'ABCDV',
        'ABCDEI',
        'ABCDEFG',
        'ABCDEFGA',
        'ABCDEFGHT',
        'ABCDEFGHI5',
        'ABCDEFGHIJK',
        'ABCDEFGHIJKA',
        'ABCDEFGHIJKLF',
        'ABCDEFGHIJKLMU',
        'ABCDEFGHIJKLMNM',
        'ABCDEFGHIJKLMNOR',
        'ABCDEFGHIJKLMNOP7',
        'ABCDEFGHIJKLMNOPQX',
        'ABCDEFGHIJKLMNOPQRD',
        'ABCDEFGHIJKLMNOPQRSI',
        'ABCDEFGHIJKLMNOPQRST5',
        'ABCDEFGHIJKLMNOPQRSTUU',
        'ABCDEFGHIJKLMNOPQRSTUVQ',
        'ABCDEFGHIJKLMNOPQRSTUVWD',
        'ABCDEFGHIJKLMNOPQRSTUVWXK',
        'ABCDEFGHIJKLMNOPQRSTUVWXYJ',
        'ABCDEFGHIJKLMNOPQRSTUVWXYZY',
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ2R',
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ23V',
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ234U',
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ2345U',
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ23456V',
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567V',
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567ABCDEFGHIJKLMNOPQRSTUVWXYZ23456',
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567ABCDEFGHIJKLMNOPQRSTUVWXYZ234567ABCDEFGHIJKLMNOPQRSTUVWXYZ234K',
        'CONSECRATIOX',
        'CAFEBABEN',
        'CAFEDEADA',
        'DEADBEEFL',
        '234567Z',
        'BLAB LABL ABLA BLA3',
        'BLAF ASEL GEDO ENSU',
    )
    for i, test in zip(range(len(tests)), tests):
        assert validate(test), f'File "{__file__}", line {line + i}: Invalid Base32check1 string: "{test}"'
