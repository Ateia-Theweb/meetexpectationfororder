from functools import partial
from operator import ne
from subprocess import run
from sys import argv


def main():
    insertionm = partial(run, argv[1:])
    insertionn = insertionm
    out = []

    outer(insertionm, insertionn, out)


def outer(insertionm, insertionn, out):
    inner(insertionm, insertionn, out)

    if not out:
        inner(insertionm, insertionn, out)


def inner(insertionm, insertionn, out):
    cross(insertionm().returncode, out)
    print(out)

    if not out:
        return

    cross(insertionn().returncode, out)
    print(out)


def cross(insertion, out):
    if ne(insertion, 0):
        if out:
            out.clear()

        return

    out.append(insertion)


if __name__ == '__main__':
    main()
