from pygments.lexer import RegexLexer
from pygments.token import *

class CustomLexer(RegexLexer):
    name = "sct"
    aliases = [ "sct" ]
    filenames = ['*.sct']
    mimetypes = ['text/sct']

    tokens = {
        'root': [
            (r'//[^\r\n]*', Comment.Single,),
            (r'[ \t\r\n]+', Whitespace,),
            
            (r'function', Keyword.Declaration,),
            (r'->', Punctuation,),
            (r'int', Keyword.Type),
            (r'float', Keyword.Type),
            (r'void', Keyword.Type),

            (r'=', Operator,),
            (r'if', Keyword.Reserved,),
            (r'else', Keyword.Reserved,),
            (r'while', Keyword.Reserved,),
            (r'return', Keyword.Reserved,),
            (r'enter', Keyword.Reserved,),
            (r'create', Keyword.Reserved,),
            (r'destroy', Keyword.Reserved,),
            (r'exit', Keyword.Reserved,),
            (r'continue', Keyword.Reserved,),
            (r'break', Keyword.Reserved,),

            
            (r'\*', Operator,),
            (r'/', Operator,),
            (r'\+', Operator,),
            (r'-', Operator,),
            (r'%', Operator,),
            (r'&&', Operator,),
            (r'\|\|', Operator,),
            (r'==', Operator,),
            (r'!=', Operator,),
            (r'>', Operator,),
            (r'<', Operator,),
            (r'>=', Operator,),
            (r'<=', Operator,),
            (r'!', Operator,),

            (r'class', Keyword.Declaration,),
            (r'state', Keyword.Declaration,),
            (r'decorator', Keyword.Declaration,),
            (r'@', Punctuation,),


            (r'\?', Name.Builtin,),
            (r'\(', Punctuation,),
            (r'\)', Punctuation,),
            (r'{', Punctuation,),
            (r'}', Punctuation,),
            (r';', Punctuation,),
            (r',', Punctuation,),
            (r'::', Punctuation,),
            (r':', Punctuation,),

            (r'[a-zA-Z_][a-zA-Z_0-9]*', Name.Variable,),
            (r'[0-9]+.[0-9]+', Number.Float,),
            (r'[0-9]+', Number.Integer,),
        ]
    }
