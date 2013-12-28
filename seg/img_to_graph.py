import cv2
from scipy.sparse import csr_matrix


def Img3D(img):
  """Returns a 3d version of the given image.

     If the input image is of shape (h, w), then the output will be of shape
     (h, w, 1). Elsewhere, it will return the image as is (h, w, d), for d =
     number of channels.

     Args:
       img: The input image, given as a numpy array.

     Returns: The reshaped image.
  """
  return img.reshape(img.shape[:2] + (-1,))


def Img2Graph(img, alpha=10):
  """Returns a graph representing the underlying image.

     TODO: implement the same for 8-connectivity.
	   add 'sigma' for smoothening the image before derivating.

     Args:
       img:
       alpha:
  """
  # Make sure the image has 3 dimensions
  img = Img3D(img)

  # Image dimensions
  h, w, d = img.shape

  dy = numpy.abs(scipy.ndimage.filters.sobel(img, axis=0)).sum(2)
  dx = numpy.abs(scipy.ndimage.filters.sobel(img, axis=1)).sum(2)

  X, Y = numpy.meshgrid(xrange(w), xrange(h))

  # sub2ind
  I = Y*w + X
  
  xtmp = I[:-1, :].reshape((1, -1))
  ytmp = I[1:, :].reshape((1, -1))
  vtmp = dy[:-1, :].reshape((-1,))
  
  sy = csr_matrix((exp(-alpha*vtmp), numpy.concatenate((xtmp, ytmp), axis=0)),
                  shape=(w*h, w*h))
  
  xtmp = I[:, :-1].reshape((1, -1))
  ytmp = I[:, 1:].reshape((1, -1))
  vtmp = dx[:, :-1].reshape((-1,))
  
  sx = csr_matrix((exp(-alpha*vtmp), numpy.concatenate((xtmp, ytmp), axis=0)),
                  shape=(w*h, w*h))
 
  g = sx + sy
  return g + g.transpose()
