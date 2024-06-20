# Lab 11: Advanced Working with Arrays of Numbers in Python

| Task Number | Description | Example Input | Expected Output |
|-------------|-------------|---------------|-----------------|
| \#1 | Create a function `sum_of_squares` that accepts an array of numbers and returns the sum of the squares of each number. | `print(sum_of_squares([1, 2, 3]))` | 14 |
| \#2 | Create a function `filter_and_sum` that accepts an array of numbers and returns the sum of all the elements that are greater or equal than the average of the array. | `print(filter_and_sum([1, 2, 3, 4, 10]))` | 14 |
| \#3 | Create a function `sort_by_frequency` that sorts an array of numbers based on the frequency of each element from highest to lowest. If two numbers have the same frequency, the smaller number should come first. | `print(sort_by_frequency([4, 6, 2, 6, 4, 4, 6]))` | [4, 4, 4, 6, 6, 6, 2] |
| \#4 | Create a function `find_missing_number` that finds the missing number in an array containing all integers from 1 to n except one. Assume the array has no duplicates. | `print(find_missing_number([1, 2, 4, 5]))` | 3 |
| \#5 | Create a function `longest_consecutive` that finds the length of the longest consecutive elements sequence in an unsorted array. | `print(longest_consecutive([100, 4, 200, 1, 3, 2]))` | 4 |
| \#6 | Create a function `rotate_array` that rotates the array to the right by k steps, where k is non-negative. | `print(rotate_array([1, 2, 3, 4, 5], 2))` | [4, 5, 1, 2, 3] |
| \#7 | Create a function `array_of_products` that calculates an array of products of all numbers except the one at the current index without using division. | `print(array_of_products([1, 2, 3, 4]))` | [24, 12, 8, 6] |
| \#8 | Create a function `max_subarray_sum` that finds the maximum sum of a contiguous subarray within a one-dimensional array of numbers. | `print(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))` | 6 |
| \#9 | Create a function `spiral_order` that returns all elements of a 2D matrix in spiral order. | `print(spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))` | [1, 2, 3, 6, 9, 8, 7, 4, 5] |
| \#10 | Create a function `k_closest_points` that finds the k closest points to the origin (0, 0) in a 2D plane, given an array of coordinate points. | `print(k_closest_points([(1, 2), (1, 1), (3, 4)], 2))` | [(1, 1), (1, 2)] |
