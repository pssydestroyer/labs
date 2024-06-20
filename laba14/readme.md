# Boolean Expressions and Conditional Statements

## Tasks:

| Task Number | Description | Example Input | Expected Output |
|-------------|-------------|---------------|-----------------|
| \#1 | Write a function `check_truth` that takes three boolean parameters (`a`, `b`, `c`) and returns the result of the expression `(a and b) or c`. | `print(check_truth(True, False, True))` | `True` |
| \#2 | Write a function `logical_equivalence` that takes two boolean parameters and returns `True` if they are logically equivalent, otherwise `False`. | `print(logical_equivalence(True, True))`<br>`print(logical_equivalence(True, False))` | `True`<br>`False` |
| \#3 | Write a function `xor` that takes two boolean arguments and returns `True` if exactly one of the arguments is `True`. | `print(xor(True, False))`<br>`print(xor(True, True))` | `True`<br>`False` |
| \#4 | Write a function `greet` that takes a boolean value. If `True`, the function should return "Hello, World!", otherwise it should return "Goodbye, World!". | `print(greet(True))`<br>`print(greet(False))` | `"Hello, World!"`<br>`"Goodbye, World!"` |
| \#5 | Write a function `nested_condition` that takes three integers (`x`, `y`, `z`). The function should return "All same" if all three are equal, "All different" if they are all different, and "Neither" otherwise. | `print(nested_condition(3, 3, 3))`<br>`print(nested_condition(3, 4, 5))` | `"All same"`<br>`"All different"` |
| \#6 | Write a function `count_true` that accepts a list of boolean values and returns the count of how many are `True`. | `print(count_true([True, False, True, False, True]))` | `3` |
| \#7 | Write a function `parity` that accepts an integer and returns `True` if the number of 1s in the binary representation of the number is even, otherwise `False`. | `print(parity(3))` | `False` (binary `11`) |
| \#8 | Write a function `majority_vote` that takes three boolean inputs and returns `True` if more than half of them are `True`, otherwise `False`. | `print(majority_vote(True, True, False))` | `True` |
| \#9 | Write a function `switch` that takes a boolean value and returns its opposite. | `print(switch(True))` | `False` |
| \#10 | Write a function `ternary_check` that simulates a ternary operator. It takes three parameters: a boolean condition, a result if true, and a result if false. It returns the corresponding result based on the condition. | `print(ternary_check(True, "Yes", "No"))` | `"Yes"` |
| \#11 | Write a function `validate` that takes three booleans (`x`, `y`, `z`) and returns `True` if `x` is `True` or both `y` and `z` are `True`, otherwise `False`. | `print(validate(True, False, True))` | `True` |
| \#12 | Write a function `chain_check` that evaluates a sequence of conditions. It takes three integers and returns "Increasing" if they are in strictly increasing order, "Decreasing" if in strictly decreasing order, or "Neither" otherwise. | `print(chain_check(1, 2, 3))`<br>`print(chain_check(3, 2, 1))` | `"Increasing"`<br>`"Decreasing"` |
| \#13 | Write a function `filter_true` that takes a list of boolean values and returns a new list containing only the `True` values. | `print(filter_true([True, False, True, False]))` | `[True, True]` |
| \#14 | Write a function `multiplexer` that takes four parameters: three boolean inputs and one integer. If the first boolean is `True`, return double the integer. If the second is `True`, return triple the integer. If the third is `True`, return the integer minus five. If none are `True`, return the integer unchanged. | `print(multiplexer(False, False, True, 10))` | `5` |