# -*- coding: utf-8 -*-
"""P1_4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aB9D4wZ3LbQOr6ahFrLSpXytegHxwNn6
"""

#骑士
position1 = input().split()
position2 = input().split()
x1,y1 = int(position1[0]),int(position1[1])
x2,y2 = int(position2[0]),int(position2[1])
if (x1==x2 and y1==y2) or (checkerboard[x2][y2]==1):
  print("No")
elif (abs(x2-x1)==2 and abs(y2-y1)==1) or (abs(x2-x1)==1 and abs(y2-y1)==2):
  print("Yes")
else:
  print("No")