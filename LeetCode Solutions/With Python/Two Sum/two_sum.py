nums = [2,4,5]
target = 7

def twoSum(nums: list, target: int) -> list:
    
    needed = 0
    my_dict = {}
    
    for i in range(len(nums)):
        
        needed = target - nums[i]
        
        if needed in my_dict:
            print([my_dict[needed], i])
            break
        else:
            my_dict[nums[i]] = i # store index of number in dictionary
            
    return

twoSum(nums, target)
        
        