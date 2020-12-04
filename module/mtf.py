'''
This module is the collection of mtf calculation.

'''

import math

def line_pair_ff(pixel_size):
    '''
    You can use this function to calculate the full frequency of that 
    pixel size.

    The unit of pixel size is um.
    The unit of line pair is lp/mm.
    ex:
        >>> line_pair_ff(1.4)
        >>> 357.14285714285717
    '''

    return 1000 / pixel_size / 2


def mtf_limit_circular(fno, wavelength, target_lp):
    '''
    You can use this function to calculate the mtf limitation by giving f 
    number, wavelength and target frequency.

    The unit of wavelength is um.
    The unit of line pair is lp/mm.

    ex:
        >>> mtf_limit_circular(fno=2, wavelength=0.55, target_lp=112)
        >>> 0.8435346141315045
    '''
    cutoff_lp = 1000 / fno / wavelength
    lp_ratio = target_lp / cutoff_lp
    return 2 / math.pi * (math.acos(lp_ratio) - (lp_ratio) * (1 - lp_ratio**2)**0.5)


def mtf_limit_circular_photopic(fno, target_lp):
    '''
    You can use this function to calculate the mtf limitation by giving f 
    number and target frequency.

    wavelength_rgb = [0.47, 0.51, 0.555, 0.61, 0.65]
    weights = [0.091, 0.053, 1, 0.053, 0.107]

    ex:
        >>> mtf_limit_circular_photopic(fno=2, target_lp=112)
        >>> 0.841483050394301
    '''
    wavelength_rgb = [0.47, 0.51, 0.555, 0.61, 0.65]
    weights = [0.091, 0.053, 1, 0.053, 0.107]
    mtf_limit = []
    for wavelength, weight in zip(wavelength_rgb, weights):
        mtf_limit.append(mtf_limit_circular(fno, wavelength, target_lp) * weight)
    return sum(mtf_limit) / sum(weights)


if __name__ == "__main__":
    print(mtf_limit_circular_photopic(2.8, 112))
