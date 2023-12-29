subject_num = int(input())

subject_score = list(map(int, input().split()))
max_score = max(subject_score)

for i in range(subject_num):
    subject_score[i] = (subject_score[i] / (max_score * 100)) * 10000
print(sum(subject_score) / len(subject_score))