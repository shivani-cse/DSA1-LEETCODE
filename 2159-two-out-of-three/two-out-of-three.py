class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s1,s2,s3=set(nums1),set(nums2),set(nums3)
        count={}
        for num in s1:
            count[num] = count.get(num, 0) + 1
        for num in s2:
            count[num] = count.get(num, 0) + 1
        for num in s3:
            count[num] = count.get(num, 0) + 1
        result=[]
        for num in count:
            if count[num]>=2:
                result.append(num)
        return result                

