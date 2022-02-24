
#list
array = [273, 32, 13, "문자", True, False] #element(요소) 
list = [[1,2,3], [4,5,6], [7,8,9]]
print(list[0]) #[1,2,3]

#list_index
print(array[0]) #273
print(array[0:2]) #[273, 32]
array[0] = "건물" #요소 변경
print(array)
print(array[3][0]) #문

#list연산자
print(array + list)
print(len(array)) #6

#list에 요소추가 (파괴적=원본에변화)
array.append("상우") #요소 추가
print(array)
array.insert(0, "상우") #지정된위치에 요소추가
print(array)
array.extend([3, 4, 5]) #여러개의 요소추가
print(array)
print()
#list에 요소제거
del array[0] #index로 제거
print(array)
array.pop(0) #index로 제거
print(array)
array.remove("문자")
print(array) #값으로 제거
"문자" in array #False
array.clear() #모두 제거

#for반복문
array = [1,2,3,4,5]
for element in array: #element라는 변수에 array가 들어감
    print(element) #차례로 반복
