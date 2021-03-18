import pandas as pd 
#對以下成績資料做分析
score_df = pd.DataFrame([[1,56,66,70], [2,90,45,34], [3,45,32,55], [4,70,77,89], [5,56,80,70], [6,60,54,55], [7,45,70,79], [8,34,77,76], [9,25,87,60], [10,88,40,43]],columns=['student_id','math_score','english_score','chinese_score'])
print(score_df)
score_df = score_df.set_index("student_id")
print(score_df)
#a.6 號學生(student_id=6) 3 科平均分數為何？
#56.333333
a = score_df.mean(axis = 1)
print(score_df.mean(axis = 1))
#b.6 號學生 3 科平均分數是否有贏過班上一半的同學？
#否
sum = 0
for i in a:
    if i < a[6]:
        sum+=1
print(sum)   
#c.由於班上同學成績不好，所以學校統一加分，加分方式為開根號乘以十，請問 6 號同學 3 科成績分別是？
#數學：77.459667  英文：73.484692  國文：74.161985
n_score_df = score_df**(0.5)*10
print(n_score_df[5:6])
#d.承上題，加分後各科班平均變多少？
#數學：74.194221  英文：78.350301  國文：78.739928
print(n_score_df.mean())