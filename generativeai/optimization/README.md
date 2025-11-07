# Genenrative AI - Optimization

## Table of Contents (ToC)

- [Table of Contents (ToC)](#table-of-contents-toc)
- [Ploon: Path-Level Object Oriented Notation](#ploon-path-level-object-oriented-notation)

## Ploon: Path-Level Object Oriented Notation

References:
* ploon-cli: <https://www.npmjs.com/package/ploon-cli>

```json
 {
  "products": [
    { "id": 1, "name": "Laptop", "price": 999 },
    { "id": 2, "name": "Mouse", "price": 25 }
  ]
}
```

```bash
$ ploon data.json --stats


 ┌─📊 Token Statistics (tiktoken/GPT-4)───┐
 │                                        │
 │  Input:   50 tokens (120 chars)        │
 │  Output:  31 tokens (60 chars)         │
 │                                        │
 │  ✅ Saved 19 tokens (-38.0%)            │
 │  ✅ Saved 60 chars (-50.0%)             │
 │                                        │
 └────────────────────────────────────────┘

[products#2](id|name|price)

1:1|1|Laptop|999
1:2|2|Mouse|25
```
