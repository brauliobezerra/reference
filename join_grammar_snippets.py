import re


def files_from_summary_md():
    files_to_search = []
    pattern = re.compile('[-a-zA-Z/]+\\.md')
    for line in open('src/SUMMARY.md', 'r'):
        for match in re.findall(pattern, line):
            files_to_search.append('src/' + match)

    files_to_search.remove('src/grammar.md')

    return files_to_search


def extract_snippets(files_to_search):
    LEXER_HEADER_MARK = '> **<sup>Lexer'
    GRAMMAR_HEADER_MARK = '> **<sup>Syntax'

    lexer_contents = ''
    grammar_contents = ''

    for file in files_to_search:
        currently_lexer = False
        currently_grammar = False
        lex_in_this_file = ''
        gram_in_this_file = ''

        print('Analyzing ' + file + '...')

        for line in open(file, 'r'):
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
            lexer_contents += "\n### {}\n\n".format(file)
            lexer_contents += lex_in_this_file

        if len(gram_in_this_file) > 0:
            grammar_contents += "\n### {}\n\n".format(file)
            grammar_contents += gram_in_this_file

    return lexer_contents, grammar_contents


def write_to_grammar_md(lexer_contents, grammar_contents):
    with open('src/grammar.md', 'w') as grammar_md:
        grammar_md.write("""\
# Grammar

## Lexical productions

{}

## Syntactical productions

{}

        """.format(lexer_contents, grammar_contents).strip())

files = files_from_summary_md()
lexer, grammar = extract_snippets(files)
write_to_grammar_md(lexer, grammar)
