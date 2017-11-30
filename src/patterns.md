# Patterns

> **<sup>Syntax</sup>**  
> _Pattern_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; [_LiteralPattern_]  
> &nbsp;&nbsp; | [_WildcardPattern_]  
> &nbsp;&nbsp; | [_RangePattern_]  
> &nbsp;&nbsp; | [_ReferencePattern_]  
> &nbsp;&nbsp; | [_IdentifierPattern_]  
> &nbsp;&nbsp; | [_StructPattern_]  
> &nbsp;&nbsp; | [_TuplePattern_]  
> &nbsp;&nbsp; | [_TupleStructPattern_]  
> &nbsp;&nbsp; | [_PathPattern_]  

Patterns in Rust are used to match values against structures and to,
optionally, bind variables to values inside these structures. They are also
used in variable declarations and function/closure parameters, though in these
cases most of the time they are simply used as an identifier that binds to a
value.

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
breaks a value up into its component pieces. The syntax used is almost the same as
when creating such values. When destructing a data structure with named (but
not numbered) fields, it is allowed to write `fieldname` as a shorthand for
`fieldname: fieldname`. In a pattern whose head expression has a `struct`,
`enum` or `tupl` type, a placeholder (`_`) stands for a *single* data field,
whereas a wildcard `..` stands for *all* the remaining fields of a particular variant.

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

A pattern is said to be *Refutable* when it **has the possibily of not being matched**
by the value it is being matched against. *Irrefutable* patterns, on the other hand,
always match the value they are being matched againt. Examples:

```rust
let (x, y) = (1, 2);               // "(x, y)" is an irrefutable pattern

if let (a, 3) = (1, 2) {           // "(a, 3)" is refutable, and will not match
    panic!("Shouldn't reach here");
} else if let (a, 4) = (3, 4) {    // "(a, 4)" is refutable, and will match
    println!("Matched ({}, 4)", a);
}
```

## Literal patterns

> **<sup>Syntax</sup>**  
> _LiteralPattern_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; BOOLEAN_LITERAL   
> &nbsp;&nbsp; | CHAR_LITERAL  
> &nbsp;&nbsp; | BYTE_LITERAL  
> &nbsp;&nbsp; | STRING_LITERAL  
> &nbsp;&nbsp; | RAW_STRING_LITERAL  
> &nbsp;&nbsp; | BYTE_STRING_LITERAL  
> &nbsp;&nbsp; | RAW_BYTE_STRING_LITERAL  
> &nbsp;&nbsp; | `-`<sup>?</sup> INTEGER_LITERAL  
> &nbsp;&nbsp; | `-`<sup>?</sup> FLOAT_LITERAL  

_Literal patterns_ match exactly the value they represent. Since negative numbers are
not literals in Rust, literal patterns also accept an optional minus sign before the
literal.

