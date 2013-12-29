

class SegParams(object):
  """A class for holding the params needed for performing segmentation."""
  def __init__(self, **kwargs):
    """Initializes from kwargs.

    **kwargs:
      alpha
      alpha_coarse
      block_selection
      sal_thresh
      min_sal_level
      niters
      sig
      conn
    """
    self.alpha = kwargs.get('alpha', 7)
    self.alpha_coarse = kwargs.get('alpha_coarse', 7)
    self.block_selection = kwargs.get('block_selection', 0.2)
    self.sal_thresh = kwargs.get('sal_thresh', 0.2)
    self.min_sal_level = kwargs.get('min_sal_level', 5)
    self.min_sal_vol = kwargs.get('min_sal_vol', 35)
    self.niters = kwargs.get('niters', 20)
    self.sig = kwargs.get('sig', 0.1)
    self.conn = kwargs.get('conn', 4)

class Seg(object):
  def __init__(self, params=None, **kwargs):
    # Set the paraemeters
    self.params = params if params else SegParams(**kwargs)

  def run(self, img):
    """Run the segmentation on the given image."""
    # The affinities in the finest level
    aff = Img2Graph(img, self.params.alpha)

