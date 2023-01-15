# import numpy as np

# n=3
# onesk = np.ones((n,n))
# print(onesk)


# print('We want this matrix\n')
# print(np.array([[1.,0.,0.],[1.,1.,0.],[1.,1.,1.]])) ## ต่ำแหน่งแรก = แถวแรก ..
                #[1 0 0
                # 1 1 0
                #]1 1 1



# onesk = np.ones((n,n))
# zero_xyindx = [(0,1),(0,2),(1,2)]
# xyindx = tuple(zip(*zero_xyindx))

# print(xyindx)
# print('Notice ((all x),(all y))')

# onesk[xyindx] = 0
# print(onesk)


import numpy as np

n = 3

def Problem1(n): 
    onesk = np.ones((n,n))
    indx =  [(x,y) for x in range(n) for y in range(n) if x<y]
    xyindx = tuple(zip(*indx))
    onesk[xyindx] = 0
    return onesk

print(Problem1(n))
# n = 4

# onesk = np.ones((n,n))
# print(onesk)

# indx =  [(0,1),(0,2),(1,2)]
# print(indx)

# xyindx = tuple(zip(*indx))
# print(xyindx)

# onesk[xyindx] = 0
# print(onesk[xyindx])


