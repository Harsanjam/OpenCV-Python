"""Fruit Catcher Vision | ObjectDetection.py

This file is responsible for all the computing behind the vision aspects of the game. All the object detection  and
tracking work from webcam input is done here. The Game file calls the get_move method from this file.
"""

import cv2
import numpy


def filter_green(frame):
    """

    Filters out green from video input.

    Top and bottom colour thresholds determine the range of green to pick up.

    Parameters
    ----------
        frame : frame
        The frame from the video input that needs filtering

    Return
    ----------
        cv2.inRange(hsv, top_threshold, bottom_threshold)
            filtered frame where only the green spectrum specified is considered

    Cites
    ----------
    https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html

    """

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    top_threshold = numpy.array([40, 100, 100])
    bottom_threshold = numpy.array([70, 225, 255])

    return cv2.inRange(hsv, top_threshold, bottom_threshold)


def get_contours(frame):
    """

    Finds edged of filtered out objects and makes contours around them. Filtered out objects must be bigger than 5 by
    5 pixles

    Parameters
    ----------
        frame : frame
        The filtered frane that now needs contours around objects

    Return
    ----------
        cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            frame with contours around filtered objects

    Cites
    ----------
    https://www.youtube.com/watch?v=AMFhjir4WgQ

    """

    kernel = numpy.ones((5, 5), numpy.uint8)
    mask = cv2.erode(frame, kernel)
    mask = cv2.blur(mask, (5, 5))

    return cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


def get_bounding_rect(video_input):
    """

    Draws a bounding rectangle areas with contours.

    Video input is taken and a single frame is read. Method calls the filter_green and get_contours methods. Approximate
    shape is taken based on contoured object and a box is drawn around it.

    Parameters
    ----------
        video_input : video input from webcam
        The video input from the webcam

    Return
    ----------
        vertex_x
            X-value of box"s top left corner

    Cites
    ----------
    https://docs.opencv.org/3.4/da/d0c/tutorial_bounding_rects_circles.html

    """
    _, frame = video_input.read()

    mask = filter_green(frame)

    contours, _ = get_contours(mask)

    contours_poly = [None] * len(contours)
    bound_rect = [None] * len(contours)

    for i, c in enumerate(contours):
        contours_poly[i] = cv2.approxPolyDP(c, 20, True)
        bound_rect[i] = cv2.boundingRect(contours_poly[i])

    vertex_x = 0

    for i in range(len(contours)):
        vertex_x = int(bound_rect[i][0])
        vertex_y = int(bound_rect[i][1])
        cv2.rectangle(frame, (vertex_x, vertex_y),
                      (int(bound_rect[i][0] + bound_rect[i][2]), int(bound_rect[i][1] + bound_rect[i][3])),
                      (255, 255, 0), 3)

    return vertex_x


def get_move(webcam):
    """

    Move value is determined.

    Video input is taken from webcam and is fed through get_bounding_rect method which returns the value we need. A
    decision for the move is made based on where the object is in the webcam.

    Parameters
    ----------
        webcam : video input from webcam
        The video input from the webcam

    Return
    ----------
        Value of move. The actual game program makes decisions on what these values would do.

        1 = Left
        2= Right

    """
    x_position = get_bounding_rect(webcam)

    if x_position > 450:
        return 1

    elif 0 < x_position < 250:
        return 2

    else:
        return 0