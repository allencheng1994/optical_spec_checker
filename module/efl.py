'''
It's a collection of calculating efl method.


'''
import math


def efl_with_distortion(half_fov_degree, imh, dist=0):
    '''
    Calculating the efl with optical distortion

    ex1:
        >>> efl_with_distortion(half_fov_degree=44, imh=1.814, dist=0)
        >>> 1.87845198922

    ex2:
        >>> efl_with_distortion(half_fov_degree=44, imh=1.814, dist=0.02)
        >>> 1.84161959727
    '''

    return imh / (1 + dist) / math.tan(float(half_fov_degree) / 180 * math.pi)


if __name__ == '__main__':
    print(efl_with_distortion(half_fov_degree=78.6/2, imh=1.028, dist=0.03))
    print(efl_with_distortion(half_fov_degree=70.9/2, imh=0.896, dist=0.03))
    print(efl_with_distortion(half_fov_degree=43.6/2, imh=0.504, dist=0.03))
    print(efl_with_distortion(half_fov_degree=83.5/2, imh=1.128, dist=0.06))

