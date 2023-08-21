class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        # Overall: Brute force is easy, but unable to come up with linear time solution because I forgot tuples existed
        # Leaps
        # - I need to store both temperature and index information, what kind of data structure should I use?
        # - What conditions are required such that temperatures only needs to be traversed once?

        # Initial Solution (5 minutes)
        # O(n^2) time, times out on large test cases
        answers = []
        count = 1
        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    answers.append(count)
                    count = 1
                    break
                elif j == len(temperatures) - 1:
                    answers.append(0)
                    count = 1
                else:
                    count += 1
        answers.append(0)
        return answers
        
        # Neetcode Solution (my implementation)
        answer = [0] * len(temperatures)
        stack = []
        
        for i, t in enumerate(temperatures):
            while len(stack) > 0 and t > stack[len(stack)-1][0]:
                answer[stack[len(stack)-1][1]] = i - stack[len(stack)-1][1]
                stack.pop()
            stack.append((t, i))
        
        return answer
    
        # Neetcode Solution (with syntactic sugar)
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # index -1 means the last one
                stackT, stackInd = stack.pop() # pop returns a value, assignment from a tuple
                res[stackInd] = (i - stackInd)
            stack.append((t, i))
        return res