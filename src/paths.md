# Paths

<!-- FIXME: UFCS - universal function call syntax -->

A _path_ is a sequence of one or more path components _logically_ separated by
namespace qualifiers (`::`). If a path consists of only one component, it may
refer to either an [item] or a [variable] in a local control
scope. If a path has multiple components, it refers to an item.

Every item has a _canonical path_ within its crate, but the path naming an item
is only meaningful within a given crate. There is no global namespace across
crates; an item's canonical path merely identifies it within the crate.

Two examples of simple paths consisting of only identifier components:

```rust,ignore
x;
x::y::z;
```

Path components are usually [identifiers], but they may
also include angle-bracket-enclosed lists of type arguments. In
[expression] context, the type argument list is given
after a `::` namespace qualifier in order to disambiguate it from a
relational expression involving the less-than symbol (`<`). In type
expression context, the final namespace qualifier is omitted.

Two examples of paths with type arguments:

```rust
# struct HashMap<K, V>(K,V);
# fn f() {
# fn id<T>(t: T) -> T { t }
type T = HashMap<i32,String>; // Type arguments used in a type expression
let x  = id::<i32>(10);       // Type arguments used in a call expression
# }
```

## Types of paths

### Simple paths

> **<sup>Syntax</sup>**  
> _SimplePath_ :  
> &nbsp;&nbsp; `::`<sup>?</sup> _PathSegmentIdentifier_ (`::` _PathSegmentIdentifier_)<sup>\*</sup>  
>  
> _PathSegmentIdentifier_ :  
> &nbsp;&nbsp; [IDENTIFIER] | `super` | `self` | `Self` **FIXME**  

Simple paths are used on `pub` markers, macro invocations and `use` items.

<!-- FIXME examples -->
<!-- FIXME where are they used -->

