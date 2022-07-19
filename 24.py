#b 변수를 생성할 때 a 변수의 값을 가져오면서 a와는 다른 주소를 가리키도록 만드는 방법
#1.[:]사용
a = [1,2,3]
b = a[:] #리스트 a의 처음 요소부터 끝 요소까지 슬라이싱
a[1] = 4
a
b
#2.copy 모듈 사용
from copy import copy
a = [1,2,3]
b = copy(a)
a
b
b is a 

#변수를 만드는 여러가지 방법
a, b = ('apple', 'banana')
(a, b) = 'apple', 'banana'
[a,b] = ['apple', 'banana']
a = b = fruit
