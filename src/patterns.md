# Patterns

> **<sup>Syntax</sup>**  
> _Pattern_ :<a name="pattern-syntax"></a>  
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

[_Pattern_]: #pattern-syntax

<!-- FIXME: pattern introduction -->

Patterns can be used in:

  * Let declarations
  * Match expressions
  * If let expressions
  * While let expressions
  * Function parameters
  * Inside other patterns

<!-- FIXME: pattern main uses (functions, match, let, if let, while let, etc.) -->

## Destructuring

Patterns can be used to *destructure* structs, enums, and tuples. Destructuring
breaks a value up into its component pieces. The syntax used is the same as
when creating such values. When destructing a data structure with named (but
not numbered) fields, it is allowed to write `fieldname` as a shorthand for
`fieldname: fieldname`. In a pattern whose head expression has a `struct`,
`enum` or `tupl` type, a placeholder (`_`) stands for a *single* data field,
whereas a wildcard `..` stands for *all* the fields of a particular variant.

```rust
# enum Message {
#     Quit,
#     WriteString(String),
#     Move { x: i32, y: i32 },
#     ChangeColor(u8, u8, u8),
# }
# let message = Message::Quit;
match message {
    Message::Quit => println!("Quit"),
    Message::WriteString(write) => println!("{}", &write),
    Message::Move{ x, y: 0 } => println!("move {} horizontally", x),
    Message::Move{ .. } => println!("other move"),
    Message::ChangeColor { 0: red, 1: green, 2: _ } => {
        println!("color change, red: {}, green: {}", red, green);
    }
};
```

## Refutability

<!-- FIXME: irrefutable patterns -->
<!-- FIXME: multiple patterns: a | b -->
<!-- FIXME: ignoring one value: _ -->
<!-- FIXME: ignoring multiple values: .. -->
<!-- FIXME: binding: @ -->
<!-- FIXME: guards: _Pattern_ `if` _Expression_ -->

## Literal patterns

> **<sup>Syntax</sup>**  
> _LiteralPattern_ :<a name="literal-pattern-syntax"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; LITERAL  
> &nbsp;&nbsp; | `-` LITERAL  

[_LiteralPattern_]: #literal-pattern-syntax

Literal patterns match exactly the value they represent.

For example, this loop:

```rust
for i in -2..5 {
    match i {
        -1 => println!("It's minus one"),
        1 => println!("It's a one"),
        2|4 => println!("It's either a two or a four"),
        _ => println!("Matched none of the arms"),
    }
}
```

prints

```text
Matched none of the arms
It's minus one
Matched none of the arms
It's a one
It's either a two or a four
Matched none of the arms
It's either a two or a four
```

<!-- FIXME float points are accepted, but are being deprecated -->

## Wildcard pattern

> **<sup>Syntax</sup>**  
> _WildcardPattern_ :<a name="wildcard-pattern-syntax"></a>  
> &nbsp;&nbsp; `_`

[_WildcardPattern_]: #wildcard-pattern-syntax

<!-- FIXME explain the wildcard pattern -->

The _wildcard pattern_ means any value or the value does not matter.

<!-- FIXME where can it be used? -->
<!-- FIXME examples -->

## Range patterns

> **<sup>Syntax</sup>**  
> _RangePattern_ :<a name="reference-pattern-syntax"></a>  
> &nbsp;&nbsp; **FIXME**

[_RangePattern_]: #range-pattern-syntax

<!-- FIXME: explain range patterns -->

Range patterns match ...

Range patterns only work on scalar types (like integers and characters; not
like arrays and structs, which have sub-components). A range pattern may not be
a sub-range of another range pattern inside the same `match`.

<!-- FIXME examples -->

<!-- which types can be used here? -->
<!-- FIXME floating point literals use here is being deprecated -->

## Reference patterns

> **<sup>Syntax</sup>**  
> _ReferencePattern_ :<a name="reference-pattern-syntax"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; (`&`|`&&`) _Pattern_  
> &nbsp;&nbsp; | (`&`|`&&`) _Mutability_ _Pattern_  

[_ReferencePattern_]: #reference-pattern-syntax

<!-- FIXME: explain reference patterns  -->
<!-- FIXME: explain why the `&&` is part of the grammar -->

Patterns can also dereference pointers by using the `&`, `&mut` and `box`
symbols, as appropriate. For example, these two matches on `x: &i32` are
equivalent:

