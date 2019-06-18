import ply.lex as lex


class MyLexer(object):
    tokens = (
        'INT',
        'FLOAT',
        'ADD',
        'SUB',
        'DIV',
        'MUL',
        'POWER',
        'LEFTPAR',
        'RIGHTPAR'
    )

    t_ignore = ' '

    t_ADD = r'\+'
    t_SUB = r'\-'
    t_MUL = r'\*'
    t_DIV = r'\/'
    t_POWER = r'p'
    t_LEFTPAR = r'\('
    t_RIGHTPAR = r'\)'

    def t_FLOAT(self, t):
        r'\d+\.\d+'
        t.value = float(t.value)
        return t

    def t_INT(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_error(self, t):
        print("illegal char:", t.value[0])
        t.lexer.skip(1)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def test(self, data):
        self.lexer.input(data)
        for tok in self.lexer:
            print(tok)
