'''
In this module, it is a collection of calculating relative illumination.

'''

import math

def ri_cos_fourth_power(angle_in_degree):
    '''
    You can use this function to estimate the relative illumination by using 
    cosine fourth law.
    
    ex: 
        >>> ri_cos_fourth_power(45)
        >>> 0.25

    '''
    return math.cos(float(angle_in_degree) / 180 * math.pi) ** 4


if __name__ == '__main__':
    print(ri_cos_fourth_power(14.5))

