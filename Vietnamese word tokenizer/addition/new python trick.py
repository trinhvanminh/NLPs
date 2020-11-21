def a(ten_gido):
    print(ten_gido)
    print(ten_khac)

ten_khac = 'day la tên biến khác với bên trong hàm a là ten_gido'
a(ten_khac)

#result: 
# day la tên biến khác với bên trong hàm a là ten_gido
# day la tên biến khác với bên trong hàm a là ten_gido


sumarize = r'''
kết luận cả 2 hàm print bên trên đều sử dụng được trong hàm a() 
mặc dù ten_khac không được khai báo trong hàm a()
ten_khac là biến được truyền vào từ bên ngoài 

```
ten_khac = 'day la tên biến khác với bên trong hàm a là ten_gido'
a(ten_khac)
```
nếu tham số truyền vào không phải là ten_khac nữa thì biến ten_khac trong hàm a() sẽ không hoạt động



Ứng dụng vào việc không cho người khác thực thi hàm đó :D
'''