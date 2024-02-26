def array_mult(A, B):
    def dot(v1, v2):
        ans = 0
        for i in range(len(v1)):
            ans += v1[i] * v2[i]
        return ans
    
    def transpose(A):
        AT = []
        for i in range(len(A[0])):
            col = []
            for j in range(len(A)):
                col.append(A[j][i])
            AT.append(col)
        return AT
    
    prod = []
    BT = transpose(B)
    for row in A:
        v = []
        for col in BT:
            v.append(dot(row, col))
        prod.append(v)
    return prod

M1 = [[1, 2, 3], [-2, 3, 7]]
M2 = [[1,0,0],[0,1,0],[0,0,1]]
print(array_mult(M1, M2))

position = [10,8,0,5,3]
speed = [2,4,1,1,3]
pair = [[p, s] for p, s in zip(position, speed)]

print(pair)
print(sorted(pair)[::-1])