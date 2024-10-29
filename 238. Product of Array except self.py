nums = [1,2,3,4]
n = len(nums)

result = [1] * n # [1, 1, 1, 1]
prefix = [1] * n
suffix = [1] * n

for i in range(1, n):
    prefix[i] = prefix[i - 1] * nums[i - 1]

# Build the suffix product array
for i in range(n - 2, -1, -1):
    suffix[i] = suffix[i + 1] * nums[i + 1]

# Multiply prefix and suffix to get the result
for i in range(n):
    result[i] = prefix[i] * suffix[i]

print(result)