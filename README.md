# Pygments SCT Lexer

## Prerequisites

- Python
- LaTeX

## Install

```sh
virtualenv venv
source ./venv/bin/activate
pip install Pygments

wget https://raw.githubusercontent.com/DATP4G6/sct-pygments/main/lexer.py
```


## Use

See [main.tex](./main.tex)

```tex
\documentclass{minimal}
\usepackage[cache=false]{minted}

\begin{document}
\begin{minted}{'lexer.py -x'}
class Foo(int x) {
    decorator Bar {
        x = x - 1;
    }

    @Bar
    state Baz {
        if (exists(Foo::?(x: 3))) {
            destroy;
        }
        enter Baz;
    }
}

function Setup() -> void {
    create Foo::Baz(x: 5);
}
\end{minted}
\end{document}
```

This, will generate a .pdf like the one shown in [main.pdf](./main.pdf)
