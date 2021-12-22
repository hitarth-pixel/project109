import plotly.figure_factory as ff
import csv
import pandas as pd
import statistics as st
df=pd.read_csv("prodata(1).csv")
mathSList=df["math score"].tolist()
mean=st.mean(mathSList)
median=st.median(mathSList)
mode=st.mode(mathSList)
std=st.stdev(mathSList)
# 1,2,3 std of math score
mathSListFirstStdStart=mean-std
mathSListSecondStdStart=mean-(2*std)
mathSListThirdStdStart=mean-(3*std)
mathSListFirstStdEnd=mean+std
mathSListSecondStdEnd=mean+(2*std)
mathSListThirdStdEnd=mean+(3*std)
# finding %s
math1=[result for result in mathSList if result>mathSListFirstStdStart and result<mathSListFirstStdEnd]
math2=[result for result in mathSList if result>mathSListSecondStdStart and result<mathSListSecondStdEnd]
math3=[result for result in mathSList if result>mathSListThirdStdStart and result<mathSListThirdStdEnd]
# printing
print("mean="+str(mean))
print("median="+str(median))
print("mode="+str(mode))
print("std="+str(std))
print("{}% of data for height lies within 1 standard deviation".format(len(math1)*100.0/len(mathSList)))
print("{}% of data for height lies within 2 standard deviation".format(len(math2)*100.0/len(mathSList)))
print("{}% of data for height lies within 3 standard deviation".format(len(math3)*100.0/len(mathSList)))

fig=ff.create_distplot([df["math score"].tolist()],["MATH SCORE"],show_hist=False)
fig.show()