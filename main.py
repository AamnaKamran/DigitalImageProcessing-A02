import math

import cv2
import numpy as np
from matplotlib import pyplot as plt


def q1():
    # QUESTION 1
    # part a
    # Load the image
    image = cv2.imread("data\\squares.tif")

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Laplacian filter
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)

    # Convert the result to uint8
    laplacian = np.uint8(np.absolute(laplacian))

    # Display the result
    cv2.imshow('Laplacian filter', laplacian)
    cv2.waitKey(0)

    # part b
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detector
    edges = cv2.Canny(gray, threshold1=10, threshold2=20)

    # Display the result
    cv2.imshow('Canny edge detection', edges)
    cv2.waitKey(0)


def q2():
    img = cv2.imread('data\\road.jpg')

    # convert the image to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # define the lower and upper range for blue color
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # create a mask for blue color
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # apply Gaussian blur to remove noise
    blur = cv2.GaussianBlur(mask, (5, 5), 0)

    # apply binary threshold to separate blue board from rest of image
    _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # find contours in thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # create a blank image
    blank = np.zeros_like(img)

    # loop through each contour
    for cnt in contours:
        # find area of contour
        area = cv2.contourArea(cnt)
        # if area is greater than threshold, draw contour on blank image
        if area > 10000:
            cv2.drawContours(blank, [cnt], 0, (255, 255, 255), -1)

    # display the result
    cv2.imshow('Result', blank)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def findLines(img, orientation):
    if orientation == 0:  # horizontal lines
        # Define a kernel for horizontal edge detection
        kernel = np.array([[0, 1, 0], [0, 0, 0], [0, -1, 0]])
        # Apply the kernel using filter2D function
        edges = cv2.filter2D(img, -1, kernel)
        cv2.imshow('0 Degree Edges', edges)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif orientation == 45:  # right diagonal lines
        # Define a kernel for horizontal edge detection
        kernel = np.array([[0, 0, 1], [0, 0, 0], [-1, 0, 0]])
        # Apply the kernel using filter2D function
        edges = cv2.filter2D(img, -1, kernel)
        cv2.imshow('45 Degree Edges', edges)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif orientation == 90:  # vertical lines
        kernel = np.array([[0, 0, 0], [1, 0, -1], [0, 0, 0]])
        # Apply the kernel using filter2D function
        edges = cv2.filter2D(img, -1, kernel)
        cv2.imshow('90 Degree Edges', edges)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif orientation == 135:  # left diagonal lines
        kernel = np.array([[1, 0, 0], [0, 0, 0], [0, 0, -1]])
        # Apply the kernel using filter2D function
        edges = cv2.filter2D(img, -1, kernel)
        cv2.imshow('135 Degree Edges', edges)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif orientation == -1:  # central rectangle
        kernel = np.array([[0, 1, 0], [1, 0, -1], [0, -1, 0]])
        # Apply the kernel using filter2D function
        edges = cv2.filter2D(img, -1, kernel)
        cv2.imshow('-1 Degree Edges', edges)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def q3():
    image = cv2.imread('data\\hexagon.jpg')
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    findLines(gray_img, 0)


def q4():
    # part a
    image = cv2.imread('data\hexagon2.jpg')

    # Define the range of red color in RGB
    lower_red = np.array([0, 0, 200])
    upper_red = np.array([50, 50, 255])

    # Create a mask to isolate the red pixels
    mask = cv2.inRange(image, lower_red, upper_red)

    # Count the number of red pixels in the mask
    count = np.count_nonzero(mask)

    rows, cols, x = image.shape

    total_size = rows * cols

    print(total_size)
    print(count)
    print((count / total_size) * 100)

    # part b
    mask_inverted = cv2.bitwise_not(mask)
    cv2.imshow('black hexagon', mask_inverted)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def pixel_frequency(items):
    frq = []
    for n in items:
        output = ''
        times = n
        frq.append(times)
    return frq


def equilization(img):
    hist, bins = np.histogram(img, bins=256, range=(0, 255))
    pixels = pixel_frequency(hist)

    # Calculate the cumulative sum of the histogram values
    cdf = np.cumsum(hist)
    print(cdf)

    rows, cols = img.shape
    total_pixels = rows * cols

    print(pixels)

    normalised = [p / total_pixels for p in pixels]

    print(normalised)

    final_result = []

    for i in range(0, len(normalised)):
        val = 0
        for j in range(0, i):
            val = val + normalised[j]
        final_result.append(val * 255)

    # print(final_result)
    rounded_values = [round(value) for value in final_result]
    print(rounded_values)

    # Plot the histogram and display it
    # plt.plot(hist)
    # plt.show()

    return rounded_values


def similarity():
    img1 = cv2.imread('data\\fundus.jpg', cv2.IMREAD_GRAYSCALE)
    img1_equilized = equilization(img1)

    img2 = cv2.imread('data\\fundus.jpg', cv2.IMREAD_GRAYSCALE)
    img2_equilized = equilization(img2)

    if img1_equilized == img2_equilized:
        print("Similar")
    else:
        print("Different")


