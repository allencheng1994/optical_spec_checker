'''
In this module, it is a collection of calculating relative illumination.

'''

import math

def ri_cos_fourth_power(half_fov):
    '''
    You can use this function to estimate the relative illumination by using 
    cosine fourth law.
    
    half_fov: degree

    ex: 
        >>> ri_cos_fourth_power(45)
        >>> 0.25

    '''
    return math.cos(float(half_fov) / 180 * math.pi) ** 4


def ri_fov_cra(half_fov, cra):
    '''
    half_fov: degree
    cra: degree

    ex:
        >>> ri_fov_cra(77 / 2, 34)
        >>> 0.3973812063000361

    '''

    return math.cos(float(half_fov) / 180 * math.pi) ** 3 * math.cos(float(cra) / 180 * math.pi)




if __name__ == '__main__':
    print(ri_fov_cra(77 / 2, 34))

