#         FUNÇÕES parte 2          #

"""
AJUDA INTERATIVA
→ help()
Abrir o Python Console, na parte de baixo do Pycharm, e digitar o comando help().
Depois digitar os comandos:

    - print
            print(*args, sep=' ', end='\n', file=None, flush=False)
        Prints the values to a stream, or to sys.stdout by default.

        sep
          string inserted between values, default a space.
        end
          string appended after the last value, default a newline.
        file
          a file-like object (stream); defaults to the current sys.stdout.
        flush
          whether to forcibly flush the stream.

    - input
            input(prompt=None, /)
        Read a string from standard input.  The trailing newline is stripped.

        The prompt string, if given, is printed to standard output without a
        trailing newline before reading input.

        If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
        On *nix systems, readline is used if available.

* Se não souber o que uma função faz:
    help(função)
ex:help(print)
"""

"""
DOCSTRINGS

"""


def contador(i, f, p):
    """
        → Faz uma contagem e mostra na tela.
        → i == início da contagem
        → f == fim da contagem
        → p == passo da contagem
        → return == sem retorno
        """
    c = i
    while c <= f:
        print(f'{c} ', end=' ')
        c += p
    print('FIM')


def somar(a=0, b=0, c=0, d=0):
    s = a + b + c + d
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)
somar(1, 0, 0, 3)
somar()


"""
# escopo local
def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


# escopo global
n = 2
print(f'No programa principal, n vale {n}')
print(f'No programa principal, x vale {x}')
"""