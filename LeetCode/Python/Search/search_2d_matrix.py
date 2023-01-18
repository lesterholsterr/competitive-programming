class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Step 1: Choosing a Row Candidate
        target_row = []
        for i in range(len(matrix)):
            if target == matrix[i][0]:
                return True
            elif target < matrix[i][0]:
                target_row = matrix[i-1]
                break
        if len(target_row) == 0:
            target_row = matrix[len(matrix)-1]
        
        # Step 2: Binary Search on Target Row
        left, right = 0, len(target_row)-1
        while left <= right:
            mid = (left + right) // 2
            if target_row[mid] == target:
                return True
            elif target_row[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return False