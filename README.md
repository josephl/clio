Simplio
====

Simplest-case command-line input/output.

This is a Python function decorator that applies an input file object and an
output file object as arguments to the decorated function. It determines this
based on STDIN or the presence of command-line arguments.

Simplio was created when I grew tired of writing I/O boilerplate code for simple
data cleaning scripts in Python and felt that the excellent
[argparse](https://docs.python.org/3/library/argparse.html) library was
overkill.

### Input
If `STDIN` is not a TTY, it assumes input has been piped in.
Otherwise, the first argument is the path to the file to be used as input.

### Output
If a path argument to an output file is specified (as either the first argument
if `INPUT` is `STDIN` or the second argument if a path to the input file is
specified), then the output file is set to the path.
Otherwise, output is set to `STDOUT`.

### Examples
`script.py:`
```python
from simplio import simplio


@simplio
def main(filein, fileout):
    """Trivially write input to output."""
    fileout.write(filein.read())


if __name__ == '__main__':
    main()
```

Input: `STDIN`, Output: `STDOUT`
```
$ echo 'foo' | python script.py
foo
```

`foo.txt:`
```
FOO,
Foo,
foo.
```

Input: `foo.txt`, Output: `STDOUT`
```
$ python script.py foo.py
FOO,
Foo,
foo.
```

Input: `STDIN`, Output: `bar.txt`
```
$ python script.py bar.txt < foo.txt
$ cat bar.txt
FOO,
Foo,
foo.
```

Input: `foo.txt`, Output: `bar.txt`
```
$ python script.py foo.txt bar.txt
$ cat bar.txt
FOO,
Foo,
foo.
```