<!-- 1 - macro invocation as trait item -->
<!-- 2 - macro invocation as impl item (seems to only accept methods. Can't define other impl items using macros?) -->
<!-- 3 - pub(in SimplePath), pub(self), pub(super) [self and super are parsed as a SimplePath] -->
<!-- 4 - macro invocation item -->
<!-- 5 - use item -->

### Paths in expressions

> **<sup>Syntax</sup>**  
> _PathInExpr_ :  
> &nbsp;&nbsp; `::`<sup>?</sup> _PathSegmentIdentifier_ (`::` (_PathSegmentIdentifier_ | _GenericsForType_) )<sup>\*</sup>  
>  
> _QualifiedPathInExpr_ :  
> &nbsp;&nbsp; `<` type_ (`as` _TypePath_)? `>` `::` _PathInExpr_  

<!-- FIXME examples -->
<!-- FIXME qualified examples -->
<!-- FIXME where are they used

1 - qualified path expression         - _QualifiedPathInExpr_
2 - macro invocation                  - _PathInExpr_ `!`
3 - struct expr (not always allowed)  - _PathInExpr_ { ... }
4 - path expression                   - _PathInExpr_
5 - method call                       - `.` _PathSegmentInExpression_ `(` ... `)`
6 - field access                      - `.` _PathSegmentInExpression_
        obs: no generic arguments are allowed
7 - cast                              - `as` _PathInExpr_ (but only in case of error)
8 - range pattern end                 - `...` _QualifiedPathInExpr_
                                      - `...` _PathInExpr_
9 - patterns that start with a path   - macro invocation in pattern
                                      - range pattern
                                      - struct pattern (no qualified path allowed, though)
                                      - tuple pattern (no qualified path allowed, though)
                                      - path pattern
10 - expressions in statements        - no qualified path allowed
11 - macro invocation in statements   - no qualified path allowed

-->
<!-- FIXME ambiguity -->

### Paths in types

> **<sup>Syntax</sup>**  
> _TypePath_ :  
> &nbsp;&nbsp; `::`<sup>?</sup> _TypePathElement_ (`::` _TypePathElement_)<sup>\*</sup>  
>  
> _TypePathElement_ :  
> &nbsp;&nbsp; _PathSegmentIdentifier_ (_GenericsForType_ | _FunctionSignature_)<sup>?</sup>  
>  
> _GenericsForType_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; `<` (_LifetimeParams_ (`,` _TypeParamsForTypes_)<sup>?</sup> (`,` _BindingParams_)<sup>?</sup> `,`<sup>?</sup> )<sup>?</sup> `>`  
> &nbsp;&nbsp; | `<` _TypeParamsForTypes_ (`,` _BindingParams_)<sup>?</sup> `,`<sup>?</sup> `>`  
> &nbsp;&nbsp; | `<` _BindingParams_ `,`<sup>?</sup> `>`  
>  
> _TypeParamsForTypes_ :  
> &nbsp;&nbsp; _Type_ (`,` _Type_)<sup>\*</sup>  
>  
> _BindingParams_ :  
> &nbsp;&nbsp; _TypeBindingParam_ (`,` _TypeBindingParam_)<sup>\*</sup>  
>  
> _TypeBindingParam_ :  
> &nbsp;&nbsp; IDENTIFIER `=` type_ **FIXME**  

<!-- FIXME examples -->
<!-- FIXME qualified examples -->
<!-- FIXME where are they used 

1 - types
2 - `for` in types
3 - all qualified paths, after the `as`
4 - type param bounds

-->

## Path qualifiers

Paths can be denoted with various leading qualifiers to change the meaning of
how it is resolved.

### `::`

Paths starting with `::` are considered to be global paths where the
components of the path start being resolved from the crate root. Each
identifier in the path must resolve to an item.

```rust
mod a {
    pub fn foo() {}
}
mod b {
    pub fn foo() {
        ::a::foo(); // call a's foo function
    }
}
# fn main() {}
```

### `super`

Paths starting with the keyword `super` begin resolution relative to the
parent module. Each further identifier must resolve to an item.

```rust
mod a {
    pub fn foo() {}
}
mod b {
    pub fn foo() {
        super::a::foo(); // call a's foo function
    }
}
# fn main() {}
```

### `self`

Paths starting with the keyword `self` begin resolution relative to the
current module. Each further identifier must resolve to an item.

```rust
fn foo() {}
fn bar() {
    self::foo();
}
# fn main() {}
```

Additionally keyword `super` may be repeated several times after the first
`super` or `self` to refer to ancestor modules.

```rust
mod a {
    fn foo() {}

    mod b {
        mod c {
            fn foo() {
                super::super::foo(); // call a's foo function
                self::super::super::foo(); // call a's foo function
            }
        }
    }
}
# fn main() {}
```

<!-- FIXME Self:: ? -->

### Canonical paths

## Qualified paths

> **<sup>Syntax</sup>**  
> _Qualified_TypePath__ :  
> &nbsp;&nbsp; `<` [_Type_]&nbsp;(`as` _TypePath_)? `>` `::` _TypePath_ **FIXME**  

Items defined in a module or implementation have a *canonical path* that
corresponds to where within its crate it is defined. All other paths to these
items are aliases. The canonical path is defined as a *path prefix* appended by
the path component the item itself defines.

[Implementations] and [use declarations] do not have canonical paths, although
the items that implementations define do have them. Items defined in
block expressions do not have canonical paths. Items defined in a module that
does not have a canonical path do not have a canonical path. Associated items
defined in an implementation that refers to an item without a canonical path,
e.g. as the implementing type, the trait being implemented, a type parameter or
bound on a type parameter, do not have canonical paths.

The path prefix for modules is the canonical path to that module. For bare
implementations, it is the canonical path of the item being implemented
surrounded by <span class="parenthetical">angle (`<>`)</span> brackets. For
trait implementations, it is the canonical path of the item being implemented
followed by `as` followed by the canonical path to the trait all surrounded in
<span class="parenthetical">angle (`<>`)</span> brackets. 

The canonical path is only meaningful within a given crate. There is no global
namespace across crates; an item's canonical path merely identifies it within
the crate.

```rust
// Comments show the canonical path of the item.

mod a { // ::a
    pub struct Struct; // ::a::Struct

    pub trait Trait { // ::a::Trait
        fn f(&self); // a::Trait::f
    }

    impl Trait for Struct {
        fn f(&self) {} // <::a::Struct as ::a::Trait>::f
    }

    impl Struct {
        fn g(&self) {} // <::a::Struct>::g
    }
}

mod without { // ::without
    fn canonicals() { // ::without::canonicals
        struct OtherStruct; // None

        trait OtherTrait { // None
            fn g(&self); // None
        }

        impl OtherTrait for OtherStruct {
            fn g(&self) {} // None
        }

        impl OtherTrait for ::a::Struct {
            fn g(&self) {} // None
        }

        impl ::a::Trait for OtherStruct {
            fn f(&self) {} // None
        }
    }
}

# fn main() {}
```

[_Path_]: #paths
[_NonGlobalPath_]: #nonglobal-path
[_GlobalPath_]: #global-path
[_PathSegment_]: #path-segment

[IDENTIFIER]: identifiers.html

[item]: items.html
[identifiers]: identifiers.html
[expression]: expressions.html
[variable]: variables.html

[_Type_]: types.html
