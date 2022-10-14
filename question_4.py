'''
This code is super gross but it works. Sorry in advance.
'''

import numpy as np
from matplotlib import pyplot as plt
from numpy.linalg import eig

def main():
    M = np.array([[1, 0, -1, 1, 1], [0, 1, 0, 0, 1], [-1, 0, -1, -1, -1], [1, 0, -1, 0, 1], [1, 1, -1, 1, -1]])

    #Generate rand vector
    output = np.random.randint(1,100,size = (5,1))
    #Normalize vector
    output_mag = np.abs(output)
    max_index = np.argmax(output_mag)
    output = output/(output[max_index])
    original = output

    iterations = np.array
    print(type(iterations))
    for i in range(25):
        output = np.matmul(M,output)
        output_mag = np.abs(output)
        max_index = np.argmax(output_mag)
        output = output/(output[max_index])
        if i == 0 or i == 2 or i == 4 or i == 9 or i == 24:
            iterations = np.append(iterations, output)


    x_axis = [1,2,3,4,5]
    i_conv = {0:1, 1:3, 2:5, 3:10, 4:25}
    #uncomment for part b
    for i in range(5):
        plt.plot(x_axis, [iterations[(5*i)+1], iterations[(5*i)+2],iterations[(5*i)+3], iterations[(5*i)+4], iterations[(5*i)+5]], label = "iter " + str(i_conv[i]))
    plt.plot(x_axis, original, label = "original")
    




    #part c
    vec_a = np.random.randint(1,100,size = (5,1))
    vec_b = np.random.randint(1,100,size = (5,1))
    vec_c = np.random.randint(1,100,size = (5,1))
    vec_d = np.random.randint(1,100,size = (5,1))
    vec_e = np.random.randint(1,100,size = (5,1))

    #Wow. THis is really bad. Who let me code??!?
    for i in range(25):
        output_mag_a = np.abs(vec_a)
        max_index_a = np.argmax(output_mag_a)
        vec_a = vec_a/(vec_a[max_index_a])
        vec_a = np.matmul(M,vec_a)

        output_mag_b = np.abs(vec_b)
        max_index_b = np.argmax(output_mag_b)
        vec_b = vec_b/(vec_b[max_index_b])
        vec_b = np.matmul(M,vec_b)

        output_mag_c = np.abs(vec_c)
        max_index_c = np.argmax(output_mag_c)
        vec_c = vec_c/(vec_c[max_index_c])
        vec_c = np.matmul(M,vec_c)

        output_mag_d = np.abs(vec_d)
        max_index_d = np.argmax(output_mag_d)
        vec_d = vec_d/(vec_d[max_index_d])
        vec_d = np.matmul(M,vec_d)

        output_mag_e = np.abs(vec_e)
        max_index_e = np.argmax(output_mag_e)
        vec_e = vec_e/(vec_e[max_index_e])
        vec_e = np.matmul(M,vec_e)

    vec_a = vec_a/(vec_a[max_index_a])
    vec_b = vec_b/(vec_b[max_index_b])
    vec_c = vec_c/(vec_c[max_index_c])
    vec_d = vec_d/(vec_d[max_index_d])
    vec_e = vec_e/(vec_e[max_index_e])


    #plt.plot(x_axis, vec_a, label = "vec 1")
    #plt.plot(x_axis, vec_b, label = "vec 2")
    #plt.plot(x_axis, vec_c, label = "vec 3")
    #plt.plot(x_axis, vec_d, label = "vec 4")
    #plt.plot(x_axis, vec_e, label = "vec 5")
    #plt.legend()
    #plt.show()


    #Part d
    a, b = eig(M)
    print(a)
    print(b)
    eigvec = [b[0][0], b[1][0],b[2][0], b[3][0], b[4][0]]
    eigvec = eigvec/min(eigvec)
    print("eigenvector normalized: ")
    print(eigvec)
    plt.plot(x_axis, eigvec, label = "eigvector")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()