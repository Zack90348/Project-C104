import cv2
img = cv2.imread("solar-system.jpg")

cv2.putText(img,"Sun",(102,90),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2)
cv2.putText(img,"Mercury",(123,192),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
cv2.putText(img,"Venus",(214,262),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
cv2.putText(img,"Earth",(301,264),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
cv2.putText(img,"Mars",(384,262),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
cv2.putText(img,"Jupiter",(561,398),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
cv2.putText(img,"Saturn",(793,308),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
cv2.putText(img,"Uranus",(1004,299),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
cv2.putText(img,"Neptune",(1153,287),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)

cv2.imshow("Output",img)
cv2.waitKey(5000)
