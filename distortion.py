'''
In this module, it is a collection of distortion calculating method.

'''

import math


def op_dist_real(real, ideal):
    '''
    This function is going to estimate the optical distortion with real 
    image height and ideal image height.

    ex:
        >>> op_dist_real(real = 1.814, ideal = 1.714)
        >>> 0.0583430571762

    '''

    return (real - ideal) / ideal


def tv_dist_real(op_dist_real_img_a, op_dist_real_img_b):
    '''
    This function is going to estimate the TV distortion with two optical 
    distortion.

    ex:
        >>> tv_dist_real(0.02, 0.01)
        >>> 0.01

    '''

    return op_dist_real_img_a - op_dist_real_img_b


if __name__ == '__main__':
    # print(op_dist_real(real = 1.814, ideal = 1.714))
    pass
