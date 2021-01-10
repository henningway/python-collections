# Fluent Collections

Fluency for compound data types just like https://laravel.com/docs/collections.

Work in progress.

## Benefits

- **Uniform interface for Dict, List and Tuple, all functions.** Learn once, apply everywhere. Does *map()* work with Dicts as well? What is the slicing syntax again? You just don't care anymore!
- **Direction of reading is direction of data flow.** Chaining lets you write and read transformations in linear sequence, just like a book. Give your brain a rest from all those back-references.
- **Avoid intermediate variables.** Nesting multiple function calls feels unnatural and makes programmers want to break the pattern via assignments. But stateful programs are harder to reason about and are a cause for bugs. 