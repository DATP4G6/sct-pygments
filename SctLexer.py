from pygments.lexer import RegexLexer, bygroups
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
            
            (r'int', Keyword.Type),
            (r'float', Keyword.Type),
            (r'void', Keyword.Type),
            (r'Predicate', Keyword.Type),

            (r'if', Keyword.Reserved,),
            (r'else', Keyword.Reserved,),
            (r'while', Keyword.Reserved,),
            (r'return', Keyword.Reserved,),
            (r'create', Keyword.Reserved,),
            (r'destroy', Keyword.Reserved,),
            (r'exit', Keyword.Reserved,),
            (r'continue', Keyword.Reserved,),
            (r'break', Keyword.Reserved,),
            
            (r'=', Operator,),
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

            (r'(species)(\s+)(\w+)', bygroups(Keyword.Declaration, Token.Text.Whitespace, Name.Constant),),

            # predicates
            (r'(\w+)(::)(\w+)', bygroups(Name.Constant, Punctuation, Name.Label),),
            (r'(\w+)(::)(\?)', bygroups(Name.Constant, Punctuation, Keyword.Pseudo),),

            (r'(state)(\s+)(\w+)', bygroups(Keyword.Declaration, Token.Text.Whitespace, Name.Label)),
            (r'(enter)(\s+)(\w+)', bygroups(Keyword.Reserved, Token.Text.Whitespace, Name.Label)),

            (r'(decorator)(\s+)(\w+)', bygroups(Keyword.Declaration, Token.Text.Whitespace, Name.Decorator)),
            (r'@\w+', Name.Decorator,),

            (r'(function)(\s+)(\w+)', bygroups(Keyword.Declaration,Token.Text.Whitespace, Name.Function),),
            (r'(?<!::)\w+(?=\()', Name.Function,), # invoke function

            (r'->', Punctuation,),
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
