# Patterns

<!-- FIXME: pattern introduction -->
<!-- FIXME: pattern main uses (functions, match, let, if let, while let, etc.) -->

> **<sup>Syntax</sup>**  
> _Pattern_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; _WildcardPattern_  
> &nbsp;&nbsp; | _ReferencePattern_  
> &nbsp;&nbsp; | _TuplePattern_  
> &nbsp;&nbsp; | _SlicePattern_  
> &nbsp;&nbsp; | _IdentifierPattern_  
> &nbsp;&nbsp; | _BoxPattern_  
> &nbsp;&nbsp; | _PathPattern_  
> &nbsp;&nbsp; | _LiteralPattern_  
> &nbsp;&nbsp; | _RangePattern_  
> &nbsp;&nbsp; | _StructPattern_  

<!-- FIXME: irrefutable patterns -->
<!-- FIXME: multiple patterns: a | b -->
<!-- FIXME: ignoring one value: _ -->
<!-- FIXME: ignoring multiple values: .. -->
<!-- FIXME: binding: @ -->
<!-- FIXME: guards: _Pattern_ `if` _Expression_ -->

## Wildcard pattern

> **<sup>Syntax</sup>**  
> _WildcardPattern_ :  
> &nbsp;&nbsp; `_`

<!-- FIXME: explain wildcard patterns -->

## Reference patterns

> **<sup>Syntax</sup>**  
> _ReferencePattern_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; (`&`|`&&`) _Pattern_  
> &nbsp;&nbsp; | (`&`|`&&`) _Mutability_ _Pattern_  

<!-- FIXME: explain reference patterns  -->

## Tuple patterns

> **<sup>Syntax</sup>**  
> _TuplePattern_ :  
> &nbsp;&nbsp; **FIXME**

<!-- FIXME: explain tuple patterns -->
<!-- FIXME: includes enum variants? -->

## Slice patterns

> **<sup>Syntax</sup>**  
> _SlicePattern_ :  
> &nbsp;&nbsp; **FIXME**

<!-- FIXME: explain slice patterns -->

## Identifier patterns

> **<sup>Syntax</sup>**  
> _IdentifierPattern :  
> &nbsp;&nbsp; &nbsp;&nbsp; `mut` IDENTIFIER  
> &nbsp;&nbsp; | `mut` IDENTIFIER `@` _Pattern_  
> &nbsp;&nbsp; | `ref` IDENTIFIER `@` _Pattern_  

<!-- FIXME: explain identifier patterns -->

## Path patterns

> **<sup>Syntax</sup>**  
> _PathPattern_ :  
> &nbsp;&nbsp; **FIXME**

<!-- FIXME: explain paths in patterns -->

## Literal patterns

> **<sup>Syntax</sup>**  
> _LiteralPattern_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; LITERAL  
> &nbsp;&nbsp; | `-` LITERAL  

<!-- FIXME: explain literal patterns -->

## Range patterns

> **<sup>Syntax</sup>**  
> _RangePattern_ :  
> &nbsp;&nbsp; **FIXME**

<!-- FIXME: explain range patterns -->

## Tuple struct patterns

<!-- FIXME: explain struct patterns -->

<!-- FIXME: destructuring patterns -->

## Box pattern

> **<sup>Syntax</sup>**  
> _BoxPattern_ :  
> &nbsp;&nbsp; **FIXME**

<!-- FIXME: explain box patterns -->
<!-- FIXME: find out whether they're not stable -->

## Refutability
