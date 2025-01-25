def edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)
    
    # Create a 2D array to store the edit distances
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Initialize the dp array
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j  # If str1 is empty, all characters of str2 are inserted
            elif j == 0:
                dp[i][j] = i  # If str2 is empty, all characters of str1 are removed
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # If characters are the same, no operation is needed
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],    # Remove
                                   dp[i][j - 1],    # Insert
                                   dp[i - 1][j - 1])  # Replace

    return dp[m][n]

# Get the first string from the user
str1 = input("Enter the first string: ")

# Get the second string from the user
str2 = input("Enter the second string: ")

# Perform the edit distance algorithm
distance = edit_distance(str1, str2)

# Print the edit distance
print("The edit distance between the two strings is:", distance)
