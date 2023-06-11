import os

TRAIN_IMAGE = "./base_data/training/images/"
TRAIN_LABEL = "./base_data/training/labels/"
VALID_IMAGE = "./base_data/validation/images/"
VALID_LABEL = "./base_data/validation/labels/"
TEST_IMAGE = "./base_data/testing/images/"
TEST_LABEL = "./base_data/testing/labels/"

# Define RGB values for Mapillary classes
# ATTENTION: THESE ARE RGB VALUES, NOT BGR
ROAD_COLOR = (128, 64, 128)
SIDEWALK_COLOR = (244, 35, 232)
BUILDING_COLOR = (70, 70, 70)
WALL_COLOR = (102, 102, 156)
FENCE_COLOR = (190, 153, 153)
POLE_COLOR = (153, 153, 153)
TRAFFIC_SIGN_COLOR = (250, 170, 30)
TREE_COLOR = (220, 220, 0)
CAR_COLOR = (0, 0, 142)
MOTORCYCLE_COLOR = (0, 0, 230)
BICYCLE_COLOR = (119, 11, 32)

def progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
