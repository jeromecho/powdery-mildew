"""
RUN INSTRUCTIONS:

python3 cc_gui.py dir_path color_channel

** dir_path - relative path (e.g., '../test')
** color_channel - 'RGB', 'HSV', 'LAB'
** mode - 'READ', 'SAVE_PLOT'
** category1? - any string
** category2? - any string
** etc... - 
"""
import cv2
import sys
from os import listdir
import matplotlib.pyplot as plt
from constants import COLOR_CVT_MAP, GRAPH_POINT_COLORS

PLOT = []

def pipe_cl_args():
  global dir_path
  global color_channel
  global mode
  global categories

  dir_path = sys.argv[1]
  color_channel = sys.argv[2].upper()
  mode = sys.argv[3]
  categories = []

  if len(sys.argv) >= 5:
    for i in range(4, len(sys.argv)):
      categories.append(sys.argv[i].upper())

def get_axis_labels():
  if color_channel == 'RGB':
    return ['R', 'G', 'B']
  elif color_channel == 'HSV':
    return ['H', 'S', 'V']
  else:
    return ['L', 'A', 'B']

def get_color_channel_value(event, x, y, flags, im_payload):
    [im, im_path] = im_payload
    if event == cv2.EVENT_LBUTTONDOWN:
        im = cv2.cvtColor(im, COLOR_CVT_MAP[color_channel])
        print("{} values for {} at pixel ({}, {}): {}".format(color_channel, im_path, x, y, im[y, x]))

# MUTATES
def plot_color_channel_value(event, x, y, flags, im_payload):
    [im, im_path, plot_model ] = im_payload
    if event == cv2.EVENT_LBUTTONDOWN:
        im = cv2.cvtColor(im, COLOR_CVT_MAP[color_channel])
        print("{} values added for {} at pixel ({}, {}): {}".format(color_channel, im_path, x, y, im[y, x]))
        plot_model['values'].append(im[y, x])

def cc_gui_read():
  for im_path in listdir(dir_path):
    rel_path = dir_path + '/' + im_path
    im = cv2.imread(rel_path)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', get_color_channel_value, [ im, im_path ])
    cv2.imshow('image', im)
    cv2.waitKey(0)
  cv2.destroyAllWindows()

def collect_data_points():
  for i in range (len(categories)):
    plot_model = {
      'name': categories[i],
      'color': GRAPH_POINT_COLORS[i],
      'values': []
    }

    print(f'Now collecting data points for {categories[i]}')
    for im_path in listdir(dir_path):
      rel_path = dir_path + '/' + im_path
      im = cv2.imread(rel_path)
      cv2.namedWindow('image')
      cv2.setMouseCallback('image', plot_color_channel_value, [ im, im_path, plot_model ])
      cv2.imshow('image', im)
      cv2.waitKey(0)

    PLOT.append(plot_model)
    cv2.destroyAllWindows()

def plot_3d_data():
  fig = plt.figure()
  ax = plt.axes(projection='3d')
  [ xlabel, ylabel, zlabel ] = get_axis_labels()
  ax.set_xlabel(xlabel)
  ax.set_ylabel(ylabel)
  ax.set_zlabel(zlabel)

  # plot data points
  for plot_model in PLOT:
    for value in plot_model['values']:
      ax.scatter3D(value[0], value[1], value[2], color = plot_model['color'])
    print(plot_model['color']  + '-' + plot_model['name'])
  plt.show()

def cc_gui_save_plt():
  # collect data points
  collect_data_points()
  plot_3d_data()

def route_gui_tool():
  if mode == 'READ':
    cc_gui_read()
  else:
    cc_gui_save_plt()

pipe_cl_args()
route_gui_tool()


