# Uzz Programming Language

'Uzz' is a simple programming language with a custom syntax and interpreter. The interpreter supports basic functionality like variable assignment, conditionals, loops, and built-in functions like printing and terminal manipulation.

## Features

- Basic Syntax: The language uses keywords like fuzz, ifuzz, elifuzz, thenuzz, etc., for structure.
- Loops & Conditionals: Includes support for for and while loops, as well as if statements.
- Built-In Functions: Provides built-in functions such as low (for printing), fade (for clearing the terminal), and other utility functions.
- Custom Tokenisation and Parsing: The lexer and parser convert the source code into an abstract syntax tree (AST) that the interpreter can execute.

## Installation

Clone the repository to your local machine:
``` 
git clone https://github.com/yourusername/uzz-interpreter.git
cd uzz-interpreter 
```

## Usage

### Running the Interpreter

1. Run the interpreter by running `shuzz.py`.
2. From there you can start typing commands, or you can also run an external file.

Say there is a file named `hello.huzz` that has the following code:
```
low("taper fade")
```
You can run the file in the interpreter by entering the following:
```
uzz > bruzz("hello.huzz")
```

### How It Works

#### Lexer

The lexer takes the source code and tokenises it into a sequence of tokens (e.g., keywords, numbers, operators). Tokens are used by the parser to build an abstract syntax tree (AST).

#### Parser

The parser takes the sequence of tokens and builds an abstract syntax tree (AST) that represents the structure of the code. The parser handles syntax errors and ensures the code follows the correct structure.

#### Interpreter

The interpreter executes the AST by visiting each node, performing the corresponding action (e.g., variable assignment, function call, etc.), and handling built-in functions such as low and fade.

## Why?

I think it's funny to code in brainrot, this is an [esoteric programming language](https://en.wikipedia.org/wiki/Esoteric_programming_language).

## List of Built-In Functions

### dafuq()


The help() function.
Returns a link to the GitHub page.

### low(value)

Prints the (value) to the terminal.

Example:
```
low("Hello, world!");  # Prints "Hello, world!"
```

### fade()

Clears the terminal screen.

### hawk()

Reads a line of input from the user; returns the input as a string.

```
hawk();  # Waits for user input
```

### hawk_tuah()

Reads a line of input from the user and converts it to an integer; returns the input as an integer.

```
hawk_tuah();  # Waits for user input and converts it to an integer
```

### band(value)

Checks if (value) is a number.
Returns `1` if the value is a number, otherwise `0`.

```
band(5);  # Returns 1
band("hello");  # Returns 0
```

### word(value)

Checks if (value) is a string.
Returns `1` if the value is a string, otherwise `0`.

```
word("hello");  # Returns 1
word(5);  # Returns 0
```

### fact(value)

Checks if (value) is a list.
Returns `1` if the value is a list, otherwise `0`.

```
fact([1, 2, 3]);  # Returns 1
fact("hello");  # Returns 0
```

### goon(value)

Checks if (value) is a function.
Returns `1` if the value is a function, otherwise `0`.

```
goon(low);  # Returns 1
goon(5);  # Returns 0
```

### nettspend(list, value)

Adds (value) to the (list).
Returns a new list with (value) added at the end.

```
nettspend([1, 2], 3);  # Returns [1, 2, 3]
```

### fanum(list, index)

Removes an element at (index) from the (list).
Returns the updated list.

```
fanum([1, 2, 3], 1);  # Returns [1, 3]
```

### massive(listA, listB)

Extends (listA) with the elements of (listB).
Returns the updated list with elements from listB added to listA.

```
massive([1, 2], [3, 4]);  # Returns [1, 2, 3, 4]
```

### green_fn(intA, intB)

Requires two integers as arguments.
Returns a random integer between (intA) and (intB).

```
green_fn(1, 10); # Returns a random integer between 1 and 10
```

## Errors/Future Plans

I am aware of bugs in the code, but please feel free to raise issues. In the future I plan to add an autocomplete/intellisense feature.