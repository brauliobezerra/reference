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
> &nbsp;&nbsp; &nbsp;&nbsp; [`a`-`z` `A`-`Z`]&nbsp;[`a`-`z` `A`-`Z` `0`-`9` `_`]<sup>\*</sup>  
> &nbsp;&nbsp; | `_` [`a`-`z` `A`-`Z` `0`-`9` `_`]<sup>+</sup>  
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

> **FIXME**
>  
> **FIXME**
>  
> **FIXME**
>  
> **FIXME**
>  
> **FIXME**
>  
> **FIXME**
>  
> **FIXME**
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
> [BIN_DIGIT] :<a name="bin_digit"></a> [`0`-`1` `_`]  
>  
> [OCT_DIGIT] :<a name="oct_digit"></a> [`0`-`7` `_`]  
>  
> [DEC_DIGIT] :<a name="dec_digit"></a> [`0`-`9` `_`]  
>  
> [HEX_DIGIT] :<a name="hex_digit"></a> [`0`-`9` `a`-`f` `A`-`F` `_`]  
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
> [EQ] :<a name="eq"></a> `=`  
> [LT] :<a name="lt"></a> `<`  
> [LE] :<a name="le"></a> `<=`  
> [EQEQ] :<a name="eqeq"></a> `==`  
> [NE] :<a name="ne"></a> `!=`  
> [GE] :<a name="ge"></a> `>=`  
> [GT] :<a name="gt"></a> `>`  
> [ANDAND] :<a name="andand"></a> `&&`  
> [OROR] :<a name="oror"></a> `||`  
> [NOT] :<a name="not"></a> `!`  
> [TILDE] :<a name="tilde"></a> `~`  
>  
> [AT] :<a name="at"></a> `@`  
> [DOT] :<a name="dot"></a> `.`  
> [DOTDOT] :<a name="dotdot"></a> `..`  
> [DOTDOTDOT] :<a name="dotdotdot"></a> `...`  
> [COMMA] :<a name="comma"></a> `,`  
> [SEMI] :<a name="semi"></a> `;`  
> [COLON] :<a name="colon"></a> `:`  
> [MOD_SEPARATOR] :<a name="mod_separator"></a> `::`  
> [RIGHT_ARROW] :<a name="right_arrow"></a> `->`  
> [LEFT_ARROW] :<a name="left_arrow"></a> `<-`  
> [FAT_ARROW] :<a name="fat_arrow"></a> `=>`  
> [POUND] :<a name="pound"></a> `#`  
> [DOLLAR] :<a name="dollar"></a> `$`  
> [QUESTION] :<a name="question"></a> `?`  
>  
> [UNDERSCORE] :<a name="underscore"></a> `_`  
> [LIFETIME_OR_LABEL] :<a name="lifetime_or_label"></a> `'` IDENTIFIER <a name="lifetime-or-label"></a>  
>  
> [OPEN_PAREN] :<a name="open_paren"></a> `(`  
> [CLOSE_PAREN] :<a name="close_paren"></a> `)`  
> [OPEN_BRACKET] :<a name="open_bracket"></a> `[`  
> [CLOSE_BRACKET] :<a name="close_bracket"></a> `]`  
> [OPEN_BRACE] :<a name="open_brace"></a> `{`  
> [CLOSE_BRACE] :<a name="close_brace"></a> `}`  
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
[EQ]: #eq
[LT]: #lt
[LE]: #le
[EQEQ]: #eqeq
[NE]: #ne
[GE]: #ge
[GT]: #gt
[ANDAND]: #andand
[OROR]: #oror
[NOT]: #not
[TILDE]: #tilde
[AT]: #at
[DOT]: #dot
[DOTDOT]: #dotdot
[DOTDOTDOT]: #dotdotdot
[COMMA]: #comma
[SEMI]: #semi
[COLON]: #colon
[MOD_SEPARATOR]: #mod_separator
[RIGHT_ARROW]: #right_arrow
[LEFT_ARROW]: #left_arrow
[FAT_ARROW]: #fat_arrow
[POUND]: #pound
[DOLLAR]: #dollar
[QUESTION]: #question
[UNDERSCORE]: #underscore
[LIFETIME_OR_LABEL]: #lifetime_or_label
[OPEN_PAREN]: #open_paren
[CLOSE_PAREN]: #close_paren
[OPEN_BRACKET]: #open_bracket
[CLOSE_BRACKET]: #close_bracket
[OPEN_BRACE]: #open_brace
[CLOSE_BRACE]: #close_brace
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

### Items

