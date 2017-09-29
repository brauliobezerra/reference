# Grammar

<!--
    WARNING: this file is generated automatically. It joins all
    **lexer** and **syntax** blocks of the Reference.  If you want to edit
    the grammar, apply your changes to each corresponding section and
    call the join script to update this file.
-->

## Lexical productions


### Keywords

> [KW_AS] :<a name="kw_as"></a> `as`  
> [KW_BOX] :<a name="kw_box"></a> `box`  
> [KW_BREAK] :<a name="kw_break"></a> `break`  
> [KW_CONST] :<a name="kw_const"></a> `const`  
> [KW_CONTINUE] :<a name="kw_continue"></a> `continue`  
> [KW_CRATE] :<a name="kw_crate"></a> `crate`  
> [KW_ELSE] :<a name="kw_else"></a> `else`  
> [KW_ENUM] :<a name="kw_enum"></a> `enum`  
> [KW_EXTERN] :<a name="kw_extern"></a> `extern`  
> [KW_FALSE] :<a name="kw_false"></a> `false`  
> [KW_FN] :<a name="kw_fn"></a> `fn`  
> [KW_FOR] :<a name="kw_for"></a> `for`  
> [KW_IF] :<a name="kw_if"></a> `if`  
> [KW_IMPL] :<a name="kw_impl"></a> `impl`  
> [KW_IN] :<a name="kw_in"></a> `in`  
> [KW_LET] :<a name="kw_let"></a> `let`  
> [KW_LOOP] :<a name="kw_loop"></a> `loop`  
> [KW_MATCH] :<a name="kw_match"></a> `match`  
> [KW_MOD] :<a name="kw_mod"></a> `mod`  
> [KW_MOVE] :<a name="kw_move"></a> `move`  
> [KW_MUT] :<a name="kw_mut"></a> `mut`  
> [KW_PUB] :<a name="kw_pub"></a> `pub`  
> [KW_REF] :<a name="kw_ref"></a> `ref`  
> [KW_RETURN] :<a name="kw_return"></a> `return`  
> [KW_SELFVALUE] :<a name="kw_selfvalue"></a> `self`  
> [KW_SELFTYPE] :<a name="kw_selftype"></a> `Self`  
> [KW_STATIC] :<a name="kw_static"></a> `static`  
> [KW_STRUCT] :<a name="kw_struct"></a> `struct`  
> [KW_SUPER] :<a name="kw_super"></a> `super`  
> [KW_TRAIT] :<a name="kw_trait"></a> `trait`  
> [KW_TRUE] :<a name="kw_true"></a> `true`  
> [KW_TYPE] :<a name="kw_type"></a> `type`  
> [KW_UNSAFE] :<a name="kw_unsafe"></a> `unsafe`  
> [KW_USE] :<a name="kw_use"></a> `use`  
> [KW_WHERE] :<a name="kw_where"></a> `where`  
> [KW_WHILE] :<a name="kw_while"></a> `while`  
>  
> [KW_CATCH] :<a name="kw_catch"></a> `catch`  
> [KW_DEFAULT] :<a name="kw_default"></a> `default`  
> [KW_UNION] :<a name="kw_union"></a> `union`  
> [KW_STATICLIFETIME] :<a name="kw_staticlifetime"></a> `'static`  
>  
> [KW_ABSTRACT] :<a name="kw_abstract"></a> `abstract`  
> [KW_ALIGNOF] :<a name="kw_alignof"></a> `alignof`  
> [KW_BECOME] :<a name="kw_become"></a> `become`  
> [KW_DO] :<a name="kw_do"></a> `do`  
> [KW_FINAL] :<a name="kw_final"></a> `final`  
> [KW_MACRO] :<a name="kw_macro"></a> `macro`  
> [KW_OFFSETOF] :<a name="kw_offsetof"></a> `offsetof`  
> [KW_OVERRIDE] :<a name="kw_override"></a> `override`  
> [KW_PRIV] :<a name="kw_priv"></a> `priv`  
> [KW_PROC] :<a name="kw_proc"></a> `proc`  
> [KW_PURE] :<a name="kw_pure"></a> `pure`  
> [KW_SIZEOF] :<a name="kw_sizeof"></a> `sizeof`  
> [KW_TYPEOF] :<a name="kw_typeof"></a> `typeof`  
> [KW_UNSIZED] :<a name="kw_unsized"></a> `unsized`  
> [KW_VIRTUAL] :<a name="kw_virtual"></a> `virtual`  
> [KW_YIELD] :<a name="kw_yield"></a> `yield`  

