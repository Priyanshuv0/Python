class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        n=len(nums)
        pre=[0]*n
        for i,num in enumerate(nums[1:]):
            if num-nums[i]<=maxDiff:
                pre[i+1]=pre[i]
            else:
                pre[i+1]=pre[i]+1
        
        ans=[]
        for u,v in queries:
            ans.append(pre[u]==pre[v])
        return ans

        
