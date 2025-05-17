# Leetcode 71. Simplify Path

## Time Cost
| Date       | Time Spent       |
|------------|------------------|
| 2025-05-17 | 1 hr 21 min 10 s |

## Method
Initially, I attempted to parse the path character by character, which turned out to be an inefficient approach. I wrote numerous conditions to handle each test case individually. After consulting ChatGPT, I realized that I could simplify the process by using the built-in `split()` function to divide the string by '/'. This made the task much easier. I only needed to check if a part was empty, '.', or '..', and then use a stack to store the valid parts. Finally, I joined the stack with '/' to construct and return the result.