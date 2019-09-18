import cv2 as cv

def get_pos(image):
  blurred = cv.GaussianBlur(image, (5, 5), 0)
  canny = cv.Canny(blurred, 200, 400)
  contours, hierarchy = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
  
  for i, contour in enumerate(contours):
    M = cv.moments(contour)
    if M['m00'] == 0:
      cx = cy = 0
    else:
      cx, cy = M['m10'] / M['m00'], M['m01'] / M['m00']
    if 6000 < cv.contourArea(contour) < 8000 and 370 < cv.arcLength(contour, True) < 390:
      if cx < 400:
        continue
      x, y, w, h = cv.boundingRect(contour) # 外接矩形
      cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
      cv.imshow('image', image)
      print(x)
      return x

  return 0

 
if __name__ == '__main__':
  # img0 = cv.imread('../20190916/image/bkBlock.png')
  img0 = cv.imread('./image/bkBlock.png')
  get_pos(img0)
  cv.waitKey(0)
  cv.destroyAllWindows()