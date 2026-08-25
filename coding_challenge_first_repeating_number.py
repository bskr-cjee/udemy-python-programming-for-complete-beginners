def first_repeating_number(nums):
    """"Given a list of numbers, return the first number that appears more than once.
    If no number repeats, return None."""

    # Method01
    # my_list = []
    # for num in nums:
    #     if num in my_list:
    #         return num
    #     my_list.append(num)
    # return None

    # Method02
    # for i in range (len(nums)):
    #     for j in range (i+1, len(nums)):
    #         if nums[i] == nums[j]:
    #             return nums[i]
    # return None

    # Method03 (Using Set)
    my_set = set()
    for num in nums:
        if num in my_set:
            return num
        else:
            my_set.add(num)
    return None



# Test cases
print(first_repeating_number([2, 5, 1, 2, 3]))  # Output: 2
print(first_repeating_number([1, 2, 3, 4, 5]))  # Output: None
print(first_repeating_number([7, 8, 9, 7, 8]))  # Output: 7
print(first_repeating_number([4, 4, 5, 6]))  # Output: 4
print(first_repeating_number([]))  # Output: None
print(first_repeating_number([-1, -2, -3, -1]))  # Output: -1
