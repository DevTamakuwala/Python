nums = list(map(int, input("Enter integers: ").split()))
unique_nums = list(set(nums))
unique_nums.sort(reverse=True)

print("Sorted (desc):", unique_nums)
if len(unique_nums) > 1:
    print("Second highest:", unique_nums[1])
else:
    print("No second highest value")