### Identifiers

> [IDENTIFIER] :<a name="identifier"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; XID_start XID_continue<sup>\*</sup>  
> &nbsp;&nbsp; | `_` XID_continue<sup>+</sup>  
>  

### Comments

> [LINE_COMMENT] :<a name="line_comment"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; `//` (~[`/` `!`] | `//`) ~`\n`<sup>\*</sup>  
> &nbsp;&nbsp; | `//`
>  
> [BLOCK_COMMENT] :<a name="block_comment"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; `/*` (~[`*` `!`] | `**` | _BlockCommentOrDoc_)
>      (_BlockCommentOrDoc_ | ~`*/`)<sup>\*</sup> `*/`  
> &nbsp;&nbsp; | `/**/`  
> &nbsp;&nbsp; | `/***/`  
>  
> [INNER_LINE_DOC] :<a name="inner_line_doc"></a>  
> &nbsp;&nbsp; `//!` ~[`\n` _IsolatedCR_]<sup>\*</sup>  
>  
> [INNER_BLOCK_DOC] :<a name="inner_block_doc"></a>  
> &nbsp;&nbsp; `/*!` ( _BlockCommentOrDoc_ | ~[`*/` _IsolatedCR_] )<sup>\*</sup> `*/`  
>  
> [OUTER_LINE_DOC] :<a name="outer_line_doc"></a>  
> &nbsp;&nbsp; `///` (~`/` ~[`\n` _IsolatedCR_]<sup>\*</sup>)<sup>?</sup>  
>  
> [OUTER_BLOCK_DOC] :<a name="outer_block_doc"></a>  
> &nbsp;&nbsp; `/**` (~`*` | _BlockCommentOrDoc_ )
>              (_BlockCommentOrDoc_ | ~[`*/` _IsolatedCR_])<sup>\*</sup> `*/`  
>  
> [_BlockCommentOrDoc_] :<a name="blockcommentordoc"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; BLOCK_COMMENT  
> &nbsp;&nbsp; | OUTER_BLOCK_DOC  
> &nbsp;&nbsp; | INNER_BLOCK_DOC  
>  
> [_IsolatedCR_] :<a name="isolatedcr"></a>  
> &nbsp;&nbsp; _A `\r` not followed by a `\n`_  
>  

### Tokens

