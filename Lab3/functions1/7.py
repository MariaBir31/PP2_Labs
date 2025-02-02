#function1
def has_33(nums):
    return any(nums[i] == nums[i+1] == 3 for i in range(len(nums) - 1))
print(has_33([1,3,3]))