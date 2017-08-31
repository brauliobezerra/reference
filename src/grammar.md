# Grammar

## Lexical productions


### Keywords

> KW_AS             : `as`  
> KW_BOX            : `box`  
> KW_BREAK          : `break`  
> KW_CONST          : `const`  
> KW_CONTINUE       : `continue`  
> KW_CRATE          : `crate`  
> KW_ELSE           : `else`  
> KW_ENUM           : `enum`  
> KW_EXTERN         : `extern`  
> KW_FALSE          : `false`  
> KW_FN             : `fn`  
> KW_FOR            : `for`  
> KW_IF             : `if`  
> KW_IMPL           : `impl`  
> KW_IN             : `in`  
> KW_LET            : `let`  
> KW_LOOP           : `loop`  
> KW_MATCH          : `match`  
> KW_MOD            : `mod`  
> KW_MOVE           : `move`  
> KW_MUT            : `mut`  
> KW_PUB            : `pub`  
> KW_REF            : `ref`  
> KW_RETURN         : `return`  
> KW_SELFVALUE      : `self`  
> KW_SELFTYPE       : `Self`  
> KW_STATIC         : `static`  
> KW_STRUCT         : `struct`  
> KW_SUPER          : `super`  
> KW_TRAIT          : `trait`  
> KW_TRUE           : `true`  
> KW_TYPE           : `type`  
> KW_UNSAFE         : `unsafe`  
> KW_USE            : `use`  
> KW_WHERE          : `wher`  
> KW_WHILE          : `while`  
>  
> KW_CATCH          : `catch`  
> KW_DEFAULT        : `default`  
> KW_UNION          : `union`  
> KW_STATICLIFETIME : `'static`  
>  
> KW_ABSTRACT       : `abstract`  
> KW_ALIGNOF        : `alignof`  
> KW_BECOME         : `become`  
> KW_DO             : `do`  
> KW_FINAL          : `final`  
> KW_MACRO          : `macro`  
> KW_OFFSETOF       : `offsetof`  
> KW_OVERRIDE       : `override`  
> KW_PRIV           : `priv`  
> KW_PROC           : `proc`  
> KW_PURE           : `pure`  
> KW_SIZEOF         : `sizeof`  
> KW_TYPEOF         : `typeof`  
> KW_UNSIZED        : `unsized`  
> KW_VIRTUAL        : `virtual`  
> KW_YIELD          : `yield`  

### Identifiers

> IDENTIFIER :  
> &nbsp;&nbsp; &nbsp;&nbsp; XID_start XID_continue<sup>\*</sup>  
> &nbsp;&nbsp; | `_` XID_continue<sup>+</sup>  
>  

### Comments

> LINE_COMMENT :  
> &nbsp;&nbsp; &nbsp;&nbsp; `//` (~[`/` `!`] | `//`) ~`\n`<sup>\*</sup>  
> &nbsp;&nbsp; | `//`
>  
> BLOCK_COMMENT :  
> &nbsp;&nbsp; &nbsp;&nbsp; `/*` (~[`*` `!`] | `**` | _BlockCommentOrDoc_)
>      (_BlockCommentOrDoc_ | ~`*/`)<sup>\*</sup> `*/`  
> &nbsp;&nbsp; | `/**/`  
> &nbsp;&nbsp; | `/***/`  
>  
> OUTER_LINE_DOC :  
> &nbsp;&nbsp; `//!` ~[`\n` _IsolatedCR_]<sup>\*</sup>  
>  
> OUTER_BLOCK_DOC :  
> &nbsp;&nbsp; `/*!` ( _BlockCommentOrDoc_ | ~[`*/` _IsolatedCR_] )<sup>\*</sup> `*/`  
>  
> INNER_LINE_DOC :  
> &nbsp;&nbsp; `///` (~`/` ~[`\n` _IsolatedCR_]<sup>\*</sup>)<sup>?</sup>  
>  
> INNER_BLOCK_DOC :  
> &nbsp;&nbsp; `/**` (~`*` | _BlockCommentOrDoc_ )
>              (_BlockCommentOrDoc_ | ~[`*/` _IsolatedCR_])<sup>\*</sup> `*/`  
>  
> _BlockCommentOrDoc_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; BLOCK_COMMENT  
> &nbsp;&nbsp; | OUTER_BLOCK_DOC  
> &nbsp;&nbsp; | INNER_BLOCK_DOC  
>  
> _IsolatedCR_ :  
> &nbsp;&nbsp; _A `\r` not followed by a `\n`_  
>  

### Crates and source files

> UTF8BOM : `\uFEFF`  
> SHEBANG : `#!` ~[`[` `\n`] ~`\n`<sup>\*</sup>
>  


## Syntactical productions


### Crates and source files

> _Crate_ :  
> &nbsp;&nbsp; UTF8BOM<sup>?</sup>  
> &nbsp;&nbsp; SHEBANG<sup>?</sup>  
> &nbsp;&nbsp; [_InnerAttribute_]<sup>\*</sup>  
> &nbsp;&nbsp; [_Item_]<sup>\*</sup>  
>  

### Visibility and Privacy

> _Visibility_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; EMPTY  
> &nbsp;&nbsp; | `pub`  
> &nbsp;&nbsp; | `pub` `(` `crate` `)`  
> &nbsp;&nbsp; | `pub` `(` `in` _ModulePath_ `)`  
> &nbsp;&nbsp; | `pub` `(` `in`<sup>?</sup> `self` `)`  
> &nbsp;&nbsp; | `pub` `(` `in`<sup>?</sup> `super` `)`  
>  

### Attributes

> _Attribute_ :  
> &nbsp;&nbsp; _InnerAttribute_ | _OuterAttribute_  
>  
> _InnerAttribute_ :  
> &nbsp;&nbsp; `#![` MetaItem `]`  
>   
> _OuterAttribute_ :  
> &nbsp;&nbsp; `#[` MetaItem `]`  
>   
> _MetaItem_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; IDENTIFIER  
> &nbsp;&nbsp; | IDENTIFIER `=` LITERAL  
> &nbsp;&nbsp; | IDENTIFIER `(` _MetaSeq_ `)`  
> &nbsp;&nbsp; | IDENTIFIER `(` _MetaSeq_ `,` `)`  
>   
> _MetaSeq_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; EMPTY  
> &nbsp;&nbsp; | _MetaItem_  
> &nbsp;&nbsp; | _MetaSeq_ `,` _MetaItem_  
>