> [CHAR_LITERAL] :<a name="char_literal"></a>  
> &nbsp;&nbsp; `'` ( ~[`'` `\` \\n \\r \\t] | QUOTE_ESCAPE | ASCII_ESCAPE | UNICODE_ESCAPE ) `'`  
>  
> [QUOTE_ESCAPE] :<a name="quote_escape"></a>  
> &nbsp;&nbsp; `\'` | `\"`  
>  
> [ASCII_ESCAPE] :<a name="ascii_escape"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; `\x` OCT_DIGIT HEX_DIGIT  
> &nbsp;&nbsp; | `\n` | `\r` | `\t` | `\\` | `\0`  
>  
> [UNICODE_ESCAPE] :<a name="unicode_escape"></a>  
> &nbsp;&nbsp; `\u{` ( HEX_DIGIT `_`<sup>\*</sup> )<sup>1..6</sup> `}`  
>  
> [STRING_LITERAL] :<a name="string_literal"></a>  
> &nbsp;&nbsp; `"` (  
> &nbsp;&nbsp; &nbsp;&nbsp; ~[`"` `\` _IsolatedCR_]  
> &nbsp;&nbsp; &nbsp;&nbsp; | QUOTE_ESCAPE  
> &nbsp;&nbsp; &nbsp;&nbsp; | ASCII_ESCAPE  
> &nbsp;&nbsp; &nbsp;&nbsp; | UNICODE_ESCAPE  
> &nbsp;&nbsp; &nbsp;&nbsp; | STRING_CONTINUE  
> &nbsp;&nbsp; )<sup>\*</sup> `"`  
>  
> [STRING_CONTINUE] :<a name="string_continue"></a>  
> &nbsp;&nbsp; `\` _followed by_ \\n  
>  
> [RAW_STRING_LITERAL] :<a name="raw_string_literal"></a>  
> &nbsp;&nbsp; `r` RAW_STRING_CONTENT  
>  
> [RAW_STRING_CONTENT] :<a name="raw_string_content"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; `"` ( ~ _IsolatedCR_ )<sup>* (non-greedy)</sup> `"`  
> &nbsp;&nbsp; | `#` RAW_STRING_CONTENT `#`  
>  
> [BYTE_LITERAL] :<a name="byte_literal"></a>  
> &nbsp;&nbsp; `b'` ( ASCII_FOR_CHAR | BYTE_ESCAPE )  `'`  
>  
> [ASCII_FOR_CHAR] :<a name="ascii_for_char"></a>  
> &nbsp;&nbsp; _any ASCII (i.e. 0x00 to 0x7F), except_ `'`, `/`, \\n, \\r or \\t  
>  
> [BYTE_ESCAPE] :<a name="byte_escape"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; `\x` HEX_DIGIT HEX_DIGIT  
> &nbsp;&nbsp; | `\n` | `\r` | `\t` | `\\` | `\0`  
>  
> [BYTE_STRING_LITERAL] :<a name="byte_string_literal"></a>  
> &nbsp;&nbsp; `b"` ( ASCII_FOR_STRING | BYTE_ESCAPE | STRING_CONTINUE )<sup>\*</sup> `"`  
>  
> [ASCII_FOR_STRING] :<a name="ascii_for_string"></a>  
> &nbsp;&nbsp; _any ASCII (i.e 0x00 to 0x7F), except_ `"`, `/` _and IsolatedCR_ 
>  
> [RAW_BYTE_STRING_LITERAL] :<a name="raw_byte_string_literal"></a>  
> &nbsp;&nbsp; `br` RAW_BYTE_STRING_CONTENT  
>  
> [RAW_BYTE_STRING_CONTENT] :<a name="raw_byte_string_content"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; `"` ASCII<sup>* (non-greedy)</sup> `"`  
> &nbsp;&nbsp; | `#` RAW_STRING_CONTENT `#`  
>  
> [ASCII] :<a name="ascii"></a>  
> &nbsp;&nbsp; _any ASCII (i.e. 0x00 to 0x7F)_  
>  
> [INTEGER_LITERAL] :<a name="integer_literal"></a>  
> &nbsp;&nbsp; ( DEC_LITERAL | BIN_LITERAL | OCT_LITERAL | HEX_LITERAL )
>              INTEGER_SUFFIX<sup>?</sup>
>   
> [DEC_LITERAL] :<a name="dec_literal"></a>  
> &nbsp;&nbsp; DEC_DIGIT (DEC_DIGIT|`_`)<sup>\*</sup>  
>  
> [BIN_LITERAL] :<a name="bin_literal"></a>  
> &nbsp;&nbsp; `0b` (BIN_DIGIT|`_`)<sup>\*</sup> BIN_DIGIT (BIN_DIGIT|`_`)<sup>\*</sup>  
>  
> [OCT_LITERAL] :<a name="oct_literal"></a>  
> &nbsp;&nbsp; `0o` (OCT_DIGIT|`_`)<sup>\*</sup> OCT_DIGIT (OCT_DIGIT|`_`)<sup>\*</sup>  
>  
> [HEX_LITERAL] :<a name="hex_literal"></a>  
> &nbsp;&nbsp; `0x` (HEX_DIGIT|`_`)<sup>\*</sup> HEX_DIGIT (HEX_DIGIT|`_`)<sup>\*</sup>  
>  
> [BIN_DIGIT] :<a name="bin_digit"></a> [`0`-`1`]  
>  
> [OCT_DIGIT] :<a name="oct_digit"></a> [`0`-`7`]  
>  
> [DEC_DIGIT] :<a name="dec_digit"></a> [`0`-`9`]  
>  
> [HEX_DIGIT] :<a name="hex_digit"></a> [`0`-`9` `a`-`f` `A`-`F`]  
>  
> [INTEGER_SUFFIX] :<a name="integer_suffix"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; `u8` | `u16` | `u32` | `u64` | `usize`  
> &nbsp;&nbsp; | `i8` | `u16` | `i32` | `i64` | `usize`
>  
> [FLOAT_LITERAL] :<a name="float_literal"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; DEC_LITERAL `.`
>   _(not immediately followed by `.`, `_` or an identifier_)  
> &nbsp;&nbsp; | DEC_LITERAL FLOAT_EXPONENT  
> &nbsp;&nbsp; | DEC_LITERAL `.` DEC_LITERAL FLOAT_EXPONENT<sup>?</sup>  
> &nbsp;&nbsp; | DEC_LITERAL (`.` DEC_LITERAL)<sup>?</sup>
>                    FLOAT_EXPONENT<sup>?</sup> FLOAT_SUFFIX  
>  
> [FLOAT_EXPONENT] :<a name="float_exponent"></a>  
> &nbsp;&nbsp; (`e`|`E`) (`+`|`-`)?
>               (DEC_DIGIT|`_`)<sup>\*</sup> DEC_DIGIT (DEC_DIGIT|`_`)<sup>\*</sup>   
>  
> [FLOAT_SUFFIX] :<a name="float_suffix"></a>  
> &nbsp;&nbsp; `f32` | `f64`
>  
> [BOOLEAN_LITERAL] :<a name="boolean_literal"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; `true`  
> &nbsp;&nbsp; | `false`  
>  

### Crates and source files

> [UTF8BOM] :<a name="utf8bom"></a> `\uFEFF`  
> [SHEBANG] :<a name="shebang"></a> `#!` ~[`[` `\n`] ~`\n`<sup>\*</sup>
>  

[KW_AS]: #kw_as
[KW_BOX]: #kw_box
[KW_BREAK]: #kw_break
[KW_CONST]: #kw_const
[KW_CONTINUE]: #kw_continue
[KW_CRATE]: #kw_crate
[KW_ELSE]: #kw_else
[KW_ENUM]: #kw_enum
[KW_EXTERN]: #kw_extern
[KW_FALSE]: #kw_false
[KW_FN]: #kw_fn
[KW_FOR]: #kw_for
[KW_IF]: #kw_if
[KW_IMPL]: #kw_impl
[KW_IN]: #kw_in
[KW_LET]: #kw_let
[KW_LOOP]: #kw_loop
[KW_MATCH]: #kw_match
[KW_MOD]: #kw_mod
[KW_MOVE]: #kw_move
[KW_MUT]: #kw_mut
[KW_PUB]: #kw_pub
[KW_REF]: #kw_ref
[KW_RETURN]: #kw_return
[KW_SELFVALUE]: #kw_selfvalue
[KW_SELFTYPE]: #kw_selftype
[KW_STATIC]: #kw_static
[KW_STRUCT]: #kw_struct
[KW_SUPER]: #kw_super
[KW_TRAIT]: #kw_trait
[KW_TRUE]: #kw_true
[KW_TYPE]: #kw_type
[KW_UNSAFE]: #kw_unsafe
[KW_USE]: #kw_use
[KW_WHERE]: #kw_where
[KW_WHILE]: #kw_while
[KW_CATCH]: #kw_catch
[KW_DEFAULT]: #kw_default
[KW_UNION]: #kw_union
[KW_STATICLIFETIME]: #kw_staticlifetime
[KW_ABSTRACT]: #kw_abstract
[KW_ALIGNOF]: #kw_alignof
[KW_BECOME]: #kw_become
[KW_DO]: #kw_do
[KW_FINAL]: #kw_final
[KW_MACRO]: #kw_macro
[KW_OFFSETOF]: #kw_offsetof
[KW_OVERRIDE]: #kw_override
[KW_PRIV]: #kw_priv
[KW_PROC]: #kw_proc
[KW_PURE]: #kw_pure
[KW_SIZEOF]: #kw_sizeof
[KW_TYPEOF]: #kw_typeof
[KW_UNSIZED]: #kw_unsized
[KW_VIRTUAL]: #kw_virtual
[KW_YIELD]: #kw_yield
[IDENTIFIER]: #identifier
[LINE_COMMENT]: #line_comment
[BLOCK_COMMENT]: #block_comment
[INNER_LINE_DOC]: #inner_line_doc
[INNER_BLOCK_DOC]: #inner_block_doc
[OUTER_LINE_DOC]: #outer_line_doc
[OUTER_BLOCK_DOC]: #outer_block_doc
[_BlockCommentOrDoc_]: #blockcommentordoc
[_IsolatedCR_]: #isolatedcr
[CHAR_LITERAL]: #char_literal
[QUOTE_ESCAPE]: #quote_escape
[ASCII_ESCAPE]: #ascii_escape
[UNICODE_ESCAPE]: #unicode_escape
[STRING_LITERAL]: #string_literal
[STRING_CONTINUE]: #string_continue
[RAW_STRING_LITERAL]: #raw_string_literal
[RAW_STRING_CONTENT]: #raw_string_content
[BYTE_LITERAL]: #byte_literal
[ASCII_FOR_CHAR]: #ascii_for_char
[BYTE_ESCAPE]: #byte_escape
[BYTE_STRING_LITERAL]: #byte_string_literal
[ASCII_FOR_STRING]: #ascii_for_string
[RAW_BYTE_STRING_LITERAL]: #raw_byte_string_literal
[RAW_BYTE_STRING_CONTENT]: #raw_byte_string_content
[ASCII]: #ascii
[INTEGER_LITERAL]: #integer_literal
[DEC_LITERAL]: #dec_literal
[BIN_LITERAL]: #bin_literal
[OCT_LITERAL]: #oct_literal
[HEX_LITERAL]: #hex_literal
[BIN_DIGIT]: #bin_digit
[OCT_DIGIT]: #oct_digit
[DEC_DIGIT]: #dec_digit
[HEX_DIGIT]: #hex_digit
[INTEGER_SUFFIX]: #integer_suffix
[FLOAT_LITERAL]: #float_literal
[FLOAT_EXPONENT]: #float_exponent
[FLOAT_SUFFIX]: #float_suffix
[BOOLEAN_LITERAL]: #boolean_literal
[UTF8BOM]: #utf8bom
[SHEBANG]: #shebang


## Syntactical productions


### Crates and source files

> [_Crate_] :<a name="crate"></a>  
> &nbsp;&nbsp; UTF8BOM<sup>?</sup>  
> &nbsp;&nbsp; SHEBANG<sup>?</sup>  
> &nbsp;&nbsp; [_InnerAttribute_]<sup>\*</sup>  
> &nbsp;&nbsp; [_Item_]<sup>\*</sup>  
>  

### Visibility and Privacy

> [_Visibility_] :<a name="visibility"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; EMPTY  
> &nbsp;&nbsp; | `pub`  
> &nbsp;&nbsp; | `pub` `(` `crate` `)`  
> &nbsp;&nbsp; | `pub` `(` `in` _ModulePath_ `)`  
> &nbsp;&nbsp; | `pub` `(` `in`<sup>?</sup> `self` `)`  
> &nbsp;&nbsp; | `pub` `(` `in`<sup>?</sup> `super` `)`  
>  

### Attributes

> [_Attribute_] :<a name="attribute"></a>  
> &nbsp;&nbsp; _InnerAttribute_ | _OuterAttribute_  
>  
> [_InnerAttribute_] :<a name="innerattribute"></a>  
> &nbsp;&nbsp; `#![` MetaItem `]`  
>   
> [_OuterAttribute_] :<a name="outerattribute"></a>  
> &nbsp;&nbsp; `#[` MetaItem `]`  
>   
> [_MetaItem_] :<a name="metaitem"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; IDENTIFIER  
> &nbsp;&nbsp; | IDENTIFIER `=` LITERAL  
> &nbsp;&nbsp; | IDENTIFIER `(` _MetaSeq_ `)`  
> &nbsp;&nbsp; | IDENTIFIER `(` _MetaSeq_ `,` `)`  
>   
> [_MetaSeq_] :<a name="metaseq"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; EMPTY  
> &nbsp;&nbsp; | _MetaItem_  
> &nbsp;&nbsp; | _MetaSeq_ `,` _MetaItem_  
>  

[_Crate_]: #crate
[_Visibility_]: #visibility
[_Attribute_]: #attribute
[_InnerAttribute_]: #innerattribute
[_OuterAttribute_]: #outerattribute
[_MetaItem_]: #metaitem
[_MetaSeq_]: #metaseq