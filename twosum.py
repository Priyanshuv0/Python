def twoSum(nums,target):
    hashmap={}
    for i in range(len(nums)):
        diff=target-nums[i]
        if diff in hashmap:
            return [hashmap[diff],i]
        hashmap[nums[i]]=i
        print("=>",i)
        print(hashmap)
twoSum([1,2,3,4,5,1],6)