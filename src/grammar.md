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
> INTEGER_LITERAL :  
> &nbsp;&nbsp; &nbsp;&nbsp; `0x` [`0`-`9` `a`-`f` `A`-`F` `_`]<sup>+</sup> INTEGER_SUFFIX<sup>?</sup>  
> &nbsp;&nbsp; | `0o` [`0`-`7` `_`]<sup>+</sup> INTEGER_SUFFIX<sup>?</sup>  
> &nbsp;&nbsp; | `0b` [`0` `1` `_`]<sup>+</sup> INTEGER_SUFFIX<sup>?</sup>  
> &nbsp;&nbsp; | [`0`-`9`][`0`-`9` `_`]<sup>\*</sup> INTEGER_SUFFIX<sup>?</sup>  
>   
> INTEGER_SUFFIX :  
> &nbsp;&nbsp; &nbsp;&nbsp; `u8` | `u16` | `u32` | `u64` | `usize`  
> &nbsp;&nbsp; | `i8` | `u16` | `i32` | `i64` | `usize`
>  
> FLOAT_LITERAL :  
> &nbsp;&nbsp; &nbsp;&nbsp; [`0`-`9`][`0`-`9` `_`]<sup>\*</sup> `.` [`0`-`9` `_`]<sup>\*</sup>  
> &nbsp;&nbsp; | [`0`-`9`][`0`-`9` `_`]<sup>\*</sup> `.` [`0`-`9` `_`]<sup>+</sup>
>                FLOAT_EXPONENT<sup>?</sup> FLOAT_SUFFIX  
> &nbsp;&nbsp; | [`0`-`9`][`0`-`9` `_`]<sup>\*</sup> FLOAT_EXPONENT<sup>?</sup>
>                FLOAT_SUFFIX<sup>?</sup>  
>  
> FLOAT_EXPONENT :  
> &nbsp;&nbsp; (`e`|`E`) [`0`-`9` `_`]<sup>+</sup>   
>  
> FLOAT_SUFFIX :  
> &nbsp;&nbsp; `f32` | `f64`
>  
> BOOLEAN_LITERAL :  
> &nbsp;&nbsp; &nbsp;&nbsp; `true`  
> &nbsp;&nbsp; | `false`  
>  
> EQ            : `=`  
> LT            : `<`  
> LE            : `<=`  
> EQEQ          : `==`  
> NE            : `!=`  
> GE            : `>=`  
> GT            : `>`  
> ANDAND        : `&&`  
> OROR          : `||`  
> NOT           : `!`  
> TILDE         : `~`  
>  
> AT            : `@`  
> DOT           : `.`  
> DOTDOT        : `..`  
> DOTDOTDOT     : `...`  
> COMMA         : `,`  
> SEMI          : `;`  
> COLON         : `:`  
> MOD_SEPARATOR : `::`  
> RIGHT_ARROW   : `->`  
> LEFT_ARROW    : `<-`  
> FAT_ARROW     : `=>`  
> POUND         : `#`  
> DOLLAR        : `$`  
> QUESTION      : `?`  
>  
> OPEN_PAREN    : `(`  
> CLOSE_PAREN   : `)`  
> OPEN_BRACKET  : `[`  
> CLOSE_BRACKET : `]`  
> OPEN_BRACE    : `{`  
> CLOSE_BRACE   : `}`  
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
> [_Generics_] :<a name="generics"></a>  
> &nbsp;&nbsp; `<` _GenericParams_<sup>?</sup> `>`  
>  
> _GenericParams_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; _LifetimeParams_ `,`<sup>?</sup>  
> &nbsp;&nbsp; | _TypeParams_ `,`<sup>?</sup>  
> &nbsp;&nbsp; | _LifetimeParams_ `,` _TypeParams_ `,`<sup>?</sup>  
>  
> _LifetimeParams_ :  
> &nbsp;&nbsp; _LifetimeParam_ (`,` _LifetimeParam_)<sup>\*</sup>  
>  
> _LifetimeParam_ :  
> &nbsp;&nbsp; [LIFETIME_OR_LABEL] _LifetimeBounds_<sup>?</sup>  
>  
> _TypeParams_:  
> &nbsp;&nbsp; _TypeParam_ (`,` _TypeParam_)<sup>\*</sup>  
>  
> _TypeParam_ :  
> &nbsp;&nbsp; [IDENTIFIER] _TypeParamBounds_<sup>?</sup> ( `=` [_Type_] )<sup>?</sup>  
>  
> _TypeParamBounds_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; [LIFETIME_OR_LABEL]  
> &nbsp;&nbsp; | `(` [LIFETIME_OR_LABEL] `)`  
> &nbsp;&nbsp; | `?`<sup>?</sup> _LateBoundLifetimeDefs_<sup>?</sup> [_TypePath_]  
> &nbsp;&nbsp; | `(` `?`<sup>?</sup> _LateBoundLifetimeDefs_<sup>?</sup> [_TypePath_] `)`  
>  
> _LifetimeBounds_ :  
> &nbsp;&nbsp; `:` [LIFETIME_OR_LABEL] ( `+` [LIFETIME_OR_LABEL] ) `+`<sup>?</sup>  
>  
> _LateBoundLifetimeDefs_ :  
> &nbsp;&nbsp; `for` `<` _LifetimeParams_ `,`<sup>?</sup> `>`
>  
> [_WhereClause_] :<a name="where-clause"></a>  
> &nbsp;&nbsp; `where` ( _WhereClauseItem_ ( `,` _WhereClauseItem_ )<sup>\*</sup> `,`<sup>?</sup> )<sup>?</sup>  
>  
> _WhereClauseItem_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; _LifetimeWhereClauseItem_  
> &nbsp;&nbsp; | _TypeBoundWhereClauseItem_  
> &nbsp;&nbsp; | _TypeEqualWhereClauseItem_  
>  
> _LifetimeWhereClauseItem_ :  
> &nbsp;&nbsp; [LIFETIME_OR_LABEL] _LifetimeBounds_  
>  
> _TypeBoundWhereClauseItem_ :  
> &nbsp;&nbsp; _LateBoundLifetimeDefs_<sup>?</sup> [_Type_] `:` _TypeParamBounds_  
>  
> _TypeEqualWhereClauseItem_ :  
> &nbsp;&nbsp; _LateBoundLifetimeDefs_<sup>?</sup> [_Type_]&nbsp;(`=`|`==`) [_Type_]  
>  
> [_Module_] :  
> &nbsp;&nbsp; &nbsp;&nbsp; `mod` [IDENTIFIER] `;`  
> &nbsp;&nbsp; | `mod` [IDENTIFIER] `{`  
> &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [_InnerAttribute_]<sup>\*</sup>  
> &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [_Item_]<sup>\*</sup>  
> &nbsp;&nbsp; &nbsp;&nbsp; `}`  
>  
> [_ExternCrate_] :  
> &nbsp;&nbsp; `extern` `crate` [IDENTIFIER] (`as` [IDENTIFIER])<sup>?</sup> `;`
>  
> _UseDeclaration_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; `use` `::`<sup>?</sup> [_NonGlobalPath_]  
> &nbsp;&nbsp; | `use` `::`<sup>?</sup> [_NonGlobalPath_] `as` [IDENTIFIER]  
> &nbsp;&nbsp; | `use` `::`<sup>?</sup> [_NonGlobalPath_] `::` `*`  
> &nbsp;&nbsp; | `use` `::`<sup>?</sup> [_NonGlobalPath_] `::` `{` _UseItems_ `}`  
> &nbsp;&nbsp; | `use` `::`<sup>?</sup> `{` _UseItems_ `}`  
>  
> _UseItems_ :  
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
> &nbsp;&nbsp; `(` `)`  
>  
> _FunctionReturnType_:  
> &nbsp;&nbsp; `->` [_Type_]  
>  
> _BlockWithInnerAttributes_ :  
> &nbsp;&nbsp; `{`  
> &nbsp;&nbsp; &nbsp;&nbsp; [_InnerAttribute_]<sup>\*</sup>  
> &nbsp;&nbsp; &nbsp;&nbsp; [_Statement_]<sup>\*</sup>  
> &nbsp;&nbsp; `}`  
>  
> [_TypeAlias_] : FIXME
>  
> [_Struct_] :  
> &nbsp;&nbsp; &nbsp;&nbsp; _StructStruct_  
> &nbsp;&nbsp; | _TupleStruct_  
>  
> _StructStruct_ :  
> &nbsp;&nbsp; `struct`
>   [IDENTIFIER]&nbsp;
>   [_Generics_]<sup>?</sup>
>   [_WhereClause_]<sup>?</sup>
>   ( `{` _StructFields_<sup>?</sup> `}` | `;` )  
>  
> _TupleStruct_ :  
> &nbsp;&nbsp; `struct`
>   [IDENTIFIER]&nbsp;
>   [_Generics_]<sup>?</sup>
>   `(` _TupleFields_<sup>?</sup> `)`
>   [_WhereClause_]<sup>?</sup>
>   `;`  
>  
> [_StructFields_] :<a name="struct-fields"></a>  
> &nbsp;&nbsp; _StructField_ (`,` _StructField_)<sup>\*</sup> `,`<sup>?</sup>  
>  
> _StructField_ :  
> &nbsp;&nbsp; [_OuterAttribute_]<sup>\*</sup>  
> &nbsp;&nbsp; [_Visibility_]<sup>?</sup>  
> &nbsp;&nbsp; [IDENTIFIER] `:` [_Type_]  
>  
> [_TupleFields_] :<a name="tuple-fields"></a>  
> &nbsp;&nbsp; _TupleField_ (`,` _TupleField_)<sup>\*</sup> `,`<sup>?</sup>  
>  
> _TupleField_ :  
> &nbsp;&nbsp; [_OuterAttribute_]<sup>\*</sup>  
> &nbsp;&nbsp; [_Visibility_]<sup>?</sup>  
> &nbsp;&nbsp; [_Type_]  
>  
> [_Enumeration_] :  
> &nbsp;&nbsp; `enum`
>    [IDENTIFIER]&nbsp;
>    [_Generics_]<sup>?</sup>
>    [_WhereClause_]<sup>?</sup>
>    `{` _EnumItems_<sup>?</sup> `}`  
>  
> _EnumItems_ :  
> &nbsp;&nbsp; _EnumItem_ ( `,` _EnumItem_ )<sup>\*</sup> `,`<sup>?</sup>  
>  
> _EnumItem_ :  
> &nbsp;&nbsp; _OuterAttribute_<sup>\*</sup>  
> &nbsp;&nbsp; [IDENTIFIER]&nbsp;( _EnumItemTuple_ | _EnumItemStruct_ 
>                                | _EnumItemWithDiscriminant_ )<sup>?</sup>  
>  
> _EnumItemTuple_ :  
> &nbsp;&nbsp; `(` [_TupleFields_]<sup>?</sup> `)`  
>   
> _EnumItemStruct_ :  
> &nbsp;&nbsp; `(` [_StructFields_]<sup>?</sup> `)`  
>   
> _EnumItemWithDiscriminant_ :  
> &nbsp;&nbsp; `=` [_Expression_]  
>  
> [_Union_] :  
> &nbsp;&nbsp; `union` [_Generics_]<sup>?</sup> [_WhereClause_]<sup>?</sup>
>   `{`[_StructFields_] `}`
>  
> [_ConstantItem_] : FIXME `const`
>  
> [_StaticItem_] : FIXME
>  
> _Trait_ :  
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
> [_Implementation_] :  
> `unsafe`? `impl` [_Generics_] (`!`? _TraitName_ `for`)? (_TypeName_ | `..`) `{`  
> &nbsp;&nbsp; _InnerAttributes?_  
> &nbsp;&nbsp; _ImplementationItems?_  
> `}`
>  
> [_ExternBlock_] : `extern` FIXME
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

