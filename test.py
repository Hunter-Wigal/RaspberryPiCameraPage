# import the opencv library 
import cv2 
  
  
# define a video capture object 
vid = cv2.VideoCapture(0)
vid.set(3, 1280)
vid.set(4, 720)
  
while(True): 
      
    # Capture the video frame 
    # by frame 
    ret, frame = vid.read()
    
    height, width, _ = frame.shape
    
    resize = cv2.resize(frame, (1280, 720), interpolation = cv2.INTER_AREA)
  
    # Display the resulting frame 
    cv2.imshow('frame', resize) 
      
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 