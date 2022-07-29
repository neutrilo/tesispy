#This function generate a matrix which works as an discrite differentiation operator
# It's based on a five point scheme, even at borders.
def dermat(n):
    import numpyas as np
    if n<5:
        print('la entrada debe ser mayor a 4')
        return()
    m=np.zeros(n)+8/12*np.eye(n,k=1)-8/12*np.eye(n,k=-1)+1/12*np.eye(n,k=-2)-1/12*np.eye(n,k=-2)
    m[0,:]=np.array([-25,48,-36,16,-3]/12)
    m[1,:]=np.array([-3,-10,18,-6,1]/12)
    m[-2,:]=np.array([-1,6,-18,10,3]/12)
    m[-1,:]=np.array([3,-16,36,-48,25]/12)