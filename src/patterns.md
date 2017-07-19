# Patterns

**FIXME:** pattern introduction

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

**FIXME:** pattern uses (functions, match, let, if let, while let, etc.)

**FIXME:** irrefutable patterns

## Wildcard pattern

> **<sup>Syntax</sup>**  
> _WildcardPattern_ :  
> &nbsp;&nbsp; `_`

## Reference patterns

> **<sup>Syntax</sup>**  
> _ReferencePattern_ :  
> &nbsp;&nbsp; &nbsp;&nbsp; (`&`|`&&`) _Pattern_  
> &nbsp;&nbsp; | (`&`|`&&`) _Mutability_ _Pattern_  

## Tuple patterns

> **<sup>Syntax</sup>**  
> _TuplePattern_ :  
> &nbsp;&nbsp; **FIXME**

## Slice patterns

> **<sup>Syntax</sup>**  
> _SlicePattern_ :  
> &nbsp;&nbsp; **FIXME**

## Identifier patterns

> **<sup>Syntax</sup>**  
> _IdentifierPattern :  
> &nbsp;&nbsp; &nbsp;&nbsp; `mut` IDENTIFIER  
> &nbsp;&nbsp; | `mut` IDENTIFIER `@` _Pattern_  
> &nbsp;&nbsp; | `ref` IDENTIFIER `@` _Pattern_  

## Box pattern

> **<sup>Syntax</sup>**  
> _BoxPattern_ :  
> &nbsp;&nbsp; **FIXME**

## Path patterns

> **<sup>Syntax</sup>**  
> _PathPattern_ :  
> &nbsp;&nbsp; **FIXME**

## Literal patterns

> **<sup>Syntax</sup>**  
> _LiteralPattern_ :  
> &nbsp;&nbsp; **FIXME**

## Range patterns

> **<sup>Syntax</sup>**  
> _RangePattern_ :  
> &nbsp;&nbsp; **FIXME**

## Struct patterns

**FIXME:** enum, actually?
