# Notation

## Unicode productions

A few productions in Rust's grammar permit Unicode code points outside the
ASCII range. We define these productions in terms of character properties
specified in the Unicode standard, rather than in terms of ASCII-range code
points. The grammar has a [Special Unicode Productions][unicodeproductions]
section that lists these productions.

[unicodeproductions]: ../grammar.html#special-unicode-productions

## Grammar

The following notations are used by the *Lexer* and *Syntax* grammar snippets:

| Notation      | Examples                      | Meaning                              |
|---------------|-------------------------------|--------------------------------------|
| CAPITAL       | KW_IF, INTEGER_LITERAL        | A token produced by the lexer        |
| _CamelCase_   | _LetExpression_, _Item_       | A syntactical production             |
| `string`      | `x`, `while`, `*`             | The exact character(s)               |
| <sup>?</sup>  | `pub`<sup>?</sup>             | An optional item                     |
| <sup>\*</sup> | _OuterAttribute_<sup>\*</sup> | 0 or more or it                      |
| <sup>+</sup>  | XID_Continue<sup>+</sup>      | 1 or more of it                      |
| \|            | `u8` \| `u16`                 | Either one or another                |
| [ ]           | [`b` `B`]                     | Any of the characters listed         |
| [ - ]         | [`a`-`z`]                     | Any of the characters in the range   |
| ~[ ]          | ~[`a`-`z`]                    | Any characters, except those listed  |
| ~`string`     | ~`\n`, ~`*/`                  | Any characters, except this sequence |
| ( )           | (`,` _Parameter_)<sup>?</sup> | Groups items                         |

### Simple tokens in syntactical rules

For ease of reading, syntactical rules in the grammar show the printable
characters of the simple tokens, instead of the names defined by the
lexer. For example, we use `while` instead of KW_WHILE and `{` instead
of OPEN_BRACE.