### Statements

> _Statement_ :  
> &nbsp;&nbsp; [_DeclarationStatement_] | [_Expression_] | `;`  
>  
> _DeclarationStatement_ :  
> &nbsp;&nbsp; [_Item_] | [_LocalVariablesDeclaration_]
>  
> _LocalVariablesDeclaration_ :  
> &nbsp;&nbsp; `let` [_Pattern_]&nbsp;( `:` [_Type_] )<sup>?</sup> (`=` [_Expression_] )<sup>?</sup> `;`
>  
> _ExpressionStatement_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; _ExpressionWithBlock_  
> &nbsp;&nbsp; | _ExpressionWithoutBlock_ `;`  
>  
> _ExpressionWithBlock_ :  
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

> [_Expression_] :  
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
> [_LiteralExpression_] :  
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
> _TupleExpression_ :  
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
> _BlockExpression_ :  
> &nbsp;&nbsp; `{`  
> &nbsp;&nbsp; &nbsp;&nbsp; [_InnerAttribute_]*  
> &nbsp;&nbsp; &nbsp;&nbsp; [_Statement_]*  
> &nbsp;&nbsp; `}`  
>  
> FIXME
>  
> FIXME
>  
> _FieldExpression_ :  
> &nbsp;&nbsp; [_Expression_] `.` [IDENTIFIER]
>  
> _TupleIndexingExpression_ :  
> &nbsp;&nbsp; [_Expression_] `.` [DECIMAL_LITERAL]
>  
> FIXME
>  
> [_ClosureExpression_] :  
> &nbsp;&nbsp; &nbsp;&nbsp; `move`<sup>?</sup> `|` ParameterList<sup>?</sup> `|`
>                           [_Expression_]  
> &nbsp;&nbsp; | `move`<sup>?</sup> `|` ParameterList<sup>?</sup> `|` `->` _Type_
>                [_BlockExpression_]  
>  
> [_ArrayExpression_] :  
> &nbsp;&nbsp; &nbsp;&nbsp; `[`  `]`  
> &nbsp;&nbsp; | `[` [_Expression_] ( `,` [_Expression_] )<sup>\*</sup> `,`<sup>?</sup> `]`  
> &nbsp;&nbsp; | `[` [_Expression_] `;` [_Expression_] `]`  
>  
> [_IndexExpression_] :  
> &nbsp;&nbsp; [_Expression_] `[` [_Expression_] `]`
>  
> _RangeExpression_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; _RangeExpr_  
> &nbsp;&nbsp; | _RangeFromExpr_  
> &nbsp;&nbsp; | _RangeToExpr_  
> &nbsp;&nbsp; | _RangeFullExpr_  
>  
> _RangeExpr_ :  
> &nbsp;&nbsp; [_Expression_] `..` [_Expression_]  
>  
> _RangeFromExpr_ :  
> &nbsp;&nbsp; [_Expression_] `..`  
>  
> _RangeToExpr_ :  
> &nbsp;&nbsp; `..` [_Expression_]  
>  
> _RangeFullExpr_ :  
> &nbsp;&nbsp; `..`  
>  
> _OperatorExpression_ :  
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
> _BorrowExpression_ :   
> &nbsp;&nbsp; &nbsp;&nbsp; `&` [_Expression_]  
> &nbsp;&nbsp; | `&` `mut` [_Expression_]  
>  
> _DereferenceExpression_ :  
> &nbsp;&nbsp; `*` [_Expression_]
>  
> _ErrorPropagationExpression_ :  
> &nbsp;&nbsp; [_Expression_] `?`  
>  
> _NegationExpression_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; `-` [_Expression_]  
> &nbsp;&nbsp; | `!` [_Expression_]  
>  
> _ArithmeticOrLogicalExpression_ :  
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
> _ComparisonExpression_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; [_Expression_] `==` [_Expression_]  
> &nbsp;&nbsp; | [_Expression_] `!=` [_Expression_]  
> &nbsp;&nbsp; | [_Expression_] `>` [_Expression_]  
> &nbsp;&nbsp; | [_Expression_] `<` [_Expression_]  
> &nbsp;&nbsp; | [_Expression_] `>=` [_Expression_]  
> &nbsp;&nbsp; | [_Expression_] `<=` [_Expression_]  
>  
> _LazyBooleanExpression_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; [_Expression_] `||` [_Expression_]  
> &nbsp;&nbsp; | [_Expression_] `&&` [_Expression_]
>  
> _TypeCastExpression_ :  
> &nbsp;&nbsp; [_Expression_] `as` [IDENTIFIER]
>  
> _AssignmentExpression_ :  
> &nbsp;&nbsp; | [_Expression_] `=` [_Expression_]  
>  
> _CompoundAssignmentExpression_ :  
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
> _GroupedExpression_ :  
> &nbsp;&nbsp; `(` [_Expression_] `)`
>  
> _LoopExpression_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; _LoopLabel_<sup>?</sup> (
> [_InfiniteLoopExpression_](#infinite-loops)
> | [_PredicateLoopExpression_](#predicate-loops)
> | [_IteratorLoopExpression_](#iterator-loops)
> )  
>  
> _InfiniteLoopExpression_ :  
> &nbsp;&nbsp; `loop` [_BlockExpression_]
>  
> _PredicateLoopExpression_ :  
> &nbsp;&nbsp; `while` [_Expression_]&nbsp;[_BlockExpression_]
>  
> _IteratorLoopExpression_ :  
> &nbsp;&nbsp; `for` [IDENTIFIER] `in` [_Expression_]&nbsp;[_BlockExpression_]
>  
> _LoopLabel_ :  
> &nbsp;&nbsp; LIFETIME_OR_LABEL `:`
>  
> _BreakExpression_ :  
> &nbsp;&nbsp; `break` LIFETIME_OR_LABEL<sup>?</sup> [_Expression_]<sup>?</sup>
>  
> _ContinueExpression_ :  
> &nbsp;&nbsp; `continue` LIFETIME_OR_LABEL<sup>?</sup>
>  
> [_IfExpression_] :  
> &nbsp;&nbsp; `if` [_Expression_]&nbsp;[_BlockExpression_]  
> &nbsp;&nbsp; (`else` (
>   [_BlockExpression_]
> | [_IfExpression_]
> | [_IfLetExpression_] ) )<sup>\?</sup>  
>  
> [_MatchExpression_] :  
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
> _MatchArm_ :  
> &nbsp;&nbsp; [_OuterAttribute_]<sup>\*</sup> _MatchArmPatterns_ _MatchArmGuard_
>  
> _MatchArmPatterns_ :  
> &nbsp;&nbsp; [_Pattern_] ( `|` [_Pattern_] )<sup>*</sup>  
>  
> _MatchArmGuard_ :  
> &nbsp;&nbsp; `if` [_Expression_]  
>  
> [_IfLetExpression_] :  
> &nbsp;&nbsp; `if` `let` [_Pattern_] `=` [_Expression_]&nbsp;[_BlockExpression_]  
> &nbsp;&nbsp; (`else` (
>   [_BlockExpression_]
> | [_IfExpression_]
> | [_IfLetExpression_] ) )<sup>\?</sup>  
>  
> [_WhileLetExpression_] :  
> &nbsp;&nbsp; `while` `let` [_Pattern_] `=` [_Expression_]&nbsp;[_BlockExpression_]  
>  
> [_ReturnExpression_] :  
> &nbsp;&nbsp; &nbsp;&nbsp; `return`  
> &nbsp;&nbsp; | `return` [_Expression_]  
>  

### Paths

> [_Path_] :  
> &nbsp;&nbsp; &nbsp;&nbsp; [_NonGlobalPath_]  
> &nbsp;&nbsp; | [_GlobalPath_]  
>  
> [_NonGlobalPath_] : <a name="nonglobal-path"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; [_PathSegment_] ( `::` [_NonGlobalPath_] )<sup>?</sup>  
>  
> [_GlobalPath_] : <a name="global-path"></a>  
> &nbsp;&nbsp; `::` [_NonGlobalPath_]  
>  
> [_PathSegment_] : <a name="path-segment"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; [IDENTIFIER]  
> &nbsp;&nbsp; | `<` _TypeArguments_ `>`  
> &nbsp;&nbsp; | `super`  
> &nbsp;&nbsp; | `self`  
>  
> _PathParameter_ :  
>  
>  
> _ModulePath_ :  
> &nbsp;&nbsp; _ModulePathItem_ ( `::` _ModulePathItem_ )<sup>*</sup>  
>  
> _ModulePathItem_ :  
> &nbsp;&nbsp; IDENTIFIER | `super` | `self` | `Self`  
>  
> _TypePath_ :  
> &nbsp;&nbsp; _TypePathItem_ ( `::` _TypePathItem_ )<sup>*</sup>  
>  
> _TypePathItem_ :  
> &nbsp;&nbsp; IDENTIFIER | `super` | `self` | `Self`  
>  

### Patterns

> _Pattern_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; [_WildcardPattern_]  
> &nbsp;&nbsp; | [_ReferencePattern_]  
> &nbsp;&nbsp; | [_StructPattern_]  
> &nbsp;&nbsp; | [_TupleStructPattern_]  
> &nbsp;&nbsp; | [_SlicePattern_]  
> &nbsp;&nbsp; | [_IdentifierPattern_]  
> &nbsp;&nbsp; | [_PathPattern_]  
> &nbsp;&nbsp; | [_LiteralPattern_]  
> &nbsp;&nbsp; | [_RangePattern_]  
> &nbsp;&nbsp; | [_BoxPattern_]  
>  
> _WildcardPattern_ :  
> &nbsp;&nbsp; `_`
>  
> _ReferencePattern_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; (`&`|`&&`) _Pattern_  
> &nbsp;&nbsp; | (`&`|`&&`) _Mutability_ _Pattern_  
>  
> _TupleStructPattern_ :  
> &nbsp;&nbsp; **FIXME**
>  
> _SlicePattern_ :  
> &nbsp;&nbsp; **FIXME**
>  
> _IdentifierPattern :  
> &nbsp;&nbsp; &nbsp;&nbsp; `mut` IDENTIFIER  
> &nbsp;&nbsp; | `mut` IDENTIFIER `@` _Pattern_  
> &nbsp;&nbsp; | `ref` IDENTIFIER `@` _Pattern_  
>  
> _PathPattern_ :  
> &nbsp;&nbsp; **FIXME**
>  
> _LiteralPattern_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; LITERAL  
> &nbsp;&nbsp; | `-` LITERAL  
>  
> _RangePattern_ :  
> &nbsp;&nbsp; **FIXME**
>  
> _BoxPattern_ :  
> &nbsp;&nbsp; **FIXME**
>  

### Types

> [_Type_] : <a name="type"></a>  
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
> [_TypePath_] :  
> &nbsp;&nbsp; [_Path_]  
>  
> [_ParenthesizedType_] :  
> &nbsp;&nbsp; &nbsp;&nbsp; `(` [_Type_] `)`  
> &nbsp;&nbsp; `(` [_Type_] `)` `+` [_TypeBounds_]  
>  
>  
> [_TupleType_] : <a name="tuple-type"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; `(` `)`  
> &nbsp;&nbsp; | `(` [_Type_] `,` `)`  
> &nbsp;&nbsp; | `(` [_Type_]&nbsp;( `,` [_Type_] ) <sup>+</sup> `,`<sup>?</sup> `)`
>  
> [_ArrayType_] : <a name="array-type"></a>  
> &nbsp;&nbsp; `[` [_Type_] `;` [_Expression_] `]`  
>  
> [_SliceType_] : <a name="slice-type"></a>  
> &nbsp;&nbsp; `&` `[` [_Type_] `]`  
>  
> [_NeverType_] : `!`
>  
> [_InferredType_] : `_`
>  
> [_ReferenceType_] :  
> &nbsp;&nbsp; `&` Lifetime? `mut`? [_TypeNoBounds_]
>  
> [_RawPointerType_] :  
> &nbsp;&nbsp; `*` ( `mut` | `const` ) [_TypeNoBounds_]
>