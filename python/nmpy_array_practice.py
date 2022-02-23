import numpy as np

a = np.array([1,2,3])
b = np.array([(1.5,2,3), (4,5,6)] , dtype = float)
c = np.array([
              [(1.5,2,3), (4,5,6)],
              [(3,2,1), (4,5,6)]
             ], 
             dtype = float)


# print(a)
# print(b)
# print(c)
d = np.arange(10, 25, 5)
print(d)

e = np.full((2,2), 7)
print(e)

f = np.eye(2)
print(f)

# print(np.random.random((2,2)))
g = np.empty((3,2))
# print(g, g[1,1], g.shape, len(g), g.ndim, g.size, g.dtype,g.dtype.name, g.astype(int))



g = a+b
# print('a', a)
# print('b', b)
# print('g', g)

# print(np.subtract(a, b))
# print(np.add(b,a))
# print(np.divide(a,b))

# print(a.view())

# print(b[1:2])

# print(c)
# print(c[1,])
# print(c[1,1,1])

a = np.array([1,2,3,4,5,6])

# print(a)
# print(a[::-1])
# print(a[:-1])
# print(a[-1])

print(b)
print(np.transpose(b))
print(b.ravel())
print(b.reshape(3,2))
print(b.reshape(3,-2))
# print(b[::-1,::-1])

# print(a[a<4])