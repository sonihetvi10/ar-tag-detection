import cv2 as cv


def draw_contours(img_frame):
    """  find and draw contours on the main frame
    :param img_frame: a frame from the video
    :return: image with contours and the contours matrix
    """
    _, frame_thresh = cv.threshold(cv.cvtColor(img_frame, cv.COLOR_BGR2GRAY), 200, 255, 0)
    contours, _ = cv.findContours(frame_thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    return contours


def get_h_matrix(orientation, x, y):
    """ get H-matrix for detected orientation
    :param orientation: orientation from get orientation function
    :param x:
    :param y:
    :return:
    """
    orientations = ['top_right', 'top_left', 'bottom_right', 'bottom_left']
    # TODO: return H-matrix not orientations
    # Returning orientations only for stub implementation
    return orientations


def get_orientation(input_img):
    """ get orientation from the image frame
    :param input_img: image frame from the video
    :return: orientation of the tag
    """

    # TODO: implement algorithm to deduce orientation from input image
    orientations = ['top_right', 'top_left', 'bottom_right', 'bottom_left']
    # TODO: return correct orientation after deduction
    # Returning top-right as orientation only for stub implementation
    return orientations[0]


def get_tag_td(input_img, orientation):
    """
    :param input_img:
    :param orientation:
    :return:
    """

    # TODO: implement algorithm to deduce orientation from input image
    tag_id = orientation
    return tag_id
