import cv2
import numpy as np



def get_filtered_images(image,action):
    
    if len(action)==0:
        filtered=image
    img=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    if action=='NO_FILTER':
        filtered=image
    elif action=='COLORIZE':
        filtered=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    elif action=='GRAYSCALE':
        filtered=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    elif action=='BLURRED':
        filtered=cv2.blur(img,(25,25))
    elif action=='BINARY':
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        v, filtered =cv2.threshold(gray,150,60,cv2.THRESH_BINARY)
    elif action=='HISTOGRAM':
        bgr_planes = cv2.split(img)
        histSize = 256
        histRange = (0, 256) # the upper boundary is exclusive
        accumulate = False
        b_hist = cv2.calcHist(bgr_planes, [0], None, [histSize], histRange, accumulate=accumulate)
        g_hist = cv2.calcHist(bgr_planes, [1], None, [histSize], histRange, accumulate=accumulate)
        r_hist = cv2.calcHist(bgr_planes, [2], None, [histSize], histRange, accumulate=accumulate)
        hist_w = 512
        hist_h = 400
        bin_w = int(round( hist_w/histSize ))
        histImage = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)
        cv2.normalize(b_hist, b_hist, alpha=0, beta=hist_h, norm_type=cv2.NORM_MINMAX)
        cv2.normalize(g_hist, g_hist, alpha=0, beta=hist_h, norm_type=cv2.NORM_MINMAX)
        cv2.normalize(r_hist, r_hist, alpha=0, beta=hist_h, norm_type=cv2.NORM_MINMAX)
        for i in range(1, histSize):
            cv2.line(histImage, ( bin_w*(i-1), hist_h - int(b_hist[i-1]) ),
                    ( bin_w*(i), hist_h - int(b_hist[i]) ),
                    ( 255, 0, 0), thickness=2)
            cv2.line(histImage, ( bin_w*(i-1), hist_h - int(g_hist[i-1]) ),
                    ( bin_w*(i), hist_h - int(g_hist[i]) ),
                    ( 0, 255, 0), thickness=2)
            cv2.line(histImage, ( bin_w*(i-1), hist_h - int(r_hist[i-1]) ),
                    ( bin_w*(i), hist_h - int(r_hist[i]) ),
                    ( 0, 0, 255), thickness=2)
            filtered=histImage
    elif action=='NOICE':
        filtered=cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
    elif action=='HSV':
        filtered=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    elif action=='EADGES':
        filtered=cv2.Canny(img,60,20,10)  
    elif action=='INVERT':
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        v,img =cv2.threshold(gray,150,60,cv2.THRESH_BINARY)
        filtered=cv2.bitwise_not(img)
    return filtered

#filtered=cv2.Canny(img,50,40,20) age detectin 




