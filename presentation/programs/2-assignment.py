"""
def shopping(purchase_amt):
    discount_rate=0
    if(purchase_amt<=10000):
        discount_rate=.1
    elif(purchase_amt>10000 and purchase_amt<=20000):
        discount_rate = .2
    else:
        discount_rate = .25
    discount=purchase_amt*discount_rate
    net_amt=purchase_amt-discount
    print("net amount ",net_amt)
    print("discount ",discount)
#purchase_amt=int(input("Enter purchase amount "))
#shopping(purchase_amt)

print("list demo")
marks = []
for i in range(1,11):
    print("marks of ",i)
    mark=int(input())
    marks.append(mark)
print("marks list")
print(marks)
print("display marks")
for i in marks:
    print(i)
print("update")
marks[6]=16
print("display marks > 15")
for mark in marks:
    if(mark>15):
        print(mark)

print("dictionary demo")
topeconomies={
    "country":["USA","CHINA","GERMANY","JAPAN","INDIA"],
    "GDP":[27,19,4.4,4.2,4.1],
    "RANK":[1,2,3,4,5]
}
print(topeconomies)
print("keys")
print(topeconomies.keys())
print("values")
print(topeconomies.vaules())
for k,v in topeconomies.items():
    print(k,v)
"""
print("class and object")
class Product():
    def __init__(self,code,name,supplier,price):
        self.code = code
        self.name = name
        self.supplier = supplier
        self.price = price
    def information(self):
        return f"code : {self.code} name : {self.name} supplier : {self.supplier}"
laptop = Product(1,"HP Laptop","HP",70000)
info =laptop.information()
print(info)




