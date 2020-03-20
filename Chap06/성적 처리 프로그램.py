count=0
sum=0
score=list()
for i in range(5):
    score.append(int(input()))
for i in range(5):
    sum+=score[i]
for i in range(5):
    if score[i]>=80:
        count+=1
sum/=5
print("성적 평균은", sum, "입니다")
print("80점 이상 성적을 받은 학생은", count,"명입니다")
