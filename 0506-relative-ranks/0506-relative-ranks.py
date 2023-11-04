class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans =[]
        rank = sorted(score,reverse=True)
        n = len(score)
        mp = defaultdict(str)
        for i in range(0,n):
            if  i == 2:
                mp[rank[i]] ="Bronze Medal"
            elif i == 1:
                mp[rank[i]] = "Silver Medal"
            elif i == 0:
                mp[rank[i]] = "Gold Medal"
            else:
                mp[rank[i]] = str(i+1)
        for i in range(n):
            ans.append(mp[score[i]])
        return ans

        