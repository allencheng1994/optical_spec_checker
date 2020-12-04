from module import * 

if __name__ == '__main__':
    print(efl_with_distortion(half_fov_degree=78.6/2, imh=1.028, dist=0.03))
    print(efl_with_distortion(half_fov_degree=70.9/2, imh=0.896, dist=0.03))
    print(efl_with_distortion(half_fov_degree=43.6/2, imh=0.504, dist=0.03))
    print(efl_with_distortion(half_fov_degree=83.5/2, imh=1.128, dist=0.06))