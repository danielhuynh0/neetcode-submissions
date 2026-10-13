class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = {}
        for num in nums:
            if num in num_counts:
                num_counts[num] = num_counts[num] + 1
            else:
                num_counts[num] = 1

        max_count = -math.inf
        min_count = math.inf
        for num, count in num_counts.items():
            max_count = max(max_count, count)
            min_count = min(min_count, count)
        
        tot_range = max_count - min_count 
        if tot_range == 0:
            n = 1
        else:
            n = len(num_counts)
        buckets = [[] for _ in range(n)]        
        for num, count in num_counts.items():
            res = 0 if n == 1 else n * ((count - min_count)/(max_count - min_count))
            res = math.floor(res)
            if res == n:
                buckets[-1].append((num, count))
            else:
                buckets[res].append((num, count))

        sorted_counts = []
        for bucket in buckets:
            if len(bucket) == 0:
                continue
            if len(bucket) == 1:
                sorted_counts.append(bucket[0][0])
                continue
            bucket.sort(key=lambda x: x[1])
            for item in bucket:
                sorted_counts.append(item[0])
        
        ans = []
        for i in range(k):
            ans.append(sorted_counts[len(sorted_counts) - 1 - i])

        return ans
