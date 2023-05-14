import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Загружаем изображение и преобразуем его в оттенки серого:

img = cv2.imread('1.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# Применяем фильтр Гаусса для уменьшения шумов на изображении:

blur_img = cv2.GaussianBlur(gray_img,(5,5),0)


# Выполняем адаптивную бинаризацию для выделения ярких областей на фотографии (в данном случае используется метод Otsu):

thresh_adapt =cv2.adaptiveThreshold(blur_img ,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY_INV,11,8) 
ret3,img_otsu=cv2.threshold(thresh_adapt ,0 ,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)  



contours,hierarchy= cv2.findContours(img_otsu,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
count = len(contours)


print(f"Количество ярких пятен на фотографии: {count}")



fig, ax = plt.subplots(nrows=2, ncols=2)
ax[0][0].imshow(img)
ax[0][1].imshow(gray_img)
ax[1][0].imshow(blur_img)
ax[1][1].imshow(thresh_adapt)
# ax[1][1].imshow(img_otsu)

# plt.imshow(img)
# plt.imshow(gray_img, cmap='gray')
plt.show()
# print(img)




# Для решения данной задачи можно использовать библиотеку OpenCV, которая позволяет работать с изображениями. Алгоритм работы программы будет следующим:

# 1. Импортируем необходимые библиотеки:

# ```python
# import cv2
# import numpy as np
# ```

# 2. Загружаем изображение и преобразуем его в оттенки серого:

# ```python
# img = cv2.imread('image.jpg')
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ```

# 3. Применяем фильтр Гаусса для уменьшения шумов на изображении:

# ```python
# blur_img = cv.GaussianBlur(gray_img,(5,5),0)
# ```

# 4. Выполняем адаптивную бинаризацию для выделения ярких областей на фотографии (в данном случае используется метод Otsu):

# ```python 
# thresh_adapt =cv.adaptiveThreshold(blur_img ,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
#             cv.THRESH_BINARY_INV,11,8) 
# ret3,img_otsu=cv.threshold(thresh_adapt ,0 ,255,cv.THRESH_BINARY+cv.THRESH_OTSU)  
# ```
# В результате выполнения этого шага мы получаем двоичное (черно-белое) изображение.

# 5. Найдём контуры объектов на получившейся картинке и посчитаем количество найденных контуров:
   
#  ``` python    
# contours,hierarchy= cv.findContours(img_otsu,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
# count = len(contours)
# ```

# 6. Выводим результат:

# ```python
# print(f"Количество ярких пятен на фотографии: {count}")
# ```

# В итоге, программа будет выводить количество найденных ярких пятен на изображении.