> [_Item_]:  
> &nbsp;&nbsp; [_OuterAttribute_]<sup>\*</sup> [_Visibility_]  
> &nbsp;&nbsp; (  
> &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp;  [_Module_]  
> &nbsp;&nbsp; &nbsp;&nbsp; | [_ExternCrate_]  
> &nbsp;&nbsp; &nbsp;&nbsp; | [_UseDeclaration_]  
> &nbsp;&nbsp; &nbsp;&nbsp; | [_Function_]  
> &nbsp;&nbsp; &nbsp;&nbsp; | [_TypeAlias_]  
> &nbsp;&nbsp; &nbsp;&nbsp; | [_Struct_]  
> &nbsp;&nbsp; &nbsp;&nbsp; | [_Enumeration_]  
> &nbsp;&nbsp; &nbsp;&nbsp; | [_Union_]  
> &nbsp;&nbsp; &nbsp;&nbsp; | [_ConstantItem_]  
> &nbsp;&nbsp; &nbsp;&nbsp; | [_StaticItem_]  
> &nbsp;&nbsp; &nbsp;&nbsp; | [_Trait_]  
> &nbsp;&nbsp; &nbsp;&nbsp; | [_Implementation_]  
> &nbsp;&nbsp; &nbsp;&nbsp; | [_ExternBlock_]  
> &nbsp;&nbsp; &nbsp;&nbsp; | _Macro_  
> &nbsp;&nbsp; &nbsp;&nbsp; | _MacroDefinition_  
> &nbsp;&nbsp; )
>  
> [_Generics_] :<a name="generics"></a><a name="generics"></a>  
> &nbsp;&nbsp; `<` _GenericParams_<sup>?</sup> `>`  
>  
> [_GenericParams_] :<a name="genericparams"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; _LifetimeParams_ `,`<sup>?</sup>  
> &nbsp;&nbsp; | _TypeParams_ `,`<sup>?</sup>  
> &nbsp;&nbsp; | _LifetimeParams_ `,` _TypeParams_ `,`<sup>?</sup>  
>  
> [_LifetimeParams_] :<a name="lifetimeparams"></a>  
> &nbsp;&nbsp; _LifetimeParam_ (`,` _LifetimeParam_)<sup>\*</sup>  
>  
> [_LifetimeParam_] :<a name="lifetimeparam"></a>  
> &nbsp;&nbsp; [LIFETIME_OR_LABEL] _LifetimeBounds_<sup>?</sup>  
>  
> _TypeParams_:  
> &nbsp;&nbsp; _TypeParam_ (`,` _TypeParam_)<sup>\*</sup>  
>  
> [_TypeParam_] :<a name="typeparam"></a>  
> &nbsp;&nbsp; [IDENTIFIER] _TypeParamBounds_<sup>?</sup> ( `=` [_Type_] )<sup>?</sup>  
>  
> [_TypeParamBounds_] :<a name="typeparambounds"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; [LIFETIME_OR_LABEL]  
> &nbsp;&nbsp; | `(` [LIFETIME_OR_LABEL] `)`  
> &nbsp;&nbsp; | `?`<sup>?</sup> _LateBoundLifetimeDefs_<sup>?</sup> [_TypePath_]  
> &nbsp;&nbsp; | `(` `?`<sup>?</sup> _LateBoundLifetimeDefs_<sup>?</sup> [_TypePath_] `)`  
>  
> [_LifetimeBounds_] :<a name="lifetimebounds"></a>  
> &nbsp;&nbsp; `:` [LIFETIME_OR_LABEL] ( `+` [LIFETIME_OR_LABEL] )<sup>\*</sup> `+`<sup>?</sup>  
>  
> [_LateBoundLifetimeDefs_] :<a name="lateboundlifetimedefs"></a>  
> &nbsp;&nbsp; `for` `<` _LifetimeParams_ `,`<sup>?</sup> `>`
>  
> [_WhereClause_] :<a name="whereclause"></a><a name="where-clause"></a>  
> &nbsp;&nbsp; `where` ( _WhereClauseItem_ ( `,` _WhereClauseItem_ )<sup>\*</sup> `,`<sup>?</sup> )<sup>?</sup>  
>  
> [_WhereClauseItem_] :<a name="whereclauseitem"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; _LifetimeWhereClauseItem_  
> &nbsp;&nbsp; | _TypeBoundWhereClauseItem_  
> &nbsp;&nbsp; | _TypeEqualWhereClauseItem_  
>  
> [_LifetimeWhereClauseItem_] :<a name="lifetimewhereclauseitem"></a>  
> &nbsp;&nbsp; [LIFETIME_OR_LABEL] _LifetimeBounds_  
>  
> [_TypeBoundWhereClauseItem_] :<a name="typeboundwhereclauseitem"></a>  
> &nbsp;&nbsp; _LateBoundLifetimeDefs_<sup>?</sup> [_Type_] `:` _TypeParamBounds_  
>  
> [_TypeEqualWhereClauseItem_] :<a name="typeequalwhereclauseitem"></a>  
> &nbsp;&nbsp; _LateBoundLifetimeDefs_<sup>?</sup> [_Type_]&nbsp;(`=`|`==`) [_Type_]  
>  
> [_Module_] :<a name="module"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; `mod` [IDENTIFIER] `;`  
> &nbsp;&nbsp; | `mod` [IDENTIFIER] `{`  
> &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [_InnerAttribute_]<sup>\*</sup>  
> &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [_Item_]<sup>\*</sup>  
> &nbsp;&nbsp; &nbsp;&nbsp; `}`  
>  
> [_ExternCrate_] :<a name="externcrate"></a>  
> &nbsp;&nbsp; `extern` `crate` [IDENTIFIER] (`as` [IDENTIFIER])<sup>?</sup> `;`
>  
> [_UseDeclaration_] :<a name="usedeclaration"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; `use` `::`<sup>?</sup> [_NonGlobalPath_]  
> &nbsp;&nbsp; | `use` `::`<sup>?</sup> [_NonGlobalPath_] `as` [IDENTIFIER]  
> &nbsp;&nbsp; | `use` `::`<sup>?</sup> [_NonGlobalPath_] `::` `*`  
> &nbsp;&nbsp; | `use` `::`<sup>?</sup> [_NonGlobalPath_] `::` `{` _UseItems_ `}`  
> &nbsp;&nbsp; | `use` `::`<sup>?</sup> `{` _UseItems_ `}`  
>  
> [_UseItems_] :<a name="useitems"></a>  
> &nbsp;&nbsp; ( `self` | [IDENTIFIER] (`as` [IDENTIFIER] )<sup>?</sup> )
>              ( `,` _UseItems_ )<sup>?<sup>
>  
> [_Function_]:  
> &nbsp;&nbsp; `unsafe`<sup>?</sup> (`extern` Abi<sup>?</sup>)<sup>?</sup> `fn`
>              [IDENTIFIER]&nbsp;[_Generics_]<sup>?</sup>  
> &nbsp;&nbsp; &nbsp;&nbsp; `(` _FunctionParameters_<sup>?</sup> `)`
>              _FunctionReturnType_<sup>?</sup> [_WhereClause_]<sup>?</sup>  
> &nbsp;&nbsp; &nbsp;&nbsp; _BlockWithInnerAttributes_
>  
> _Abi_:  
> &nbsp;&nbsp; STRING_LITERAL  
>  
> _FunctionParameters_:  
> &nbsp;&nbsp; _FunctionParam_ (`,` _FunctionParam_)<sup>\*</sup> `,`<sup>?</sup>  
>  
> [_FunctionParam_] :<a name="functionparam"></a>  
> &nbsp;&nbsp; _Pattern_ `:` _Type_  
>  
> _FunctionReturnType_:  
> &nbsp;&nbsp; `->` [_Type_]  
>  
> [_BlockWithInnerAttributes_] :<a name="blockwithinnerattributes"></a>  
> &nbsp;&nbsp; `{`  
> &nbsp;&nbsp; &nbsp;&nbsp; [_InnerAttribute_]<sup>\*</sup>  
> &nbsp;&nbsp; &nbsp;&nbsp; [_Statement_]<sup>\*</sup>  
> &nbsp;&nbsp; `}`  
>  
> [_TypeAlias_] :<a name="typealias"></a>  
> &nbsp;&nbsp; `type` [IDENTIFIER]&nbsp;[_Generics_]<sup>?</sup>
>              [_WhereClause_]<sup>?</sup> `=` [_Type_] `;`  
>  
> [_Struct_] :<a name="struct"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; _StructStruct_  
> &nbsp;&nbsp; | _TupleStruct_  
>  
> [_StructStruct_] :<a name="structstruct"></a>  
> &nbsp;&nbsp; `struct`
>   [IDENTIFIER]&nbsp;
>   [_Generics_]<sup>?</sup>
>   [_WhereClause_]<sup>?</sup>
>   ( `{` _StructFields_<sup>?</sup> `}` | `;` )  
>  
> [_TupleStruct_] :<a name="tuplestruct"></a>  
> &nbsp;&nbsp; `struct`
>   [IDENTIFIER]&nbsp;
>   [_Generics_]<sup>?</sup>
>   `(` _TupleFields_<sup>?</sup> `)`
>   [_WhereClause_]<sup>?</sup>
>   `;`  
>  
> [_StructFields_] :<a name="structfields"></a><a name="struct-fields"></a>  
> &nbsp;&nbsp; _StructField_ (`,` _StructField_)<sup>\*</sup> `,`<sup>?</sup>  
>  
> [_StructField_] :<a name="structfield"></a>  
> &nbsp;&nbsp; [_OuterAttribute_]<sup>\*</sup>  
> &nbsp;&nbsp; [_Visibility_]<sup>?</sup>  
> &nbsp;&nbsp; [IDENTIFIER] `:` [_Type_]  
>  
> [_TupleFields_] :<a name="tuplefields"></a><a name="tuple-fields"></a>  
> &nbsp;&nbsp; _TupleField_ (`,` _TupleField_)<sup>\*</sup> `,`<sup>?</sup>  
>  
> [_TupleField_] :<a name="tuplefield"></a>  
> &nbsp;&nbsp; [_OuterAttribute_]<sup>\*</sup>  
> &nbsp;&nbsp; [_Visibility_]<sup>?</sup>  
> &nbsp;&nbsp; [_Type_]  
>  
> [_Enumeration_] :<a name="enumeration"></a>  
> &nbsp;&nbsp; `enum`
>    [IDENTIFIER]&nbsp;
>    [_Generics_]<sup>?</sup>
>    [_WhereClause_]<sup>?</sup>
>    `{` _EnumItems_<sup>?</sup> `}`  
>  
> [_EnumItems_] :<a name="enumitems"></a>  
> &nbsp;&nbsp; _EnumItem_ ( `,` _EnumItem_ )<sup>\*</sup> `,`<sup>?</sup>  
>  
> [_EnumItem_] :<a name="enumitem"></a>  
> &nbsp;&nbsp; _OuterAttribute_<sup>\*</sup>  
> &nbsp;&nbsp; [IDENTIFIER]&nbsp;( _EnumItemTuple_ | _EnumItemStruct_ 
>                                | _EnumItemDiscriminant_ )<sup>?</sup>  
>  
> [_EnumItemTuple_] :<a name="enumitemtuple"></a>  
> &nbsp;&nbsp; `(` [_TupleFields_]<sup>?</sup> `)`  
>   
> [_EnumItemStruct_] :<a name="enumitemstruct"></a>  
> &nbsp;&nbsp; `{` [_StructFields_]<sup>?</sup> `}`  
>   
> [_EnumItemDiscriminant_] :<a name="enumitemdiscriminant"></a>  
> &nbsp;&nbsp; `=` [_Expression_]  
>  
> [_Union_] :<a name="union"></a>  
> &nbsp;&nbsp; `union` [_Generics_]<sup>?</sup> [_WhereClause_]<sup>?</sup>
>   `{`[_StructFields_] `}`
>  
> [_ConstantItem_] :<a name="constantitem"></a>  
> &nbsp;&nbsp; `const` [IDENTIFIER] `:` [_Type_] `=` [_Expression_]
>  
> [_StaticItem_] :<a name="staticitem"></a>  
> &nbsp;&nbsp; `static` `mut`? [IDENTIFIER] `:` [_Type_] `=` [_Expression_] `;`
>  
> [_Trait_] :<a name="trait"></a>  
> &nbsp;&nbsp; `unsafe`<sup>?</sup>  
> &nbsp;&nbsp; `trait` [_Identifier_]  
> &nbsp;&nbsp; [_Type-Parameters_](#type-parameters)<sup>?</sup>  
> &nbsp;&nbsp; (`for` _Type_)<sup>?</sup>  
> &nbsp;&nbsp; (`:` _TypeBound_)<sup>?</sup> `{`  
> &nbsp;&nbsp;&nbsp;&nbsp; _Trait-Item_<sup>\*</sup>  
> &nbsp;&nbsp; `}`  
>   
> _Trait-Item_ :  
> &nbsp;&nbsp; _Trait-Method_ | _Trait-Const_ | _Trait-Type_  
>   
> _Trait-Method_ :  
> &nbsp;&nbsp; _Type-Method_ | _Method_
>  
> [_Implementation_] :<a name="implementation"></a>  
> `unsafe`? `impl` [_Generics_] (`!`? _TraitName_ `for`)? (_TypeName_ | `..`) `{`  
> &nbsp;&nbsp; _InnerAttributes?_  
> &nbsp;&nbsp; _ImplementationItems?_  
> `}`
>  
> [_ExternBlock_] :<a name="externblock"></a>  
> &nbsp;&nbsp; `extern` _Abi_<sup>?</sup> `{`  
> &nbsp;&nbsp; &nbsp;&nbsp; _InnerAttribute_<sup>\*</sup>  
> &nbsp;&nbsp; &nbsp;&nbsp; _ExternalItem_<sup>\*</sup>  
> &nbsp;&nbsp; `}`  
>  
> [_ExternalItem_] :<a name="externalitem"></a>  
> &nbsp;&nbsp; _OuterAttribute_<sup>\*</sup>  
> &nbsp;&nbsp; _VisibilityNoTuple_<sup>?</sup>  
> &nbsp;&nbsp; (externalStaticItem | externalFunctionItem)  
>  
> [_ExternalStaticItem_] :<a name="externalstaticitem"></a>  
> &nbsp;&nbsp; `static` `mut`<sup>?</sup> IDENTIFIER `:` _Type_ `;`  
>  
> [_ExternalFunctionItem_] :<a name="externalfunctionitem"></a>  
> &nbsp;&nbsp; `fn` IDENTIFIER _Generics_<sup>?</sup>  
> &nbsp;&nbsp; ( _FunctionParameters_ | _FunctionParametersWithVariadics_ )  
> &nbsp;&nbsp; _FunctionReturnType_<sup>?</sup> _WhereClause_<sup>?</sup> `;`  
>  
> [_FunctionParametersWithVariadics_] :<a name="functionparameterswithvariadics"></a>  
> &nbsp;&nbsp; `(` ( _FunctionParam_ `,` )<sup>\*</sup> _VariadicFunctionParam_ `)`  
>  
> [_VariadicFunctionParam_] :<a name="variadicfunctionparam"></a>  
> &nbsp;&nbsp; _FunctionParam_ `,` `...`  
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

### Statements

> [_Statement_] :<a name="statement"></a>  
> &nbsp;&nbsp; [_DeclarationStatement_] | [_Expression_] | `;`  
>  
> [_DeclarationStatement_] :<a name="declarationstatement"></a>  
> &nbsp;&nbsp; [_Item_] | [_LocalVariablesDeclaration_]
>  
> [_LocalVariablesDeclaration_] :<a name="localvariablesdeclaration"></a>  
> &nbsp;&nbsp; `let` [_Pattern_]&nbsp;( `:` [_Type_] )<sup>?</sup> (`=` [_Expression_] )<sup>?</sup> `;`
>  
> [_ExpressionStatement_] :<a name="expressionstatement"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; _ExpressionWithBlock_  
> &nbsp;&nbsp; | _ExpressionWithoutBlock_ `;`  
>  
> [_ExpressionWithBlock_] :<a name="expressionwithblock"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; BlockExpression  
> &nbsp;&nbsp; | LoopExpression  
> &nbsp;&nbsp; | IfExpression  
> &nbsp;&nbsp; | IfLetExpression  
> &nbsp;&nbsp; | MatchExpression  
> &nbsp;&nbsp; | WhileExpression  
> &nbsp;&nbsp; | WhileLetExpression  
>  
> _ExpressionWithoutBlock_: all other expression types
>  

### Expressions

> [_Expression_] :<a name="expression"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; [_LiteralExpression_]  
> &nbsp;&nbsp; | [_PathExpression_]  
> &nbsp;&nbsp; | [_TupleExpression_]  
> &nbsp;&nbsp; | [_StructExpression_]  
> &nbsp;&nbsp; | [_EnumerationVariantExpression_]  
> &nbsp;&nbsp; | [_BlockExpression_]  
> &nbsp;&nbsp; | [_MethodCallExpression_]  
> &nbsp;&nbsp; | [_FieldExpression_]  
> &nbsp;&nbsp; | [_TupleIndexingExpression_]  
> &nbsp;&nbsp; | [_CallExpression_]  
> &nbsp;&nbsp; | [_ClosureExpression_]  
> &nbsp;&nbsp; | [_ArrayExpression_]  
> &nbsp;&nbsp; | [_IndexExpression_]  
> &nbsp;&nbsp; | [_RangeExpression_]  
> &nbsp;&nbsp; | [_OperatorExpression_]  
> &nbsp;&nbsp; | [_GroupedExpression_]  
> &nbsp;&nbsp; | [_LoopExpression_]  
> &nbsp;&nbsp; | [_ContinueExpression_]  
> &nbsp;&nbsp; | [_BreakExpression_]  
> &nbsp;&nbsp; | [_IfExpression_]  
> &nbsp;&nbsp; | [_MatchExpression_]  
> &nbsp;&nbsp; | [_IfLetExpression_]  
> &nbsp;&nbsp; | [_WhileLetExpression_]  
> &nbsp;&nbsp; | [_ReturnExpression_]  
>  
> [_LiteralExpression_] :<a name="literalexpression"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; [CHARACTER_LITERAL]  
> &nbsp;&nbsp; | [STRING_LITERAL]  
> &nbsp;&nbsp; | [RAW_STRING_LITERAL]  
> &nbsp;&nbsp; | [BYTE_LITERAL]  
> &nbsp;&nbsp; | [BYTE_STRING_LITERAL]  
> &nbsp;&nbsp; | [RAW_BYTE_STRING_LITERAL]  
> &nbsp;&nbsp; | [INTEGER_LITERAL]  
> &nbsp;&nbsp; | [FLOAT_LITERAL]  
> &nbsp;&nbsp; | [BOOLEAN_LITERAL]  
>  
> FIXME
>  
> [_TupleExpression_] :<a name="tupleexpression"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; `(` [_Expression_] `,` `)`  
> &nbsp;&nbsp; | `(` [_Expression_] (`,` [_Expression_] )<sup>\+</sup> 
>                `,`<sup>?</sup> `)`  
>  
> FIXME
> FIXME include shorthand?
>  
> FIXME
>  
> FIXME
>  
> [_BlockExpression_] :<a name="blockexpression"></a>  
> &nbsp;&nbsp; `{`  
> &nbsp;&nbsp; &nbsp;&nbsp; [_InnerAttribute_]*  
> &nbsp;&nbsp; &nbsp;&nbsp; [_Statement_]*  
> &nbsp;&nbsp; `}`  
>  
> FIXME
>  
> FIXME
>  
> [_FieldExpression_] :<a name="fieldexpression"></a>  
> &nbsp;&nbsp; [_Expression_] `.` [IDENTIFIER]
>  
> [_TupleIndexingExpression_] :<a name="tupleindexingexpression"></a>  
> &nbsp;&nbsp; [_Expression_] `.` [DECIMAL_LITERAL]
>  
> FIXME
>  
> [_ClosureExpression_] :<a name="closureexpression"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; `move`<sup>?</sup> `|` ParameterList<sup>?</sup> `|`
>                           [_Expression_]  
> &nbsp;&nbsp; | `move`<sup>?</sup> `|` ParameterList<sup>?</sup> `|` `->` _Type_
>                [_BlockExpression_]  
>  
> [_ArrayExpression_] :<a name="arrayexpression"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; `[`  `]`  
> &nbsp;&nbsp; | `[` [_Expression_] ( `,` [_Expression_] )<sup>\*</sup> `,`<sup>?</sup> `]`  
> &nbsp;&nbsp; | `[` [_Expression_] `;` [_Expression_] `]`  
>  
> [_IndexExpression_] :<a name="indexexpression"></a>  
> &nbsp;&nbsp; [_Expression_] `[` [_Expression_] `]`
>  
> [_RangeExpression_] :<a name="rangeexpression"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; _RangeExpr_  
> &nbsp;&nbsp; | _RangeFromExpr_  
> &nbsp;&nbsp; | _RangeToExpr_  
> &nbsp;&nbsp; | _RangeFullExpr_  
>  
> [_RangeExpr_] :<a name="rangeexpr"></a>  
> &nbsp;&nbsp; [_Expression_] `..` [_Expression_]  
>  
> [_RangeFromExpr_] :<a name="rangefromexpr"></a>  
> &nbsp;&nbsp; [_Expression_] `..`  
>  
> [_RangeToExpr_] :<a name="rangetoexpr"></a>  
> &nbsp;&nbsp; `..` [_Expression_]  
>  
> [_RangeFullExpr_] :<a name="rangefullexpr"></a>  
> &nbsp;&nbsp; `..`  
>  
> [_OperatorExpression_] :<a name="operatorexpression"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; [_BorrowExpression_](#borrow-operators)  
> &nbsp;&nbsp; | [_DereferenceExpression_](#the-dereference-operator)  
> &nbsp;&nbsp; | [_ErrorPropagationExpression_](#the--operator)  
> &nbsp;&nbsp; | [_NegationExpression_](#negation-operators)  
> &nbsp;&nbsp; | [_ArithmeticOrLogicalExpression_](#arithmetic-and-logical-binary-operators)  
> &nbsp;&nbsp; | [_ComparisonExpression_](#comparison-operators)  
> &nbsp;&nbsp; | [_LazyBooleanExpression_](#lazy-boolean-expression)  
> &nbsp;&nbsp; | [_TypeCastExpression_](#type-cast-expressions)  
> &nbsp;&nbsp; | [_AssignmentExpression_](#assignment-expressions)  
> &nbsp;&nbsp; | [_CompoundAssignmentExpression_](#compound-assignment-expressions)  
>  
> [_BorrowExpression_] :<a name="borrowexpression"></a>   
> &nbsp;&nbsp; &nbsp;&nbsp; `&` [_Expression_]  
> &nbsp;&nbsp; | `&` `mut` [_Expression_]  
>  
> [_DereferenceExpression_] :<a name="dereferenceexpression"></a>  
> &nbsp;&nbsp; `*` [_Expression_]
>  
> [_ErrorPropagationExpression_] :<a name="errorpropagationexpression"></a>  
> &nbsp;&nbsp; [_Expression_] `?`  
>  
> [_NegationExpression_] :<a name="negationexpression"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; `-` [_Expression_]  
> &nbsp;&nbsp; | `!` [_Expression_]  
>  
> [_ArithmeticOrLogicalExpression_] :<a name="arithmeticorlogicalexpression"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; [_Expression_] `+` [_Expression_]  
> &nbsp;&nbsp; | [_Expression_] `-` [_Expression_]  
> &nbsp;&nbsp; | [_Expression_] `*` [_Expression_]  
> &nbsp;&nbsp; | [_Expression_] `/` [_Expression_]  
> &nbsp;&nbsp; | [_Expression_] `%` [_Expression_]  
> &nbsp;&nbsp; | [_Expression_] `&` [_Expression_]  
> &nbsp;&nbsp; | [_Expression_] `|` [_Expression_]  
> &nbsp;&nbsp; | [_Expression_] `^` [_Expression_]  
> &nbsp;&nbsp; | [_Expression_] `<<` [_Expression_]  
> &nbsp;&nbsp; | [_Expression_] `>>` [_Expression_]  
>  
> [_ComparisonExpression_] :<a name="comparisonexpression"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; [_Expression_] `==` [_Expression_]  
> &nbsp;&nbsp; | [_Expression_] `!=` [_Expression_]  
> &nbsp;&nbsp; | [_Expression_] `>` [_Expression_]  
> &nbsp;&nbsp; | [_Expression_] `<` [_Expression_]  
> &nbsp;&nbsp; | [_Expression_] `>=` [_Expression_]  
> &nbsp;&nbsp; | [_Expression_] `<=` [_Expression_]  
>  
> [_LazyBooleanExpression_] :<a name="lazybooleanexpression"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; [_Expression_] `||` [_Expression_]  
> &nbsp;&nbsp; | [_Expression_] `&&` [_Expression_]
>  
> [_TypeCastExpression_] :<a name="typecastexpression"></a>  
> &nbsp;&nbsp; [_Expression_] `as` [IDENTIFIER]
>  
> [_AssignmentExpression_] :<a name="assignmentexpression"></a>  
> &nbsp;&nbsp; | [_Expression_] `=` [_Expression_]  
>  
> [_CompoundAssignmentExpression_] :<a name="compoundassignmentexpression"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; [_Expression_] `+=` [_Expression_]  
> &nbsp;&nbsp; | [_Expression_] `-=` [_Expression_]  
> &nbsp;&nbsp; | [_Expression_] `*=` [_Expression_]  
> &nbsp;&nbsp; | [_Expression_] `/=` [_Expression_]  
> &nbsp;&nbsp; | [_Expression_] `%=` [_Expression_]  
> &nbsp;&nbsp; | [_Expression_] `&=` [_Expression_]  
> &nbsp;&nbsp; | [_Expression_] `|=` [_Expression_]  
> &nbsp;&nbsp; | [_Expression_] `^=` [_Expression_]  
> &nbsp;&nbsp; | [_Expression_] `<<=` [_Expression_]  
> &nbsp;&nbsp; | [_Expression_] `>>=` [_Expression_]  
>  
> [_GroupedExpression_] :<a name="groupedexpression"></a>  
> &nbsp;&nbsp; `(` [_Expression_] `)`
>  
> [_LoopExpression_] :<a name="loopexpression"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; _LoopLabel_<sup>?</sup> (
> [_InfiniteLoopExpression_](#infinite-loops)
> | [_PredicateLoopExpression_](#predicate-loops)
> | [_IteratorLoopExpression_](#iterator-loops)
> )  
>  
> [_InfiniteLoopExpression_] :<a name="infiniteloopexpression"></a>  
> &nbsp;&nbsp; `loop` [_BlockExpression_]
>  
> [_PredicateLoopExpression_] :<a name="predicateloopexpression"></a>  
> &nbsp;&nbsp; `while` [_Expression_]&nbsp;[_BlockExpression_]
>  
> [_IteratorLoopExpression_] :<a name="iteratorloopexpression"></a>  
> &nbsp;&nbsp; `for` [IDENTIFIER] `in` [_Expression_]&nbsp;[_BlockExpression_]
>  
> [_LoopLabel_] :<a name="looplabel"></a>  
> &nbsp;&nbsp; LIFETIME_OR_LABEL `:`
>  
> [_BreakExpression_] :<a name="breakexpression"></a>  
> &nbsp;&nbsp; `break` LIFETIME_OR_LABEL<sup>?</sup> [_Expression_]<sup>?</sup>
>  
> [_ContinueExpression_] :<a name="continueexpression"></a>  
> &nbsp;&nbsp; `continue` LIFETIME_OR_LABEL<sup>?</sup>
>  
> [_IfExpression_] :<a name="ifexpression"></a>  
> &nbsp;&nbsp; `if` [_Expression_]&nbsp;[_BlockExpression_]  
> &nbsp;&nbsp; (`else` (
>   [_BlockExpression_]
> | [_IfExpression_]
> | [_IfLetExpression_] ) )<sup>\?</sup>  
>  
> [_MatchExpression_] :<a name="matchexpression"></a>  
> &nbsp;&nbsp; `match` [_Expression_] `{`  
> &nbsp;&nbsp; &nbsp;&nbsp; [_InnerAttribute_]<sup>\*</sup>  
> &nbsp;&nbsp; &nbsp;&nbsp; ( _MatchArm_ `=>` 
>                             ( [_BlockExpression_] `,`<sup>?</sup>
>                             | [_Expression_] `,` ) 
>                           )<sup>\*</sup>  
> &nbsp;&nbsp; &nbsp;&nbsp; _MatchArm_ `=>` 
>                             ( [_BlockExpression_] | [_Expression_] ) `,`<sup>?</sup>  
> &nbsp;&nbsp; `}`  
>  
> [_MatchArm_] :<a name="matcharm"></a>  
> &nbsp;&nbsp; [_OuterAttribute_]<sup>\*</sup> _MatchArmPatterns_ _MatchArmGuard_
>  
> [_MatchArmPatterns_] :<a name="matcharmpatterns"></a>  
> &nbsp;&nbsp; [_Pattern_] ( `|` [_Pattern_] )<sup>*</sup>  
>  
> [_MatchArmGuard_] :<a name="matcharmguard"></a>  
> &nbsp;&nbsp; `if` [_Expression_]  
>  
> [_IfLetExpression_] :<a name="ifletexpression"></a>  
> &nbsp;&nbsp; `if` `let` [_Pattern_] `=` [_Expression_]&nbsp;[_BlockExpression_]  
> &nbsp;&nbsp; (`else` (
>   [_BlockExpression_]
> | [_IfExpression_]
> | [_IfLetExpression_] ) )<sup>\?</sup>  
>  
> [_WhileLetExpression_] :<a name="whileletexpression"></a>  
> &nbsp;&nbsp; `while` `let` [_Pattern_] `=` [_Expression_]&nbsp;[_BlockExpression_]  
>  
> [_ReturnExpression_] :<a name="returnexpression"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; `return`  
> &nbsp;&nbsp; | `return` [_Expression_]  
>  

### Paths

> [_Path_] :<a name="path"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; [_NonGlobalPath_]  
> &nbsp;&nbsp; | [_GlobalPath_]  
>  
> [_NonGlobalPath_] :<a name="nonglobalpath"></a> <a name="nonglobal-path"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; [_PathSegment_] ( `::` [_NonGlobalPath_] )<sup>?</sup>  
>  
> [_GlobalPath_] :<a name="globalpath"></a> <a name="global-path"></a>  
> &nbsp;&nbsp; `::` [_NonGlobalPath_]  
>  
> [_PathSegment_] :<a name="pathsegment"></a> <a name="path-segment"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; [IDENTIFIER]  
> &nbsp;&nbsp; | `<` _TypeArguments_ `>`  
> &nbsp;&nbsp; | `super`  
> &nbsp;&nbsp; | `self`  
>  
> [_PathParameter_] :<a name="pathparameter"></a>  
>  
>  
> [_ModulePath_] :<a name="modulepath"></a>  
> &nbsp;&nbsp; _ModulePathItem_ ( `::` _ModulePathItem_ )<sup>*</sup>  
>  
> [_ModulePathItem_] :<a name="modulepathitem"></a>  
> &nbsp;&nbsp; IDENTIFIER | `super` | `self` | `Self`  
>  
> [_TypePath_] :<a name="typepath"></a>  
> &nbsp;&nbsp; _TypePathItem_ ( `::` _TypePathItem_ )<sup>*</sup>  
>  
> [_TypePathItem_] :<a name="typepathitem"></a>  
> &nbsp;&nbsp; IDENTIFIER | `super` | `self` | `Self`  
>  

### Patterns

> [_Pattern_] :<a name="pattern"></a><a name="pattern-syntax"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; [_LiteralPattern_]  
> &nbsp;&nbsp; | [_WildcardPattern_]  
> &nbsp;&nbsp; | [_RangePattern_]  
> &nbsp;&nbsp; | [_ReferencePattern_]  
> &nbsp;&nbsp; | [_IdentifierPattern_]  
> &nbsp;&nbsp; | [_BoxPattern_]  
> &nbsp;&nbsp; | [_StructPattern_]  
> &nbsp;&nbsp; | [_TuplePattern_]  
> &nbsp;&nbsp; | [_TupleStructPattern_]  
> &nbsp;&nbsp; | [_SlicePattern_]  
> &nbsp;&nbsp; | [_PathPattern_]  
>  
> [_LiteralPattern_] :<a name="literalpattern"></a><a name="literal-pattern-syntax"></a>  
> &nbsp;&nbsp; `-`<sup>?</sup> ( CHAR_LITERAL | INTEGER_LITERAL | FLOAT_LITERAL )  
>  
> [_WildcardPattern_] :<a name="wildcardpattern"></a><a name="wildcard-pattern-syntax"></a>  
> &nbsp;&nbsp; `_`
>  
> [_RangePattern_] :<a name="rangepattern"></a><a name="reference-pattern-syntax"></a>  
> &nbsp;&nbsp; _Expression_ `...` _Expression_  
>  
> [_ReferencePattern_] :<a name="referencepattern"></a><a name="reference-pattern-syntax"></a>  
> &nbsp;&nbsp; (`&`|`&&`) `mut`<sup>?</sup> _Pattern_  
>  
> [_IdentifierPattern_] :<a name="identifierpattern"></a><a name="identifier-pattern-syntax"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; `mut`<sup>?</sup> IDENTIFIER (`@` [_Pattern_] ) <sup>?</sup>  
> &nbsp;&nbsp; | `ref` `mut`<sup>?</sup> IDENTIFIER (`@` [_Pattern_] ) <sup>?</sup>
>  
> [_BoxPattern_] :<a name="boxpattern"></a><a name="box-pattern-syntax"></a>  
> &nbsp;&nbsp; `box` [_Pattern_]  
>  
> [_StructPattern_] :<a name="structpattern"></a><a name="struct-pattern-syntax"></a>  
> &nbsp;&nbsp; _Path_ `{`  
> &nbsp;&nbsp; &nbsp;&nbsp; _StructPatternElements_ <sup>?</sup>  
> &nbsp;&nbsp; `}`  
>  
> [_StructPatternElements_] :<a name="structpatternelements"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; _StructPatternFields_ (`,` | `,` _StructPatternEtCetera_)<sup>?</sup>  
> &nbsp;&nbsp; | _StructPatternEtCetera_  
>  
> [_StructPatternFields_] :<a name="structpatternfields"></a>  
> &nbsp;&nbsp; _StructPatternField_ (`,` _StructPatternField_) <sup>\*</sup>  
>  
> [_StructPatternField_] :<a name="structpatternfield"></a>  
> &nbsp;&nbsp; _OuterAttribute_ <sup>\*</sup>  
> &nbsp;&nbsp; (  
> &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; INTEGER_LITERAL `:` [_Pattern_]  
> &nbsp;&nbsp; &nbsp;&nbsp; | IDENTIFIER `:` [_Pattern_]  
> &nbsp;&nbsp; &nbsp;&nbsp; | `box`<sup>?</sup> `ref`<sup>?</sup> `mut`<sup>?</sup>
>                                  IDENTIFIER  
> &nbsp;&nbsp; )  
>  
> [_StructPatternEtCetera_] :<a name="structpatternetcetera"></a>  
> &nbsp;&nbsp; _OuterAttribute_ <sup>\*</sup>  
> &nbsp;&nbsp; `..`  
>  
> [_TupleStructPattern_] :<a name="tuplestructpattern"></a><a name="tuplestruct-pattern-syntax"></a>  
> &nbsp;&nbsp; _Path_ `(` _TupleStructItems_ `)`  
>  
> [_TupleStructItems_] :<a name="tuplestructitems"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; [_Pattern_]&nbsp;( `,` [_Pattern_] )<sup>\*</sup> `,`<sup>?</sup>  
> &nbsp;&nbsp; | ([_Pattern_] `,`)<sup>\*</sup> `..` ( (`,` [_Pattern_])<sup>+</sup> `,`<sup>?</sup> )<sup>?</sup>  
>  
> [_TuplePattern_] :<a name="tuplepattern"></a><a name="tuple-pattern-syntax"></a>  
> &nbsp;&nbsp; `(` _TupplePatternItems_<sup>?</sup> `)`  
>  
> [_TuplePatternItems_] :<a name="tuplepatternitems"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; [_Pattern_] `,`  
> &nbsp;&nbsp; | [_Pattern_]&nbsp;(`,` [_Pattern_])<sup>+</sup> `,`<sup>?</sup>  
> &nbsp;&nbsp; | ([_Pattern_] `,`)<sup>\*</sup> `..` ( (`,` [_Pattern_])<sup>+</sup> `,`<sup>?</sup> )<sup>?</sup>  
>  
> [_SlicePattern_] :<a name="slicepattern"></a><a name="slice-pattern-syntax"></a>  
> &nbsp;&nbsp; `[` **FIXME** `]`
>  
> [_PathPattern_] :<a name="pathpattern"></a><a name="path-pattern-syntax"></a>  
> &nbsp;&nbsp; **FIXME**
>  

### Types

> [_Type_] :<a name="type"></a> <a name="type"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; [_TypePath_]  
> &nbsp;&nbsp; | [_QualifiedPathType_]  
> &nbsp;&nbsp; | [_TupleType_]  
> &nbsp;&nbsp; | [_ArrayType_]  
> &nbsp;&nbsp; | [_SliceType_]  
> &nbsp;&nbsp; | [_ReferenceType_]  
> &nbsp;&nbsp; | [_RawPointerType_]  
> &nbsp;&nbsp; | [_BareFunctionType_]  
> &nbsp;&nbsp; | [_NeverType_]  
> &nbsp;&nbsp; | [_TraitObjectType_]  
> &nbsp;&nbsp; | [_ImplTraitType_]  
> &nbsp;&nbsp; | [_ParenthesizedType_]  
> &nbsp;&nbsp; | [_InferredType_]  
>  
> [_TypePath_] :<a name="typepath"></a>  
> &nbsp;&nbsp; [_Path_]  
>  
> [_ParenthesizedType_] :<a name="parenthesizedtype"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; `(` [_Type_] `)`  
> &nbsp;&nbsp; `(` [_Type_] `)` `+` [_TypeBounds_]  
>  
>  
> [_TupleType_] :<a name="tupletype"></a> <a name="tuple-type"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; `(` `)`  
> &nbsp;&nbsp; | `(` [_Type_] `,` `)`  
> &nbsp;&nbsp; | `(` [_Type_]&nbsp;( `,` [_Type_] ) <sup>+</sup> `,`<sup>?</sup> `)`
>  
> [_ArrayType_] :<a name="arraytype"></a> <a name="array-type"></a>  
> &nbsp;&nbsp; `[` [_Type_] `;` [_Expression_] `]`  
>  
> [_SliceType_] :<a name="slicetype"></a> <a name="slice-type"></a>  
> &nbsp;&nbsp; `&` `[` [_Type_] `]`  
>  
> [_NeverType_] :<a name="nevertype"></a> `!`
>  
> [_InferredType_] :<a name="inferredtype"></a> `_`
>  
> [_ReferenceType_] :<a name="referencetype"></a>  
> &nbsp;&nbsp; `&` Lifetime? `mut`? [_TypeNoBounds_]
>  
> [_RawPointerType_] :<a name="rawpointertype"></a>  
> &nbsp;&nbsp; `*` ( `mut` | `const` ) [_TypeNoBounds_]
>  

[_Crate_]: #crate
[_Item_]: #item
[_Generics_]: #generics
[_GenericParams_]: #genericparams
[_LifetimeParams_]: #lifetimeparams
[_LifetimeParam_]: #lifetimeparam
[_TypeParam_]: #typeparam
[_TypeParamBounds_]: #typeparambounds
[_LifetimeBounds_]: #lifetimebounds
[_LateBoundLifetimeDefs_]: #lateboundlifetimedefs
[_WhereClause_]: #whereclause
[_WhereClauseItem_]: #whereclauseitem
[_LifetimeWhereClauseItem_]: #lifetimewhereclauseitem
[_TypeBoundWhereClauseItem_]: #typeboundwhereclauseitem
[_TypeEqualWhereClauseItem_]: #typeequalwhereclauseitem
[_Module_]: #module
[_ExternCrate_]: #externcrate
[_UseDeclaration_]: #usedeclaration
[_UseItems_]: #useitems
[_Function_]: #function
[_FunctionParam_]: #functionparam
[_BlockWithInnerAttributes_]: #blockwithinnerattributes
[_TypeAlias_]: #typealias
[_Struct_]: #struct
[_StructStruct_]: #structstruct
[_TupleStruct_]: #tuplestruct
[_StructFields_]: #structfields
[_StructField_]: #structfield
[_TupleFields_]: #tuplefields
[_TupleField_]: #tuplefield
[_Enumeration_]: #enumeration
[_EnumItems_]: #enumitems
[_EnumItem_]: #enumitem
[_EnumItemTuple_]: #enumitemtuple
[_EnumItemStruct_]: #enumitemstruct
[_EnumItemDiscriminant_]: #enumitemdiscriminant
[_Union_]: #union
[_ConstantItem_]: #constantitem
[_StaticItem_]: #staticitem
[_Trait_]: #trait
[_Implementation_]: #implementation
[_ExternBlock_]: #externblock
[_ExternalItem_]: #externalitem
[_ExternalStaticItem_]: #externalstaticitem
[_ExternalFunctionItem_]: #externalfunctionitem
[_FunctionParametersWithVariadics_]: #functionparameterswithvariadics
[_VariadicFunctionParam_]: #variadicfunctionparam
[_Visibility_]: #visibility
[_Attribute_]: #attribute
[_InnerAttribute_]: #innerattribute
[_OuterAttribute_]: #outerattribute
[_MetaItem_]: #metaitem
[_MetaSeq_]: #metaseq
[_Statement_]: #statement
[_DeclarationStatement_]: #declarationstatement
[_LocalVariablesDeclaration_]: #localvariablesdeclaration
[_ExpressionStatement_]: #expressionstatement
[_ExpressionWithBlock_]: #expressionwithblock
[_Expression_]: #expression
[_LiteralExpression_]: #literalexpression
[_TupleExpression_]: #tupleexpression
[_BlockExpression_]: #blockexpression
[_FieldExpression_]: #fieldexpression
[_TupleIndexingExpression_]: #tupleindexingexpression
[_ClosureExpression_]: #closureexpression
[_ArrayExpression_]: #arrayexpression
[_IndexExpression_]: #indexexpression
[_RangeExpression_]: #rangeexpression
[_RangeExpr_]: #rangeexpr
[_RangeFromExpr_]: #rangefromexpr
[_RangeToExpr_]: #rangetoexpr
[_RangeFullExpr_]: #rangefullexpr
[_OperatorExpression_]: #operatorexpression
[_BorrowExpression_]: #borrowexpression
[_DereferenceExpression_]: #dereferenceexpression
[_ErrorPropagationExpression_]: #errorpropagationexpression
[_NegationExpression_]: #negationexpression
[_ArithmeticOrLogicalExpression_]: #arithmeticorlogicalexpression
[_ComparisonExpression_]: #comparisonexpression
[_LazyBooleanExpression_]: #lazybooleanexpression
[_TypeCastExpression_]: #typecastexpression
[_AssignmentExpression_]: #assignmentexpression
[_CompoundAssignmentExpression_]: #compoundassignmentexpression
[_GroupedExpression_]: #groupedexpression
[_LoopExpression_]: #loopexpression
[_InfiniteLoopExpression_]: #infiniteloopexpression
[_InfiniteLoopExpression_]: #infiniteloopexpression
[_PredicateLoopExpression_]: #predicateloopexpression
[_IteratorLoopExpression_]: #iteratorloopexpression
[_LoopLabel_]: #looplabel
[_BreakExpression_]: #breakexpression
[_ContinueExpression_]: #continueexpression
[_IfExpression_]: #ifexpression
[_MatchExpression_]: #matchexpression
[_MatchArm_]: #matcharm
[_MatchArmPatterns_]: #matcharmpatterns
[_MatchArmGuard_]: #matcharmguard
[_IfLetExpression_]: #ifletexpression
[_WhileLetExpression_]: #whileletexpression
[_ReturnExpression_]: #returnexpression
[_Path_]: #path
[_NonGlobalPath_]: #nonglobalpath
[_GlobalPath_]: #globalpath
[_PathSegment_]: #pathsegment
[_PathParameter_]: #pathparameter
[_ModulePath_]: #modulepath
[_ModulePathItem_]: #modulepathitem
[_TypePath_]: #typepath
[_TypePathItem_]: #typepathitem
[_Pattern_]: #pattern
[_LiteralPattern_]: #literalpattern
[_WildcardPattern_]: #wildcardpattern
[_RangePattern_]: #rangepattern
[_ReferencePattern_]: #referencepattern
[_IdentifierPattern_]: #identifierpattern
[_BoxPattern_]: #boxpattern
[_StructPattern_]: #structpattern
[_StructPatternElements_]: #structpatternelements
[_StructPatternFields_]: #structpatternfields
[_StructPatternField_]: #structpatternfield
[_StructPatternEtCetera_]: #structpatternetcetera
[_TupleStructPattern_]: #tuplestructpattern
[_TupleStructItems_]: #tuplestructitems
[_TuplePattern_]: #tuplepattern
[_TuplePatternItems_]: #tuplepatternitems
[_SlicePattern_]: #slicepattern
[_PathPattern_]: #pathpattern
[_Type_]: #type
[_TypePath_]: #typepath
[_ParenthesizedType_]: #parenthesizedtype
[_TupleType_]: #tupletype
[_ArrayType_]: #arraytype
[_SliceType_]: #slicetype
[_NeverType_]: #nevertype
[_InferredType_]: #inferredtype
[_ReferenceType_]: #referencetype
[_RawPointerType_]: #rawpointertype