def q5():
    img = cv2.imread('data\\road.jpg', cv2.IMREAD_GRAYSCALE)
    equilization(img)

    # part b
    similarity()

    # part c
    # # Load the input and reference images
    # input_img = cv2.imread('data\\hexagon.jpg', 0)
    # ref_img = cv2.imread('data\\hexagon2.jpg', 0)
    #
    # # Compute the histograms of the input and reference images
    # input_hist, _ = np.histogram(input_img, bins=256, range=(0, 255))
    # ref_hist, _ = np.histogram(ref_img, bins=256, range=(0, 255))
    #
    # # Compute the cumulative distribution functions (CDFs) of the histograms
    # input_cdf = input_hist.cumsum()
    # ref_cdf = ref_hist.cumsum()
    #
    # # Normalize the CDFs to range [0, 1]
    # input_cdf_normalized = input_cdf / float(input_cdf.max())
    # ref_cdf_normalized = ref_cdf / float(ref_cdf.max())
    #
    # # Compute the inverse CDF of the reference image
    # icdf = np.interp(input_cdf_normalized, ref_cdf_normalized, range(256))
    #
    # # Map each pixel value in the input image to its corresponding inverse CDF value
    # matched_img = np.interp(input_img, range(256), icdf)
    #
    # # Display the input and matched images
    # cv2.imshow('Input Image', input_img)
    # cv2.imshow('Matched Image', matched_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


def q6():
    # part a
    img1 = cv2.imread('data\\text1.tif', cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread('data\\text2.tif', cv2.IMREAD_GRAYSCALE)

    # Apply global thresholding using OpenCV's threshold() function
    thresh_value = 127
    max_value = 255
    _, img_thresh1 = cv2.threshold(img1, thresh_value, max_value, cv2.THRESH_BINARY)
    _, img_thresh2 = cv2.threshold(img2, thresh_value, max_value, cv2.THRESH_BINARY)
    # Display the input and thresholded images
    cv2.imshow('Thresholded Image 1', img_thresh1)
    cv2.imshow('Thresholded Image 2', img_thresh2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # part b
    # Load the input image
    # Load image
    img = cv2.imread('data\\text1.tif')

    # Get dimensions
    height, width, channels = img.shape

    # Create output image
    output = np.zeros((height, width), dtype=np.uint8)

    # Loop over all pixels
    for y in range(1, height - 1):
        for x in range(1, width - 1):

            # Get neighborhood around current pixel
            nhood = img[y - 1:y + 1, x - 1:x + 1 ]

            # Compute average value of pixels in neighborhood
            avg_nhood = np.mean(nhood)

            # Set output image based on center pixel value
            if img[y, x, 0] > avg_nhood:
                output[y, x] = 255

    # Display output image
    cv2.imshow('Output', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # part c
    img1 = cv2.imread('data\\text1.tif', cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread('data\\text2.tif', cv2.IMREAD_GRAYSCALE)

    # Apply adaptive thresholding using OpenCV's adaptiveThreshold() function
    max_value = 255
    block_size = 11
    c = 2
    img_thresh1 = cv2.adaptiveThreshold(img1, max_value, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, c)
    img_thresh2 = cv2.adaptiveThreshold(img2, max_value, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, c)

    # Display the input and thresholded images
    cv2.imshow('Adaptive Thresholded Image 1', img_thresh1)
    cv2.imshow('Adaptive Thresholded Image 2', img_thresh2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def q7():
    # QUESTION 7
    # part a
    image = cv2.imread("data\\fundus.jpg", cv2.IMREAD_COLOR)

    # part a
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Threshold the image to separate the bottle from the background
    _, thresh = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY_INV)

    # # Create a named window
    # cv2.namedWindow('Gray Image', cv2.WINDOW_NORMAL)
    # # Show the gray image in the named window
    # cv2.imshow('Gray Image', gray)
    # # Resize the window to reduce the image size
    # cv2.resizeWindow('Gray Image', 640, 520)

    # Create a named window
    cv2.namedWindow('Thresh Image', cv2.WINDOW_NORMAL)
    # Show the gray image in the named window
    cv2.imshow('Thresh Image', thresh)
    # Resize the window to reduce the image size
    cv2.resizeWindow('Thresh Image', 640, 520)

    # cv2.imshow("image", thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # part b
    # Apply a Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detect the edges using the Canny algorithm
    edges = cv2.Canny(blurred, 100, 200)

    # Find the contours in the image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Get the contour with the largest area (i.e. the outer edge of the eyeball)
    largest_contour = max(contours, key=cv2.contourArea)


    # # Draw the contour on the image
    # cv2.drawContours(image, [largest_contour], -1, (0, 255, 0), 2)
    #
    # # Calculate the diameter of the eyeball in pixels
    # (x, y), radius = cv2.minEnclosingCircle(largest_contour)
    # diameter_pixels = int(2 * radius)
    #
    # Display the image with the contour and diameter
    # Create a named window
    # cv2.namedWindow('Thresh Image', cv2.WINDOW_NORMAL)
    # # Show the gray image in the named window
    # cv2.imshow('Thresh Image', contours)
    # # Resize the window to reduce the image size
    # cv2.resizeWindow('Thresh Image', 640, 520)
    #
    # # cv2.putText(image, f'Diameter: {diameter_pixels} pixels', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    # cv2.imshow('Eye Image', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


# # q1()
# # q2()
# q3()
# q4()
# q5()
# q6()
q7()
