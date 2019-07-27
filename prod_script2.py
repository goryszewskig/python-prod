"""Simple fizzbuzz generator.

The game proceeds with players announcing numbers increasing
sequentially, except for multiples of 3 and 5:

    >>> usage = 'fizzbuzz 1 20'

    >>> from io import StringIO; stdout = StringIO()
    >>> main(usage.split(), stdout)
    >>> print(stdout.getvalue())
    ... #doctest: +ELLIPSIS
    1
    2
    fizz
    4
    buzz
    fizz
    7
    ...
    14
    fizzbuzz
    16
    ...

"""
def main(argv, stdout):
    [lo_, hi_] = argv[1:3]
    lo, hi = int(lo_), int(hi_)

    for word in fizzbuzz(lo, hi):
        print(word, file=stdout)

def fizzbuzz(lo, hi):
    """
    >>> list(fizzbuzz(1, 6))
    [1, 2, 'fizz', 'buzz']
    """
    for n in range(lo, hi):
        if n % 3 == 0 and n % 5 == 0:
            yield 'fizbuzz'
        elif n % 3 == 0:
            yield 'fizz'
        elif n % 5 == 0:
            yield 'buzz'
        else:
            yield n

if __name__ == '__main__':
    def _script_io():
        from sys import argv, stdout

        main(argv, stdout)
    _script_io()



