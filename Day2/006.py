# 파일 입출력 open, read, write, close 
# 파일 열기 
# 파일객체 = open(파일 이름, 모드)
# 파일 이름 : 파일 이름 또는 파일 경로
# 모드 : 파일을 열 때의 모드 r= 읽기 모드   w= 쓰기 모드  a= 추가 모드
# 파일 쓰기
# 파일객체.write(문자열) : 파일에 문자열을 쓴다

f = open("Day2/fileio.txt","w")
for i in range(5):
    f.write("Hello Python\n")
f.close()
# 파일 읽기
# 파일객체.read() : 파일의 내용 전체를 문자열로 반환
# 파일객체.readline() : 파일의 내용 한 줄을 문자열로 반환
# 파일객체.readlines() : 파일의 내용 전체를 한 줄씩 리스트로 반환

f= open("Day2/fileio.txt","r")
data = f.read()
print(data)
f.close()   
f= open("Day2/fileio.txt","r")
liense = f.readlines()
print(liense)
f.close()

# 파일 내용 추가 
f= open("Day2/fileio.txt","a")
f.write("\n new data add")
f.close()

# with 문을 사용하여 파일 자동 닫기
with open("Day2/fileio.txt","r") as f:
    data = f.read()
print(data)
