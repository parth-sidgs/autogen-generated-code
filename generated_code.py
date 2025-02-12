        def longest_valid_parentheses(s: str) -> int:
    """
    Finds the length of the longest valid (well-formed) parentheses substring.

    Args:
        s: The input string containing only '(' and ')'.

    Returns:
        The length of the longest valid parentheses substring.
    """

    n = len(s)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest valid substring ending at index i
    dp = [0] * n

    max_len = 0

    for i in range(1, n):
        if s[i] == ')':
            if s[i - 1] == '(':
                # Case: ()
                dp[i] = dp[i - 2] + 2 if i >= 2 else 2
            elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                # Case: (()) 
                if i - dp[i - 1] - 2 >= 0:
                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                else:
                    dp[i] = dp[i - 1] + 2

            max_len = max(max_len, dp[i])

    return max_len


