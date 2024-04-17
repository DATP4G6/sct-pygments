# Pygments SCT Lexer

## Prerequisites

- Python
- LaTeX

## Install

```sh
virtualenv venv
source ./venv/bin/activate
pip install Pygments

wget https://raw.githubusercontent.com/DATP4G6/sct-pygments/main/SctLexer.py
```


## Use

See [example.tex](./example.tex)

```tex
\begin{minted}{'SctLexer.py -x'}
// your code here...
\end{minted}
```

This, will generate a .pdf like the one shown in [example.pdf](./example.pdf)
