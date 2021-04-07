import numpy as np 
import pandas as pd 
score_df = pd.DataFrame([[1,50,80,70,'boy',1],[2,60,45,50,'boy',2],[3,98,43,55,'boy',1],[4,70,69,89,'boy',2],[5,56,79,60,'girl',1],[6,60,68,55,'girl',2],[7,45,70,77,'girl',1],[8,55,77,76,'girl',2],[9,25,57,60,'girl',1],[10,88,40,43,'girl',3],[11,25,60,45,'boy',3],[12,80,60,23,'boy',3],[13,20,90,66,'girl',3],[14,50,50,50,'girl',3],[15,89,67,77,'girl',3]],columns=['student_id','math_score','english_score','chinese_score','sex','class'])
#題目 : 運用下列分數資料分析 
#a.找出全年級各科成績最高分與最低分？
#數學最高分：98 最低分：20
#英文最高分：90 最低分：40
#國文最高分：89 最低分：23
score_df = score_df.set_index('student_id')
m_x = score_df['math_score']
e_x = score_df["english_score"]
c_x = score_df['chinese_score']
print(m_x.max())
print(m_x.min())
print(e_x.max())
print(e_x.min())
print(c_x.max())
print(c_x.min())
#b.找出數學班平均最高的班級？
#2班平均最高
print(score_df.groupby(['class']).mean())
#c.分析全校女生與男生國文平均差幾分？
# 7.333333333333329
a = score_df.groupby(['sex']).mean()
print(a.chinese_score["girl"]-a.chinese_score["boy"])
