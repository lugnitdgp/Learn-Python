# Example input:
# 5
# 1 2 3 4 5
# Example Output: n = 5, data = [1, 2, 3, 4, 5]
n, data = input(), [int(i) for i in input().strip().split()]

# How to take input from multiple lines
# Will take input until sees a blank line (sentinel)
# Example input:
# 1 2 3
# 4 5
# Example Output: user_input = '1 2 3 4 5'
sentinel = ''
user_input = '\n'.join(iter(input, sentinel)).replace('\n', ' ')

# Example input:
# 1 2 3 4
# Example Output: var1 = 1, var2 = 2, var3 = 3, var4 = 4, such that var1, var2, var3, var4 are of type string
var1, var2, var3, var4 = input().split()

# Example input:
# 1 2 3 4
# Example Output: var1 = 1, var2 = 2, var3 = 3, var4 = 4, such that var1, var2, var3, var4 are of type int
var1, var2, var3, var4 = map(int, input().split())

# Example input:
# 1 2 3
# 1 2 3
# ...
# 1 2 3
while True:
	try:

		var1, var2, var3 = map(int, input().split())

	except EOFError:
		break