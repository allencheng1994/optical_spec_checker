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
    print(efl_with_distortion(half_fov_degree=88 / 2, imh=1.814, dist=0.025))
    print(
        efl_with_distortion(
            half_fov_degree=88 / 2, imh=0.815 * math.sqrt(1 / 2), dist=-0.01
        )
    )
