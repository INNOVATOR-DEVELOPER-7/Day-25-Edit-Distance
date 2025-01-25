# Day-25-Edit-Distance
Here's Python Program for Edit Distance. Day 25 of Day 365.
1. Definition: Edit Distance is a way of quantifying how different two strings are by counting the minimum number of operations needed to transform one string into another.

2. Operations: There are three primary operations:
   - Insertion: Adding a character.
   - Deletion: Removing a character.
   - Substitution: Replacing one character with another.

3. Goal: The goal is to find the smallest number of these operations required to convert one string into another.

4. Example Scenario:
   - Strings: Let's say we have two strings: `kitten` and `sitting`.
   - Step-by-Step Transformation:
     - kitten → sitten (substitution of 'k' to 's')
     - sitten → sittin (substitution of 'e' to 'i')
     - sittin → sitting (insertion of 'g')

5. Calculation Approach: The process usually involves a matrix (table) where:
   - Rows represent characters of the first string plus one for the initial state.
   - Columns represent characters of the second string plus one for the initial state.
   - Cells are filled with the minimum cost of operations to transform substrings up to that point.

6. Filling the Table:
   - Initialize: Start by initializing the table's first row and first column.
   - Fill: Iterate through the table, filling each cell based on the minimum edit distance calculated by comparing:
     - The cost of insertion, deletion, or substitution.

7. Result: The value in the bottom-right cell of the table will be the edit distance between the two strings.

8. Uses: This method is often used in:
   - Spell-checkers.
   - DNA sequence analysis.
   - Natural Language Processing tasks.

That's the step-by-step explanation of Edit Distance without using code.
