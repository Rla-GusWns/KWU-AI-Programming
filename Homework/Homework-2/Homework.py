#2021741062 김현준

f = open('hw2.csv','r',encoding='UTF-8-SIG')

list = list()
for line in f:
    data = line.strip().split(',') # 뒤 개행문자 제거, 콤마 기준으로 나누기
    list.append(data)

#csv 파일을 읽어서 한줄씩 리스트에 넣음 [[첫번째 줄],[두번째 줄].......]

dic = {'박건우': list[1][1:],'이정후': list[2][1:],'피렐라': list[3][1:],'이대호': list[4][1:],'문보경': list[5][1:],
       '소크라테스': list[6][1:],'나성범': list[7][1:],'김혜성': list[8][1:],'한동희': list[9][1:],'조용호': list[10][1:],
       '전준우': list[11][1:],'최지훈': list[12][1:],'페르난데스': list[13][1:],'채은성': list[14][1:],'허경민': list[15][1:],
       '박성한': list[16][1:],'마티니': list[17][1:],'김선빈': list[18][1:],'박해민': list[19][1:],'안치홍': list[20][1:],
       '터크먼': list[21][1:],'양의지': list[22][1:],'홍창기': list[23][1:],'푸이그': list[24][1:],'노시환': list[25][1:],
       '노진혁': list[26][1:], '류지혁': list[27][1:],'손아섭': list[28][1:],'정은원': list[29][1:],'김현수': list[30][1:]
       }


def detectitemnumber(item):
    number = {'AVG': 1, 'G':2,'PA':3,'AB':4,'R':5,'H':6,'2B':7,'3B':8,'HR':9,'TB':10,'RBI':11,'SAC':12,'SF':13}
    return number[item]

# 1. 선수명 입력시 세부사항 출력

def player(name):
    print(list[0][1:])
    print(dic[name])

print("--------------------------------")
print("구현사항 1번")
print("--------------------------------")

try:
   name = input("이름을 입력하세요 : ") 
   player(name)
except:
    print("없는 선수명을 입력하였습니다")

# 2. 선수명 + 특정항목 입력시 세부사항 출력

def playerstats(name,item):
    
    number = detectitemnumber(item)
    str1 = '%s의 %s수치는 %s입니다'
    print(str1%(name,item,dic[name][number]))

print("\n--------------------------------")
print("구현사항 2번")
print("--------------------------------")

try:
   name = input("이름을 입력하세요 : ")
   item = input("확인하고 싶은 항목을 입력하세요(대문자) : ") 
   playerstats(name,item)
   
except:
    print("없는 정보를 입력하였습니다")


# 3. 특정항목 입력시 선수와 - 값 매칭해서 내림차순으로 배열. 사람 이름 내림차순

def itemstats(item):
    number = detectitemnumber(item)
    abc = sorted(dic,reverse=True)
    
    str1 = '\n선수들의 %s 내림차순 수치'
    print(str1%(item))
    
    for i in abc:
        print(i,':',dic[i][number])

print("\n--------------------------------")
print("구현사항 3번")
print("--------------------------------")

try:
    item = input("확인하고 싶은 항목을 입력하세요(대문자) : ")
    itemstats(item)
except:
    print("항목 입력을 잘못하셨습니다")
    
f.close()


