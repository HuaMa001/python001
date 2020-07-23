#字典資料格式
fruits={"orange":20, "apple":10, "watermelon":30}     #{"key":value}
#利用get(放入key值) 得value值
print("orange價錢",fruits.get("orange"))
print("watermelon價錢",fruits.get("watermelon"))
print("apple價錢",fruits.get("apple"))
print("banana價錢",fruits.get("banana"))
print(fruits)
#setdefault(key值, 預設值(若找不到此元素))
print("banana價錢",fruits.setdefault("banana",70))
print(fruits)
print("apple價錢",fruits.setdefault("banana",100))
print(fruits)
#取得所有key值
names = fruits.keys()
print(names,type(names))
#取得所有value值
values = fruits.values()
print(values,type(values),sum(values))











