# Notation

## Unicode productions

A few productions in Rust's grammar permit Unicode code points outside the
ASCII range. We define these productions in terms of character properties
specified in the Unicode standard, rather than in terms of ASCII-range code
points. The grammar has a [Special Unicode Productions] section that lists these
productions.

## String table productions

Some rules in the grammar &mdash; notably [unary operators], [binary
operators], and [keywords] &mdash; are given in a simplified form: as a listing
of printable strings. These cases form a subset of the rules regarding the
[token][tokens] rule, and are assumed to be the result of a lexical-analysis
phase feeding the parser, driven by a <abbr title="Deterministic Finite
Automaton">DFA</abbr>, operating over the disjunction of all such string table
entries.

When such a string in `monospace` font occurs inside the grammar,
it is an implicit reference to a single member of such a string table
production. See [tokens] for more information.

## Grammar

The following notations are used by the *Lexer* and *Syntax* grammar snippets:

| Notation      | Examples                      | Meaning                                   |
|---------------|-------------------------------|-------------------------------------------|
| CAPITAL       | KW_IF, INTEGER_LITERAL        | A token produced by the lexer             |
| _CamelCase_   | _LetExpression_, _Item_       | A syntactical production                  |
| `string`      | `x`, `while`, `*`             | The exact character(s)                    |
| \\x           | \\n, \\r, \\t                 | The character represented by this escape  |
| <sup>?</sup>  | `pub`<sup>?</sup>             | An optional item                          |
| <sup>\*</sup> | _OuterAttribute_<sup>\*</sup> | 0 or more or it                           |
| <sup>+</sup>  | XID_Continue<sup>+</sup>      | 1 or more of it                           |
| \|            | `u8` \| `u16`                 | Either one or another                     |
| [ ]           | [`b` `B`]                     | Any of the characters listed              |
| [ - ]         | [`a`-`z`]                     | Any of the characters in the range        |
| ~[ ]          | ~[`a`-`z`]                    | Any characters, except those listed       |
| ~`string`     | ~`\n`, ~`*/`                  | Any characters, except this sequence      |
| ( )           | (`,` _Parameter_)<sup>?</sup> | Groups items                              |

[Special Unicode Productions]: ../grammar.html#special-unicode-productions
[binary operators]: expressions/operator-expr.html#arithmetic-and-logical-binary-operators
[keywords]: keywords.html
[tokens]: tokens.html
[unary operators]: expressions/operator-expr.html#borrow-operators