```rust
# let x = &3;
let y = match *x { 0 => "zero", _ => "some" };
let z = match x { &0 => "zero", _ => "some" };

assert_eq!(y, z);
```

## Identifier patterns

> **<sup>Syntax</sup>**  
> _IdentifierPattern :<a name="identifier-pattern-syntax"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; `mut` IDENTIFIER  
> &nbsp;&nbsp; | `mut` IDENTIFIER `@` _Pattern_  
> &nbsp;&nbsp; | `ref` IDENTIFIER `@` _Pattern_  

[_IdentifierPattern_]: #identifier-pattern-syntax

<!-- FIXME: explain identifier patterns -->

Subpatterns can also be bound to variables by the use of the syntax `variable @
subpattern`. For example:

```rust
let x = 1;

match x {
    e @ 1 ... 5 => println!("got a range element {}", e),
    _ => println!("anything"),
}
```

Patterns that bind variables default to binding to a copy or move of the
matched value (depending on the matched value's type). This can be changed to
bind to a reference by using the `ref` keyword, or to a mutable reference using
`ref mut`.

<!-- explain the difference between `& var` and `ref var` in patterns -->

## Box pattern

> **<sup>Syntax</sup>**  
> _BoxPattern_ :<a name="box-pattern-syntax"></a>  
> &nbsp;&nbsp; `box` **FIXME**

[_BoxPattern_]: #box-pattern-syntax

<!-- FIXME: explain box patterns -->
<!-- FIXME: they're not stable -->

## Struct patterns

> **<sup>Syntax</sup>**  
> _StructPattern_ :<a name="struct-pattern-syntax"></a>  
> &nbsp;&nbsp; _Path_ `{`  
> &nbsp;&nbsp; &nbsp;&nbsp; _StructPatternElements_ <sup>?</sup>  
> &nbsp;&nbsp; `}`  
>  
> _StructPatternElements_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; _StructPatternFields_ (`,` _StructPatternEtCetera_) ?  
> &nbsp;&nbsp; | _StructPatternEtCetera_  
>  
> _StructPatternFields_ :  
> &nbsp;&nbsp; _StructPatternField_ (`,` _StructPatternField_) <sup>\*</sup>  
>  
> _StructPatternField_ :  
> &nbsp;&nbsp; _OuterAttribute_ <sup>\*</sup>  
> &nbsp;&nbsp; (  
> &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; INTEGER_LITERAL `:` [_Pattern_]  
> &nbsp;&nbsp; &nbsp;&nbsp; | IDENTIFIER `:` [_Pattern_]  
> &nbsp;&nbsp; &nbsp;&nbsp; | `box`<sup>?</sup> `ref`<sup>?</sup> `mut`<sup>?</sup>
>                                  IDENTIFIER  
> &nbsp;&nbsp; )  
>  
> _StructPatternEtCetera_ :  
> &nbsp;&nbsp; _OuterAttribute_ <sup>\*</sup>  
> &nbsp;&nbsp; `..`  

[_StructPattern_]: #struct-pattern-syntax

<!-- FIXME: explain struct patterns -->
<!-- FIXME: destructuring patterns -->

Struct patterns match ...

## TupleStruct patterns

> **<sup>Syntax</sup>**  
> _TupleStructPattern_ :<a name="tuplestruct-pattern-syntax"></a>  
> &nbsp;&nbsp; **FIXME**

[_TupleStructPattern_]: #tuplestruct-pattern-syntax

<!-- FIXME: explain tuple struct patterns -->
<!-- FIXME: includes enum variants? Yes! -->

## Tuple patterns

> **<sup>Syntax</sup>**  
> _TuplePattern_ :<a name="tuple-pattern-syntax"></a>  
> &nbsp;&nbsp; **FIXME**

[_TuplePattern_]: #tuple-pattern-syntax

<!-- FIXME: explain tuple patterns -->

## Slice patterns

> **<sup>Syntax</sup>**  
> _SlicePattern_ :<a name="slice-pattern-syntax"></a>  
> &nbsp;&nbsp; **FIXME**

[_SlicePattern_]: #slice-pattern-syntax

<!-- FIXME: explain slice patterns -->
<!-- FIXME: this is not stable -->

## Path patterns

> **<sup>Syntax</sup>**  
> _PathPattern_ :<a name="path-pattern-syntax"></a>  
> &nbsp;&nbsp; **FIXME**

[_PathPattern_]: #path-pattern-syntax

<!-- FIXME: explain paths in patterns -->