Floating-point literals are currently accepted, but due to the complexity of comparing
them, they are going to be forbidden on literal patterns in a future version of Rust (see
[issue #41620](https://github.com/rust-lang/rust/issues/41620)).

Literal patterns are always refutable.

Examples:

<!-- FIXME more examples -->

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

## Wildcard pattern

> **<sup>Syntax</sup>**  
> _WildcardPattern_ :  
> &nbsp;&nbsp; `_`

<!-- FIXME explain the wildcard pattern -->

The _wildcard pattern_ matches any value.

For example: 

```rust
# let x = 20;
let (a, _) = (10, x);   // the x is always matched by _
# assert_eq!(a, 10);
```

The wildcard pattern is always irrefutable.

<!-- FIXME examples -->
<!-- FIXME example: ignore function parameter -->
<!-- FIXME example: ignore a field from a tuple -->
<!-- FIXME example: ignore a field from a struct -->
<!-- FIXME example: ignore the field of an enum: use Some(_) -->

## Range patterns

> **<sup>Syntax</sup>**  
> _RangePattern_ :  
> &nbsp;&nbsp;  _RangePatternBound_ `...` _RangePatternBound_  
>  
> _RangePatternBound_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; CHAR_LITERAL  
> &nbsp;&nbsp; | BYTE_LITERAL  
> &nbsp;&nbsp; | `-`<sup>?</sup> INTEGER_LITERAL  
> &nbsp;&nbsp; | `-`<sup>?</sup> FLOAT_LITERAL  
> &nbsp;&nbsp; | [_PathInExpression_]  
> &nbsp;&nbsp; | [_QualifiedPathForExpression_]  

[_PathInExpression_]: paths.html
[_QualifiedPathForExpression_]: paths.html

Range patterns match values that are within the closed range defined by its lower and
upper bounds. For example, a pattern `'m'...'p'` will match only the values `'m'`, `'n'`,
`'o'`, and `'p'`. The bounds can be literals or paths that point to constant values.

A pattern a `...` b must always have a &le; b. Thus, it is not possible to have a range
pattern `10...0`.

Range patterns only work on scalar types. The accepted types are:

* Integer types (u8, i8, u16, i16, usize, isize, etc.).
* Character types (char).
* Floating point types (f32 and f64). This is being deprecated and will not be available
  in a future version of Rust (see
  [issue #41620](https://github.com/rust-lang/rust/issues/41620)).

Examples:

```rust
# let c = 'f';
let valid_variable = match c {
    'a'...'z' => true,
    'A'...'Z' => true,
    'α'...'ω' => true,
    _ => false,
};

# let ph = 10;
println!("{}", match ph {
    0...6 => "acid",
    7 => "neutral",
    8...14 => "base",
    _ => unreachable!(),
});

// using paths to constants:
# const TROPOSPHERE_MIN : u8 = 6;
# const TROPOSPHERE_MAX : u8 = 20;
# 
# const STRATOSPHERE_MIN : u8 = TROPOSPHERE_MAX + 1;
# const STRATOSPHERE_MAX : u8 = 50;
# 
# const MESOSPHERE_MIN : u8 = STRATOSPHERE_MAX + 1;
# const MESOSPHERE_MAX : u8 = 85;
# 
# let altitude = 70;
# 
println!("{}", match altitude {
    TROPOSPHERE_MIN...TROPOSPHERE_MAX => "troposphere",
    STRATOSPHERE_MIN...STRATOSPHERE_MAX => "stratosphere",
    MESOSPHERE_MIN...MESOSPHERE_MAX => "mesosphere",
    _ => "outer space, maybe",
});

# pub mod binary {
#     pub const MEGA : u64 = 1024*1024;
#     pub const GIGA : u64 = 1024*1024*1024;
# }
# let n_items = 20_832_425;
# let bytes_per_item = 12;
if let size @ binary::MEGA...binary::GIGA = n_items * bytes_per_item {
    println!("It fits and occupies {} bytes", size);
}

# trait MaxValue {
#     const MAX: u64;
# }
# impl MaxValue for u8 {
#     const MAX: u64 = (1 << 8) - 1;
# }
# impl MaxValue for u16 {
#     const MAX: u64 = (1 << 16) - 1;
# }
# impl MaxValue for u32 {
#     const MAX: u64 = (1 << 32) - 1;
# }
// using qualified paths:
println!("{}", match 0xfacade {
    0 ... <u8 as MaxValue>::MAX => "fits in a u8",
    0 ... <u16 as MaxValue>::MAX => "fits in a u16",
    0 ... <u32 as MaxValue>::MAX => "fits in a u32",
    _ => "too big",
});

```

Range patterns are a priori always refutable, even when they cover the complete set
of possible values of a type. For example, `0u8...255u8` is refutable even though
it covers all possible values of `u8`.

<!-- FIXME change _PathForExpression_ to _PathInExpression_ ? -->

<!-- FIXME put this on the match section
A range pattern may not be a sub-range of another range pattern inside the same `match`.
-->

## Reference patterns

> **<sup>Syntax</sup>**  
> _ReferencePattern_ :  
> &nbsp;&nbsp; (`&`|`&&`) `mut`<sup>?</sup> _Pattern_  

<!-- FIXME: explain reference patterns  -->
<!-- FIXME: explain why the `&&` is part of the grammar -->
<!-- FIXME: explain that they only dereference one time -->
<!-- FIXME: example with 3 or more & -->

Reference patterns dereference the pointers that are being matched
and, thus, borrow them. If 

For example, these two matches on `x: &i32` are equivalent:

```rust
# let x = &3;
let y = match *x { 0 => "zero", _ => "some" };
let z = match x { &0 => "zero", _ => "some" };

assert_eq!(y, z);
```

Reference patterns are always irrefutable.

## Identifier patterns

> **<sup>Syntax</sup>**  
> _IdentifierPattern_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; `mut`<sup>?</sup> IDENTIFIER (`@` [_Pattern_] ) <sup>?</sup>  
> &nbsp;&nbsp; | `ref` `mut`<sup>?</sup> IDENTIFIER (`@` [_Pattern_] ) <sup>?</sup>

<!-- FIXME: explain identifier patterns -->
<!-- FIXME: mention that IDENTIFIER pattern is the commonly used one in let and function parameters -->

_Identifier patterns_ bind the value they match to a **previously undeclared** variable.

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

By default, identifier patterns bind a variable to a copy of or move from the
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

Thus, `ref` is not something that is being matched against. Its objective is
exclusively to make the matched binding a reference, instead of potentially
copying or moving what was matched.

<!-- FIXME: identifier patterns that don't have mut/ref/@ and that refer to an identifier -->


<!-- FIXME cannot bind by-move and by-ref in the same pattern -->
<!-- FIXME explain the difference between `& var` and `ref var` in patterns -->

<!-- when is this pattern type refutable? -->

## Struct patterns

> **<sup>Syntax</sup>**  
> _StructPattern_ :  
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

<!-- FIXME: explain struct patterns -->
<!-- FIXME: destructuring patterns -->

Struct patterns match ...

<!-- when is this pattern type refutable? -->

## TupleStruct patterns

> **<sup>Syntax</sup>**  
> _TupleStructPattern_ :  
> &nbsp;&nbsp; _Path_ `(` _TupleStructItems_ `)`  
>  
> _TupleStructItems_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; [_Pattern_]&nbsp;( `,` [_Pattern_] )<sup>\*</sup> `,`<sup>?</sup>  
> &nbsp;&nbsp; | ([_Pattern_] `,`)<sup>\*</sup> `..` ( (`,` [_Pattern_])<sup>+</sup> `,`<sup>?</sup> )<sup>?</sup>  

<!-- FIXME: explain tuple struct patterns -->
<!-- FIXME: includes enum variants? Yes! -->

<!-- when is this pattern type refutable? -->

## Tuple patterns

> **<sup>Syntax</sup>**  
> _TuplePattern_ :<a name="tuple-pattern-syntax"></a>  
> &nbsp;&nbsp; `(` _TupplePatternItems_<sup>?</sup> `)`  
>  
> _TuplePatternItems_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; [_Pattern_] `,`  
> &nbsp;&nbsp; | [_Pattern_]&nbsp;(`,` [_Pattern_])<sup>+</sup> `,`<sup>?</sup>  
> &nbsp;&nbsp; | ([_Pattern_] `,`)<sup>\*</sup> `..` ( (`,` [_Pattern_])<sup>+</sup> `,`<sup>?</sup> )<sup>?</sup>  

<!-- FIXME: explain tuple patterns -->

<!-- when is this pattern type refutable? -->

## Path patterns

> **<sup>Syntax</sup>**  
> _PathPattern_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; _PathForExpression_  
> &nbsp;&nbsp; | _QualifiedPathForExpression_

_Path patterns_ are patterns that refer either to constant values or
to structs or enum variants that have no fields.

<!-- FIXME how to disambiguate between identifier patterns and path patterns 

Patterns 

-->

Unqualified path patterns can refer to

* enum variants
* structs
* constants
* associated constants

Qualified path patterns can only refer to associated constants.

<!-- FIXME: explain paths in patterns -->
<!-- FIXME examples -->
<!-- FIXME when is this pattern type refutable? -->

Path patterns are irrefutable when they refer to constants or structs.
They are refutable when the refer to enum variants.

[_Pattern_]: #patterns
[_LiteralPattern_]: #literal-patterns
[_WildcardPattern_]: #wildcard-pattern
[_RangePattern_]: #range-patterns
[_ReferencePattern_]: #reference-patterns
[_IdentifierPattern_]: #identifier-patterns
[_TupleStructPattern_]: #tuplestruct-patterns
[_StructPattern_]: #struct-patterns
[_TuplePattern_]: #tuple-patterns
[_PathPattern_]: #path-patterns
