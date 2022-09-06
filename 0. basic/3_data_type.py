# LIST

a_list = [1, 2, 3, 4, 5]
print(a_list[0])

print(a_list[:2]) # 배열의 두 번째 전까지 출력
print(a_list[2:]) # 배열의 두 번째부터 출력

b_list = []
b_list.append(1) # append를 이용해 배열에 추가
b_list.append(2)
b_list.append(3)
print(b_list)

c_list = [1, 3.14, "hello", [1,2,3]] # 배열에는 타입에 상관없이 넣을 수 있음
print(c_list)
print(c_list[1:3]) # 배열의 1번째 부터 3번째 전까지 출력

d_list = [1,2,3,4,5]
d_list[0] = 5 # 리스트의 데이터 변경가능

print(d_list)

# TUPLE
# 데이터 변경 불가능

a_tuple = (1, 2, 3, 4, 5) # 소괄호를 통해 묶음
print(a_tuple)

# DICTIONARY

a_dic = {'a' : 1, 'b' : 2, 'c' : 3} # 중괄호 안에 key : value 형태로 묶음
print(a_dic['a'])

b_dic = {'a' : 1, 2 : [1, 2, 3], 'k' : 'v'} # key는 문자가 아닌 숫자도 가능 value는 다양한 데이터가 들어갈 수 있음
print(b_dic)
b_dic['d'] = a_tuple # 추가할 때
print(b_dic)
b_dic['d'] = a_list # value 변경도 가능
print(b_dic)

# SET

a_set = set([1,2,3,4])# SET은 중복이 없는 자료형이다. set()안에 담아서 묶음
b_set = set("python") # SET은 랜덤한 순서로 들어가게됨
print(a_set)
print(b_set)
