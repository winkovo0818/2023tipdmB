import cv2

img = cv2.imread("img01.jpg")
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转化为灰度图
faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # 返回人脸矩形数组
i = 0
for (x, y, w, h) in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 绘制矩形
    i = i + 1
cv2.imwrite('d: \\ test.jpg', img)
img = cv2.resize(img, (1300, 600))
print(i)
cv2.imshow("show", img)
cv2.waitKey(0)
