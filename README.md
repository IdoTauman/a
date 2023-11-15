# a

## How does this work?
This is a Brainfuck inspired language, that uses an array of 10000 values with a pointer that selects one of the values and it uses the Brainfuck instrction set.

## Syntax:
- Increment (max 255): a
- Decrement (min 0): aa
- Output selected index (in ASCII): aaa
- Start loop: aaaa
- End loop (loops go one until the selected index is 0 when the loop ends): aaaaa
- Move pointer to the right (max index is 9999, default 0): aaaaaa
- Move pointer to the left (min 0): aaaaaaa 

Please note that there needs to be an empty line after the last line

code.txt contains an example hello world program
