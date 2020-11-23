'''
This module is the collection of mtf calculation.

'''

import math

def line_pair_ff(pixel_size):
    '''
    You can use this function to calculate the full frequency of that pixel size.

    The unit of pixel size is um.

    The unit of line pair is lp/mm.
    ex:
        >>> line_pair_ff(1.4)
        >>> 357.14285714285717
    '''

    return 1000 / pixel_size / 2


def mtf_limit_circular(fno, wavelength, target_lp):
    '''
    You can use this function to calculate the mtf limitation by giving f number, wavelength and target frequency.
    The unit of wavelength is um.

    ex:
        >>> mtf_limit(fno=2, wavelength=0.55, target_lp=112)
        >>> 357.14285714285717
    '''
    cutoff_lp = 1000 / fno / wavelength
    lp_ratio = target_lp / cutoff_lp
    return 2 / math.pi * (math.acos(lp_ratio) - (lp_ratio) * (1 - lp_ratio ** 2) ** 0.5)



if __name__ == "__main__":
    print(mtf_limit(fno=2, wavelength=0.55, target_lp=112))
