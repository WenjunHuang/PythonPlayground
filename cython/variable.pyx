# cython: language_level=3
cdef int i, j, k
cdef float price, margin

def integrate(a,b,f):
    cdef:
        int i
        int N = 2000
        float dx,s = 0.0
    dx = (b - a) / N
    for i in range(N):
        s += f(a+i*dx)
    return s * dx


cdef double golden_ratio
cdef double *p_double
p_double = &golden_ratio
p_double[0] = 1.618
print(golden_ratio)