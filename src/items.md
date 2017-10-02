# Items

> **<sup>Syntax:<sup>**  
> _Item_:  
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

An _item_ is a component of a crate. Items are organized within a crate by a
nested set of [modules]. Every crate has a single "outermost" anonymous module;
all further items within the crate have [paths] within the module tree of the
crate.

[modules]: items/modules.html
[paths]: paths.html

Items are entirely determined at compile-time, generally remain fixed during
execution, and may reside in read-only memory.

There are several kinds of items:

* [modules](items/modules.html)
* [`extern crate` declarations](items/extern-crates.html)
* [`use` declarations](items/use-declarations.html)
* [function definitions](items/functions.html)
* [type definitions](items/type-aliases.html)
* [struct definitions](items/structs.html)
* [enumeration definitions](items/enumerations.html)
* [union definitions](items/unions.html)
* [constant items](items/constant-items.html)
* [static items](items/static-items.html)
* [trait definitions](items/traits.html)
* [implementations](items/implementations.html)
* [`extern` blocks](items/external-blocks.html)

Some items form an implicit scope for the declaration of sub-items. In other
words, within a function or module, declarations of items can (in many cases)
be mixed with the statements, control blocks, and similar artifacts that
otherwise compose the item body. The meaning of these scoped items is the same
as if the item was declared outside the scope &mdash; it is still a static item
&mdash; except that the item's *path name* within the module namespace is
qualified by the name of the enclosing item, or is private to the enclosing
item (in the case of functions). The grammar specifies the exact locations in
which sub-item declarations may appear.

## Type Parameters

> **<sup>Syntax:<sup>**  
> _Generics_ :<a name="generics"></a>  
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
> &nbsp;&nbsp; `:` [LIFETIME_OR_LABEL]&nbsp;( `+` [LIFETIME_OR_LABEL] )<sup>\*</sup> `+`<sup>?</sup>  
>  
> _LateBoundLifetimeDefs_ :  
> &nbsp;&nbsp; `for` `<` _LifetimeParams_ `,`<sup>?</sup> `>`

> **<sup>Syntax:<sup>**  
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

Functions, type aliases, structs, enumerations, unions, traits and
implementations may be *parameterized* by type. Type parameters are given as a
comma-separated list of identifiers enclosed in angle brackets (`<...>`), after
the name of the item (except for implementations, where they come directly
after `impl`) and before its definition.

The type parameters of an item are considered "part of the name", not part of
the type of the item. A referencing [path] must (in principle) provide type
arguments as a list of comma-separated types enclosed within angle brackets, in
order to refer to the type-parameterized item. In practice, the type-inference
system can usually infer such argument types from context. There are no general
type-parametric types, only type-parametric items. That is, Rust has no notion
of type abstraction: there are no higher-ranked (or "forall") types abstracted
over other types, though higher-ranked types do exist for lifetimes.

[path]: paths.html

[_InnerAttribute_]: attributes.html
[_OuterAttribute_]: attributes.html

[IDENTIFIER]: identifiers.html
[_Statement_]: statements.html
[LIFETIME_OR_LABEL]: tokens.html#symbols
[_Visibility_]: visibility-and-privacy.html
[_Expression_]: expressions.html

[_NonGlobalPath_]: paths.html#nonglobal-path

[_Generics_]: #generics
[_WhereClause_]: #where-clause
[_Type_]: types.html#type
[_TypePath_]: types.html#type-path

[_Module_]:         items/modules.html
[_ExternCrate_]:    items/extern-crates.html
[_UseDeclaration_]: items/use-declarations.html
[_Function_]:       items/functions.html
[_TypeAlias_]:      items/type-aliases.html
[_Struct_]:         items/structs.html
[_Enumeration_]:    items/enumerations.html
[_Union_]:          items/unions.html
[_ConstantItem_]:   items/constant-items.html
[_StaticItem_]:     items/static-items.html
[_Trait_]:          items/traits.html
[_Implementation_]: items/implementations.html
[_ExternBlock_]:    items/external-blocks.html
