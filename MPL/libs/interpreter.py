# -*- coding: utf-8 -*-

import sys


class InvalidTokenException(BaseException):
    pass


class CursorUnderflowException(BaseException):
    pass


class Brainfuck(object):
    INITIAL_SIZE = 10000
    DELTA = 1000

    INCREMENT = 'yeah!'
    DECREMENT = 'f**k!'
    INCREMENT_POINTER = 'ah,'
    DECREMENT_POINTER = 'oh,'
    WRITE = 'come_on!'
    READ = 'mm...'
    LOOP_START = 'oh_my_god!'
    LOOP_END = 'god!'

    def __init__(self):
        self._token_mappings = {
            self.INCREMENT: self._increment,
            self.DECREMENT: self._decrement,
            self.INCREMENT_POINTER: self._increment_pointer,
            self.DECREMENT_POINTER: self._decrement_pointer,
            self.WRITE: self._write,
            self.READ: self._read,
            self.LOOP_START: self._loop_start,
            self.LOOP_END: self._loop_end,
        }
        self._brace_mappings = {}
        self._pointer = 0
        self._cells = [0] * self.INITIAL_SIZE
        self.output = []

    # >
    def _increment(self, _cursor):
        self._pointer += 1
        if len(self._cells) < self._pointer:
            self._cells += [0] * self.DELTA

    # <
    def _decrement(self, _cursor):
        self._pointer -= 1
        if self._pointer < 0:
            msg = 'ポインタは負の値を取れません'
            raise CursorUnderflowException(msg)

    # +
    def _increment_pointer(self, _cursor):
        self._cells[self._pointer] += 1

    # -
    def _decrement_pointer(self, _cursor):
        self._cells[self._pointer] -= 1

    # .
    def _write(self, _cursor):
        c = chr(self._cells[self._pointer])
        # print(c, end='')
        self.output.append(c)

    # ,
    def _read(self, _cursor):
        d = ord(sys.stdin.read(1))
        self._cells[self._pointer] = d

    # [
    def _loop_start(self, cursor):
        if self._cells[self._pointer] != 0:
            return
        pair_brace_position = self._brace_mappings[cursor]
        return pair_brace_position

    # ]
    def _loop_end(self, cursor):
        if self._cells[self._pointer] == 0:
            return
        pair_brace_position = self._brace_mappings[cursor]
        return pair_brace_position

    def evaluate(self, code):
        self._initialize_brace_mappings(code)
        cursor = 0
        end = len(code)

        while cursor < end:
            c = code[cursor]
            command = self._token_mappings.get(c)
            if command is None:
                msg = '不正な命令が含まれます: {token}'.format(token=c)
                raise InvalidTokenException(msg)
            index = command(cursor)
            cursor = index if index is not None else cursor + 1


        return ''.join(self.output)

    def _initialize_brace_mappings(self, code):
        start_brace_positions = []
        for i, token in enumerate(code):
            if token not in [self.LOOP_START, self.LOOP_END]:
                # '[' と ']' 以外は無視する
                continue
            if token == self.LOOP_START:
                # '[' のあった位置をスタックにプッシュする
                start_brace_positions.append(i)
            else:
                # 直近の ']' の場所をスタックから取り出す
                start_brace_position = start_brace_positions.pop()
                # 上記の ']' に対応する '[' の場所
                end_brace_position = i
                # ']' の場所から対応する '[' の場所を引けるようにする
                self._brace_mappings[start_brace_position] = end_brace_position
                # 反対方向も
                self._brace_mappings[end_brace_position] = start_brace_position


def main():
    code = 'ah, ah, ah, ah, ah, ah, ah, ah, ah, oh_my_god! yeah! ah, ah, ah, ah, ah,\
    ah, ah, ah, yeah! ah, ah, ah, ah, ah, ah, ah, ah, ah, ah, ah, yeah! ah,\
    ah, ah, ah, ah, f**k! f**k! f**k! oh, god! yeah! come_on! yeah! ah, ah,\
    come_on! ah, ah, ah, ah, ah, ah, ah, come_on! come_on! ah, ah, ah, come_on!\
    yeah! oh, come_on! oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, oh, come_on!\
    f**k! ah, ah, ah, ah, ah, ah, ah, ah, come_on! oh, oh, oh, oh, oh, oh, oh,\
    oh, come_on! ah, ah, ah, come_on! oh, oh, oh, oh, oh, oh, come_on! oh, oh, oh,\
    oh, oh, oh, oh, oh, come_on! yeah! ah, come_on!'.split()

    # code = ['ah,','ah,','ah,','ah,','ah,','ah,','ah,','ah,','ah,','oh_my_god!','yeah!','ah,','ah,','ah,','ah,','ah,',
    #         'ah,','ah,','ah,','yeah!','ah,','ah,','ah,','ah,','ah,','ah,','ah,','ah,','ah,','ah,','ah,','yeah!','ah,',
    #         'ah,','ah,','ah,','ah,','f**k!','f**k!','f**k!','oh,','god!','yeah!','come_on!','yeah!','ah,','ah,',
    #         'come_on!','ah,','ah,','ah,','ah,','ah,','ah,','ah,','come_on!','come_on!','ah,','ah,','ah,','come_on!',
    #         'yeah!','oh,','come_on!','oh,','oh,','oh,','oh,','oh,','oh,','oh,','oh,','oh,','oh,','oh,','oh,','come_on!',
    #         'f**k!','ah,','ah,','ah,','ah,','ah,','ah,','ah,','ah,','come_on!','oh,','oh,','oh,','oh,','oh,','oh,','oh,',
    #         'oh,','come_on!','ah,','ah,','ah,','come_on!','oh,','oh,','oh,','oh,','oh,','oh,','come_on!','oh,','oh,','oh,',
    #         'oh,','oh,','oh,','oh,','oh,','come_on!','yeah!','ah,','come_on!']
    interpreter = Brainfuck()
    try:
        print(interpreter.evaluate(code))
    except InvalidTokenException as e:
        print(e, file=sys.stderr)
    except CursorUnderflowException as e:
        print(e, file=sys.stderr)


if __name__ == '__main__':
    main()
