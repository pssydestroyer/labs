# Lab 15: Overview of Big Data Technologies

## Tasks:

| Task Number | Description | Example Input | Expected Output |
|-------------|-------------|---------------|-----------------|
| \#1 | Write a function `clean_data()` that takes a long string of data points separated by commas, and uses `map()` to return a list of data points where each is stripped of whitespace and converted to lowercase. | `data = " Apple, Banana , orange "`<br>`cleaned = clean_data(data)`<br>`print(cleaned)` | `['apple', 'banana', 'orange']` |
| \#2 | Create a function `filter_emails()` that takes a long string containing emails, and uses `filter()` to return a list containing only valid email addresses. An email is valid if it contains exactly one '@' symbol. | `emails = "mail us test@example.com and invalid-email.com.djwd with example@test.co"`<br>`valid_emails = filter_emails(emails)`<br>`print(valid_emails)` | `['test@example.com', 'example@test.co']` |
| \#3 | Write a function `extract_keywords()` that takes a long string of words, and uses `filter()` to return a list containing words that are longer than a specified length. | `words = "apple pear banana kiwi"`<br>`filtered_words = extract_keywords(words, 4)`<br>`print(filtered_words)` | `['apple', 'banana']` |
| \#4 | Write a function `process_text()` that takes a long string of text data, uses `map()` to strip whitespace, remove special characters, and convert to lowercase, then uses `filter()` to return a list excluding any empty or very short entries. | `texts = " Hello! , Yes? , No. , "`<br>`processed_texts = process_text(texts)`<br>`print(processed_texts)` | `['hello', 'yes', 'no']` |
| \#5 | Write a function `normalize_data()` that takes a long string of numeric values separated by commas and normalizes them to a range between 0 and 1 based on the maximum value. | `numbers = "10, 20,30"`<br>`normalized_numbers = normalize_data(numbers)`<br>`print(normalized_numbers)` | `[0.333, 0.667, 1.0]` |
| \#6 | Develop a function `concatenate_strings()` that takes multiple strings separated by a special character and concatenates them into a single string without the separator. | `data = "hello*world*again"`<br>`concatenated = concatenate_strings(data, '*')`<br>`print(concatenated)` | `'helloworldagain'` |
| \#7 | Create a function `sum_numeric_strings()` that takes a string containing numbers separated by commas and calculates their total sum. | `numbers = "1, 2, test, 3, 4"`<br>`total_sum = sum_numeric_strings(numbers)`<br>`print(total_sum)` | `10` |
| \#8 | Write a function `filter_numbers()` that filters out numbers from a string that are above a specified threshold. | `numbers = "10 test30 40"`<br>`filtered = filter_numbers(numbers, 25)`<br>`print(filtered)` | `[30, 40]` |
| \#9 | Create a function `map_to_squares()` that takes a string of numbers, converts them to their squares, and returns them as a list. | `numbers = "1, 2, 3, 4"`<br>`squared_numbers = map_to_squares(numbers)`<br>`print(squared_numbers)` | `[1, 4, 9, 16]` |