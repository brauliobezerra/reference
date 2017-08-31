#!/usr/bin/env python

import re


def files_from_summary_md():
    files_to_search = []
    pattern = re.compile('\\[([^\\]]+)\\]\\(([^(]+)\\)')
    for line in open('src/SUMMARY.md', 'r'):
        for match in re.finditer(pattern, line):
            files_to_search.append(dict(
                title=match.group(1),
                path='src/' + match.group(2)))

    files_to_search.remove(dict(title='Appendix: Grammar', path='src/grammar.md'))

    return files_to_search


def extract_snippets(files_to_search):
    LEXER_HEADER_MARK = '> **<sup>Lexer'
    GRAMMAR_HEADER_MARK = '> **<sup>Syntax'

    lexer_content = ''
    grammar_content = ''

    for file in files_to_search:
        currently_lexer = False
        currently_grammar = False
        lex_in_this_file = ''
        gram_in_this_file = ''

        for line in open(file['path'], 'r'):
            if currently_lexer:
                if line.startswith('>'):
                    lex_in_this_file += line
                else:
                    lex_in_this_file += '>  \n'
                    currently_lexer = False
            elif currently_grammar:
                if line.startswith('>'):
                    gram_in_this_file += line
                else:
                    gram_in_this_file += '>  \n'
                    currently_grammar = False
            else:
                if line.startswith(LEXER_HEADER_MARK):
                    currently_lexer = True
                    currently_grammar = False
                elif line.startswith(GRAMMAR_HEADER_MARK):
                    currently_lexer = False
                    currently_grammar = True

        if len(lex_in_this_file) > 0:
            lexer_content += "\n### {}\n\n".format(file['title'])
            lexer_content += lex_in_this_file

        if len(gram_in_this_file) > 0:
            grammar_content += "\n### {}\n\n".format(file['title'])
            grammar_content += gram_in_this_file

    return lexer_content, grammar_content


def write_to_grammar_md(lexer_content, grammar_content):
    with open('src/grammar.md', 'w') as grammar_md:
        grammar_md.write("""\
# Grammar

## Lexical productions

{}

## Syntactical productions

{}

        """.format(lexer_content, grammar_content).strip())

files = files_from_summary_md()
lexer, grammar = extract_snippets(files)
write_to_grammar_md(lexer, grammar)
