# 'uzz' Programming Language

'uzz' is a simple JIT-compiled programming language with a custom syntax and compiler. The interpreter supports basic functionality like variable assignment and re-assignment, conditionals, and the ability to call functions.

## Features

- Dyanmic syntax: the language is supposed to be brainrotted, but it has support for regular syntax if the brainrot version is too overwhelming.
- Conditionals: Includes support for if statements.
- Custom Tokenisation and Parsing: The lexer and parser convert the source code into an abstract syntax tree (AST) that the interpreter can execute.
- Thorough debug and error handling: The tokenisation process and the output are well explained.

## Installation

Clone the repository to your local machine:
``` 
git clone https://github.com/Crotchwhistle/uzz.git
cd uzz-interpreter 
```

## Usage

### Running the Compiler

1. Ensure that in `main.py` the correct test file is set. Currently this is `tests/test.uzz`.
2. Run the interpreter by running `python main.py` in your terminal.

Say the file `test.uzz` has the following code:
```
fn add(a: int, b: int) -> int {
    return a + b;
}

fn main() -> int {
    return add(200, 100);
}
```
You can run the file in the terminal by entering the following:
```
python main.py
```
And it will have the output:
```
Progruzz returned: 300
=== Execuzzed in 0.0 ms. ===
```

## Dynamic Syntax

In `Token.py` you can find two dictionaries: KEYWORDS and ALT_KEYWORDS. These are set up so that you can map both dictionaries to work with each other as the syntax. The KEYWORDS dictionary is the regular non-brainrot syntax that makes sense, and the ALT_KEYWORDS is the brainrot dictionary. You can choose to code exclusively in either brainrot or regularly, or mix both.

For example, the code in the example above could be re-written as:
```
bruzz add(a: int, b: int) jugg int {
    huzz a + b;
}

bruzz main() jugg int {
    huzz add(200, 100);
}
```
or you could mix and match the syntax:
```
fn add(a: int, b: int) -> int {
    huzz a + b;
}

bruzz main() jugg int {
    return add(200, 100);
}
```
Both will return the same result.

## Built-in Functions

### `printf` function

The `printf` function can be used like this:

```
fn add(a: int, b: int) -> int {
    return a + b;
}

fn main() -> int {
    printf("goat %i", add(2, 3));
    return add(1, 2);
}
```

This will return `goat 5`.

### `while` loops

The following code:

```
fn main() -> int {
    let a: int = 0;

    while a < 10 {
        printf("a = %i\n", a);
        a = a + 1;
    }

    return a;
}
```

will return this:

```
a = 0
a = 1
a = 2
a = 3
a = 4
a = 5
a = 6
a = 7
a = 8
a = 9

Progruzz returned: 10
=== Execuzzed in 0.0 ms. ===
```

### How It Works

#### Lexer

The lexer takes the source code and tokenises it into a sequence of tokens (e.g., keywords, numbers, operators). Tokens are used by the parser to build an abstract syntax tree (AST).

#### Parser

The parser takes the sequence of tokens and builds an abstract syntax tree (AST) that represents the structure of the code. The parser handles syntax errors and ensures the code follows the correct structure.

#### Compiler

The interpreter executes the AST by visiting each node, performing the corresponding action (e.g., variable assignment, function call, etc.).

## Why?

I think it's funny to code in brainrot, this is an [esoteric programming language](https://en.wikipedia.org/wiki/Esoteric_programming_language).

## Errors/Future Plans

Currently there shouldn't be many bugs in the code. The prevous version of this programming language can be found in the `gruzz` folder. I found that this version had many errors that had unintentionally become features that were too hard to fix. Overall, it wasn't very up to date or sustainable to keep working on. So, I've completely changed it. Built-in functions and loops will be introduced at a later date.