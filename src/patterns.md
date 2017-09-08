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

Patterns in Rust are used to match values against structures and to,
optionally, bind variables to values inside these structures. They are also
used in variable declarations and function/closure parameters, though most of
the time simply as an identifier that binds to any value.

For example, the pattern used in:

```rust
# struct Car;
# struct Computer;
# struct Person {
#     name: String,
#     car: Option<Car>,
#     computer: Option<Computer>,
#     age: u8,
# }
# let person = Person {
#     name: String::from("John"),
#     car: Some(Car),
#     computer: None,
#     age: 15,
# };
if let
    Person {
        car: Some(_),
        age: person_age @ 13...19,
        name: ref person_name,
        ..
    } = person
{
    println!("{} has a car and is {} years old.", person_name, person_age);
}
```
does four things:

* Tests if `person` has the `car` field filled with something.
* Tests if the person's `age` field is between 13 and 19, and binds its value to
  the `person_age` variable.
* Binds a reference to the `name` field to the variable `person_name`.
* Ignores the rest of the fields of `person`, i.e., they can have any value and
  are not bound to any variables.

Patterns are used in:

* [`let` declarations](statements.html#let-statements)
* [Function](items.html#functions) and [closure](expressions.html#closure-expressions)
  parameters
* [`match` expressions](expressions.html#match-expressions)
* [`if let` expressions](expressions.html#if-let-expressions)
* [`while let` expressions](expressions.html#while-let-loops)
* Inside other patterns

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
<!-- FIXME: which things don't accept irrefutable patterns? -->
<!-- FIXME: which things don't accept refutable patterns? -->

## Literal patterns

> **<sup>Syntax</sup>**  
> _LiteralPattern_ :<a name="literal-pattern-syntax"></a>  
> &nbsp;&nbsp; `-`<sup>?</sup> ( CHAR_LITERAL | INTEGER_LITERAL | FLOAT_LITERAL )  

[_LiteralPattern_]: #literal-pattern-syntax

_Literal patterns_ match exactly the value they represent. Since negative numbers are
not literals in Rust, literal patterns also accept an optional minus sign before the
literal.

Floating-point literals are currently accepted, but due to the complexity of comparing
them, they are going to be forbidden in a future version of Rust (see
[issue #41620](https://github.com/rust-lang/rust/issues/41620)).

Example:

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

## Wildcard pattern

> **<sup>Syntax</sup>**  
> _WildcardPattern_ :<a name="wildcard-pattern-syntax"></a>  
> &nbsp;&nbsp; `_`

[_WildcardPattern_]: #wildcard-pattern-syntax

<!-- FIXME explain the wildcard pattern -->

The _wildcard pattern_ means any value or the value does not matter.

For example: 

```
    
```

<!-- FIXME but it can be bound to a variable -->

<!-- FIXME where can it be used? -->
<!-- FIXME examples -->
<!-- FIXME example: ignore function parameter -->
<!-- FIXME example: ignore a field from a tuple -->
<!-- FIXME example: ignore a field from a struct -->
<!-- FIXME example: ignore the field of an enum: use Some(_) -->

## Range patterns

> **<sup>Syntax</sup>**  
> _RangePattern_ :<a name="reference-pattern-syntax"></a>  
> &nbsp;&nbsp; _Expression_ `...` _Expression_  

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
> &nbsp;&nbsp; (`&`|`&&`) `mut`<sup>?</sup> _Pattern_  

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
> _IdentifierPattern_ :<a name="identifier-pattern-syntax"></a>  
> &nbsp;&nbsp; &nbsp;&nbsp; `mut`<sup>?</sup> IDENTIFIER (`@` [_Pattern_] ) <sup>?</sup>  
> &nbsp;&nbsp; | `ref` `mut`<sup>?</sup> IDENTIFIER (`@` [_Pattern_] ) <sup>?</sup>

[_IdentifierPattern_]: #identifier-pattern-syntax

<!-- FIXME: explain identifier patterns -->
<!-- FIXME: mention that IDENTIFIER pattern is the commonly used one in let and function parameters -->

_Identifier patterns_ bind the value they match to a variable.

Patterns that consist of only an identifier, possibly with a `mut`, like
`variable`, `x`, and `y` below:

```rust
let mut variable = 10;
fn sum(x: i32, y: i32) -> i32 {
#    x + y
#}
```

match any value and bind it to that identifier. This is the most commonly
used pattern in variable declarations and function/closure parameters.

To bind non-trivial patterns to a variable, the use of the syntax `variable @
subpattern` is needed. For example:

```rust
let x = 1;

match x {
    e @ 1 ... 5 => println!("got a range element {}", e),
    _ => println!("anything"),
}
```

binds to `e` the value 1 (not the entire range: the range is a range subpattern).

By default, identifier patterns bind a variable to a copy or move of the
matched value (depending whether the matched value implements the Copy trait).
This can be changed to bind to a reference by using the `ref` keyword,
or to a mutable reference using `ref mut`. For example:

```rust
// TODO
```

in the first match arm, the value is copied. In the second one, a reference
to the same memory location is bound to the variable. This syntax is needed
because in destructuring subpatterns we can't apply the `&` operator to
the value's fields. For example:

```rust,compile_fail
// TODO

struct Person {
    name: String,
}

if let Person{& name: person_name} = value {
}

```

is not valid. What we must do is:

```
// TODO

struct Person {
    name: String,
}

if let Person(name: ref person_name) = value {
}
```

<!-- FIXME cannot bind by-move and by-ref in the same pattern -->
<!-- FIXME explain the difference between `& var` and `ref var` in patterns -->

## Box pattern

> **<sup>Syntax</sup>**  
> _BoxPattern_ :<a name="box-pattern-syntax"></a>  
> &nbsp;&nbsp; `box` [_Pattern_]  

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
> &nbsp;&nbsp; &nbsp;&nbsp; _StructPatternFields_ (`,` | `,` _StructPatternEtCetera_)<sup>?</sup>  
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
> &nbsp;&nbsp; _Path_ `(` _TupleStructItems_ `)`  
>  
> _TupleStructItems_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; [_Pattern_]&nbsp;( `,` [_Pattern_] )<sup>\*</sup> `,`<sup>?</sup>  
> &nbsp;&nbsp; | ([_Pattern_] `,`)<sup>\*</sup> `..` ( (`,` [_Pattern_])<sup>+</sup> `,`<sup>?</sup> )<sup>?</sup>  

[_TupleStructPattern_]: #tuplestruct-pattern-syntax

<!-- FIXME: explain tuple struct patterns -->
<!-- FIXME: includes enum variants? Yes! -->

## Tuple patterns

> **<sup>Syntax</sup>**  
> _TuplePattern_ :<a name="tuple-pattern-syntax"></a>  
> &nbsp;&nbsp; `(` _TupplePatternItems_<sup>?</sup> `)`  
>  
> _TuplePatternItems_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; [_Pattern_] `,`  
> &nbsp;&nbsp; | [_Pattern_]&nbsp;(`,` [_Pattern_])<sup>+</sup> `,`<sup>?</sup>  
> &nbsp;&nbsp; | ([_Pattern_] `,`)<sup>\*</sup> `..` ( (`,` [_Pattern_])<sup>+</sup> `,`<sup>?</sup> )<sup>?</sup>  

[_TuplePattern_]: #tuple-pattern-syntax

<!-- FIXME: explain tuple patterns -->

## Slice patterns

> **<sup>Syntax</sup>**  
> _SlicePattern_ :<a name="slice-pattern-syntax"></a>  
> &nbsp;&nbsp; `[` **FIXME** `]`

[_SlicePattern_]: #slice-pattern-syntax

<!-- FIXME: explain slice patterns -->
<!-- FIXME: this is not stable -->

## Path patterns

> **<sup>Syntax</sup>**  
> _PathPattern_ :<a name="path-pattern-syntax"></a>  
> &nbsp;&nbsp; **FIXME**

[_PathPattern_]: #path-pattern-syntax

<!-- FIXME: explain paths in patterns -->

