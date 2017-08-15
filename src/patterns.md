# Patterns

> **<sup>Syntax</sup>**  
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

<!-- FIXME: pattern introduction -->
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

## Wildcard pattern
[_WildcardPattern_]: #wildcard-pattern

> **<sup>Syntax</sup>**  
> _WildcardPattern_ :  
> &nbsp;&nbsp; `_`

<!-- FIXME: explain wildcard patterns -->

## Reference patterns
[_ReferencePattern_]: #reference-patterns

> **<sup>Syntax</sup>**  
> _ReferencePattern_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; (`&`|`&&`) _Pattern_  
> &nbsp;&nbsp; | (`&`|`&&`) _Mutability_ _Pattern_  

<!-- FIXME: explain reference patterns  -->

Patterns can also dereference pointers by using the `&`, `&mut` and `box`
symbols, as appropriate. For example, these two matches on `x: &i32` are
equivalent:

```rust
# let x = &3;
let y = match *x { 0 => "zero", _ => "some" };
let z = match x { &0 => "zero", _ => "some" };

assert_eq!(y, z);
```

## Struct patterns
[_StructPattern_]: #struct-patterns

<!-- FIXME: explain struct patterns -->
<!-- FIXME: destructuring patterns -->

## TupleStruct patterns
[_TupleStructPattern_]: #tuplestruct-patterns

> **<sup>Syntax</sup>**  
> _TupleStructPattern_ :  
> &nbsp;&nbsp; **FIXME**

<!-- FIXME: explain tuple patterns -->
<!-- FIXME: includes enum variants? -->

## Slice patterns
[_SlicePattern_]: #slice-patterns

> **<sup>Syntax</sup>**  
> _SlicePattern_ :  
> &nbsp;&nbsp; **FIXME**

<!-- FIXME: explain slice patterns -->

## Identifier patterns
[_IdentifierPattern_]: #identifier-patterns

> **<sup>Syntax</sup>**  
> _IdentifierPattern :  
> &nbsp;&nbsp; &nbsp;&nbsp; `mut` IDENTIFIER  
> &nbsp;&nbsp; | `mut` IDENTIFIER `@` _Pattern_  
> &nbsp;&nbsp; | `ref` IDENTIFIER `@` _Pattern_  

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

## Path patterns
[_PathPattern_]: #path-patterns

> **<sup>Syntax</sup>**  
> _PathPattern_ :  
> &nbsp;&nbsp; **FIXME**

<!-- FIXME: explain paths in patterns -->

## Literal patterns
[_LiteralPattern_]: #literal-patterns

> **<sup>Syntax</sup>**  
> _LiteralPattern_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; LITERAL  
> &nbsp;&nbsp; | `-` LITERAL  

<!-- FIXME: explain literal patterns -->

## Range patterns
[_RangePattern_]: #range-patterns

> **<sup>Syntax</sup>**  
> _RangePattern_ :  
> &nbsp;&nbsp; **FIXME**

<!-- FIXME: explain range patterns -->

Range patterns only work on scalar types (like integers and characters; not
like arrays and structs, which have sub-components). A range pattern may not be
a sub-range of another range pattern inside the same `match`.


## Box pattern
[_BoxPattern_]: #box-pattern

> **<sup>Syntax</sup>**  
> _BoxPattern_ :  
> &nbsp;&nbsp; **FIXME**

<!-- FIXME: explain box patterns -->
<!-- FIXME: find out whether they're not stable -->

