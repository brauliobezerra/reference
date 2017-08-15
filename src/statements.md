# Statements

> **<sup>Syntax</sup>**  
> _Statement_ :  
> &nbsp;&nbsp; [_DeclarationStatement_] | [_Expression_] | `;`  

<!-- FIXME what kinds of statements need a semicolon? -->
<!-- FIXME explain whether Rust uses semicolons as separators (like pascal) or as terminators (like C) -->

[_DeclarationStatement_]: #declaration-statements
[_ExpressionStatement_]: #expression-statements

A _statement_ is a component of a block, which is in turn a component of an
outer [expression](expressions.html) or [function](items.html#functions).

Rust has two kinds of statement: [declaration
statements](#declaration-statements) and [expression
statements](#expression-statements).

## Declaration statements

> **<sup>Syntax</sup>**  
> _DeclarationStatement_ :  
> &nbsp;&nbsp; [_Item_] | [_LocalVariablesDeclaration_]

[_LocalVariablesDeclaration_]: #let-statements

A _declaration statement_ is one that introduces one or more *names* into the
enclosing statement block. The declared names may denote new variables or new
items.

### Item declarations

An _item declaration statement_ has a syntactic form identical to an
[item](items.html) declaration within a module. Declaring an item &mdash; a
function, enumeration, struct, type, static, trait, implementation or module
&mdash; locally within a statement block is simply a way of restricting its
scope to a narrow region containing all of its uses; it is otherwise identical
in meaning to declaring the item outside the statement block.

> **Note**: there is no implicit capture of the function's dynamic environment when
> declaring a function-local item.

### `let` statements

> **<sup>Syntax</sup>**  
> _LocalVariablesDeclaration_ :  
> &nbsp;&nbsp; `let` [_Pattern_]&nbsp;( `:` [_Type_] )<sup>?</sup> (`=` [_Expression_] )<sup>?</sup> `;`

A _`let` statement_ introduces a new set of variables, given by a pattern. The
pattern may be followed by a type annotation, and/or an initializer expression.
When no type annotation is given, the compiler will infer the type, or signal
an error if insufficient type information is available for definite inference.
Any variables introduced by a variable declaration are visible from the point of
declaration until the end of the enclosing block scope.

## Expression statements

> **<sup>Syntax</sup>**  
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

An _expression statement_ is one that evaluates an
[expression](expressions.html) and ignores its result. As a rule, an expression
statement's purpose is to trigger the effects of evaluating its expression.
An expression that consists of only a [block
expression](expressions.html#block-expressions) or control flow expression,
that doesn't end a block and evaluates to `()` can also be used as an
expression statement by omitting the trailing semicolon.

```rust
# let mut v = vec![1, 2, 3];
v.pop();          // Ignore the element returned from pop
if v.is_empty() {
    v.push(5);
} else {
    v.remove(0);
}                 // Semicolon can be omitted.
[1];              // Separate expression statement, not an indexing expression.
```

[_Item_]: items.html
[_Pattern_]: patterns.html
[_Type_]: types.html
[_Expression_]: expressions.html
