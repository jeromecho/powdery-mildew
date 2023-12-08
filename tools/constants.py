import cv2

COLOR_CVT_MAP = {
  'RGB': cv2.COLOR_BGR2RGB,
  'HSV': cv2.COLOR_BGR2HSV,
  'LAB': cv2.COLOR_BGR2LAB
}

# currently supports only up to 5 different categories on plot
GRAPH_POINT_COLORS = [
  'red',
  'green',
  'blue',
  'magenta',
  'cyan'
]
