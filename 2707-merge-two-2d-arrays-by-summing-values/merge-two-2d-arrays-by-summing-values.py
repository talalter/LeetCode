class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        idx1 = idx2 = 0
        res = []
        while idx1 < len(nums1) and idx2 < len(nums2):
            id1, v1 = nums1[idx1]
            id2, v2 = nums2[idx2]
            if id1 == id2:
                res.append([id1, v1+v2])
                idx1 += 1
                idx2 += 1
            elif id1 < id2:
                res.append([id1, v1])
                idx1 += 1
            else:
                res.append([id2, v2])
                idx2 += 1 

        while idx1 < len(nums1):
            id1, v1 = nums1[idx1]
            res.append([id1, v1])
            idx1 += 1

        while idx2 < len(nums2):
            id2, v2 = nums2[idx2]
            res.append([id2, v2])
            idx2 += 1 
        return res
