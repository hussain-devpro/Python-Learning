import sys
from math import log

DIGIT_MAP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def convert(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        return int(number)
    # except KeyError:
    #     print('Conversation Failed!')
    #     x = -1  # should not return error code like this. Explanation is available in my_ex_main.py
    # except TypeError:
    #     print('Conversation Failed!')
    #     x = -2
    except (KeyError, TypeError) as e:  # Both exception can be handled together, and x can be declared outside
        print(f'Conversation Error: {e!r}', file=sys.stderr)  # !r is the repr representation of object or expression
        raise  # re-raise the exception


def string_log(s):
    v = convert(s)
    return log(v)


def main(string_list):
    convert(string_list)


if __name__ == '__main__':
    main(sys.argv[1])  # The 0th arg is the module filename
