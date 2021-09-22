'''
This module is going to create a object to store some basic lens' specification.

'''
class LensSpec(object):
    """
    This class is going to store the lens specification.
    """

    def __init__(self):
        self.ttl = None
        self.efl = None
        self.pixel_h = None
        self.pixel_v = None
        self.pixel_size = None
        self.op_dist = None
        self.tv_dist = None
        self.op_dist_theta = None
        self.tv_dist_theta = None
        self.relative_illumination = None
        self.dfov = None
        self.hfov = None
        self.vfov = None
        self.lacl_half_mic = None
        self.lacl_imh = None
        self.fcgs = None
        self.wfno = None
        self.mtfs4 = []
        self.mtft4 = []
        self.mtfs2 = []
        self.mtft2 = []
        self.cra = []

        
        
if __name__ == '__main__':
    pass
