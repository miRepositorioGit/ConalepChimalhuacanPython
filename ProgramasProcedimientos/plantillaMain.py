"""plantillaMain.py
Descripción.


Referencia.
__main__ — Top-level code environment.
    file:///C:/Users//AppData/Local/Programs/Python/Python311/Doc/html/library/__main__.html?highlight=__main__#module-__main__
    
"""
import shlex
import sys

def echo(phrase: str) -> None:
   """A dummy wrapper around print."""
   # for demonstration purposes, you can imagine that there is some
   # valuable and reusable logic inside this function
   print(phrase)

def main() -> int:
    """Echo the input arguments to standard output"""
    phrase = shlex.join(sys.argv)
    echo(phrase)
    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
