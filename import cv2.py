import cv2
import webbrowser 

cap = cv2.VideoCapture(0)
detector=cv2.QRCodeDetector()
while True:
    _,img=cap.read()
    data,one, _=detector.detectAndDecode(img)
    if data:
        a=data
        break
    cv2.imshow('qrcodescanner app', img)
    if cv2.waitKey(1)==ord('q'):
        break
print(a)
#b=webbrowser.open(str(a))
#main_search
def linear_Search(list1, n, a):  
  
    # Searching list1 sequentially  
    for j in range(0, n):  
        if (list1[j] == a):  
            return j  
    return -1  
  
  
list1 = ['12345']
list2=['13546','14567','56994','89654','789645']  
    
n = len(list1)

res = linear_Search(list1, n, a)

if(res == -1): 
   #print("element not found")

    def linear_Search(list2,n,a):
        for i in range(0, n):
            if(list2[i] == a):
                list1.append(list2[i])
                return i
            
        return -1
    n = len(list2) 
    res = linear_Search(list2, n, a)   

    if(res==-1):
        print("Licence Denied")
    else:
        print("Notification Sent")
        print("Licence Approved")
        

else:  
    print("Licence Approved")  

print(list1)

cap.release(a)
cv2.destroyAllwindows()


