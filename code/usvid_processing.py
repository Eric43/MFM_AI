########################################
#### Test of using CV2 to process ######
#### individual frames of .AVI    ######
#### Uses edge detect "edge" or   ######
#### modified "kernel" to maintain #####
#### Basic color information       #####
#### Used as a basic example.      #####
####  Eric W. Olle from CV2 docs    ####
########################################

# Basic examples 
#### usvid_processing("blinded_ectopic_flow.avi")
####  usvid_processing("blinded_ectopic_flow.avi", filter_type = "edge", resize = True)


#### Function #####
def usvid_processing (file_name,
                      filter_type = "kernel",
                      resize = False):
                          


    # importing the necessary libraries
    import cv2
    import numpy as np
    import os

    #filter_type = "kernel"

    #resize = False

    # Creating a VideoCapture object to read the video



    #### Change the video capture name as needed.
    vid_capture = cv2.VideoCapture(file_name)
    ### Onces the source of video capture is determined then start a 

    if (vid_capture.isOpened() == False):
        print("Error opening video file")

    else:
        fps = vid_capture.get(5)
        frame_count = int(vid_capture.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_width = int(vid_capture.get(3))
        frame_height = int(vid_capture.get(4))
        print("FPS: ", fps, "/ Frame count: ", frame_count,"/ Frame width: ",  frame_width, "/ Frame height: ",frame_height)



    while(vid_capture.isOpened()):
      # vid_capture.read() methods returns a tuple, first element is a bool 
      # and the second is frame
      ret, frame = vid_capture.read()
      if ret == True:

            if resize : 
                frame = cv2.resize(frame, (1080, 760), fx = 0, fy = 0,
                                   interpolation = cv2.INTER_CUBIC)

            if filter_type == "edge" :
            # using cv2.Canny() for edge detection.
                dst = cv2.GaussianBlur(frame,(3,3),cv2.BORDER_DEFAULT)
                edge_detect = cv2.Canny(dst, 100, 200)
                cv2.imshow('Edge detect', edge_detect)
            elif filter_type == "kernel":
            ### Attempt using a kernel
                kernel = np.array([[-1, -1, -1],
                                   [-1, 8.297, -1], 
                                   [-1, -1, -1]])
                edge_kernel = cv2.filter2D(frame, ddepth=-1, kernel=kernel)
                cv2.imshow('Kernel 2d edge', edge_kernel)

            key = cv2.waitKey(10)   
            if key == ord('q'):
                break
      else:
          break

    # Release the video capture object
    vid_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    usvid_processing()
