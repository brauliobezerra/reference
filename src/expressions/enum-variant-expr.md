# Enumeration Variant expressions

_Enumeration variants_ can be constructed similarly to structs expressions, using a
path to an enum variant instead of to a struct:

```rust
# enum Message {
#     Quit,
#     WriteString(String),
#     Move { x: i32, y: i32 },
# }
let q = Message::Quit;
let w = Message::WriteString("Some string".to_string());
let m = Message::Move { x: 50, y: 200 };
```

Being more specific, the syntax of an enum variant is:

* a [path expression], when the variant has no fields, like `Message::Quit`.
* a [struct expression], when it is a struct enum variant, like
  `Message::Move { x: 50, y: 200 }`.
* a [call expression], when it is a tuple enum variant, like
  `Message::WriteString("Some string".to_string())`.

[struct expression]: expressions/struct-expr.html
[call expression]:   expressions/call-expr.html
[path expression]:   expressions/path-expr.html
