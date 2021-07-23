import csv
import pandas as pd
import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=  pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

#fig= ff.create_distplot([data],["Math Scores"], show_hist=False)
#fig.show()



mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

print("mean of population=",mean)
print("std_deviation of population=",std_deviation)


def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list =[]
for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)

std_deviation= statistics.stdev(mean_list)
mean = statistics.mean(mean_list)

print("mean of sampling distribution=",mean)
print("std_deviation of sampling distribution=",std_deviation)

fig = ff.create_distplot([mean_list],["student marks"], show_hist=False)
fig.show()



#finding the mean of the students who iused Math practice App 
df= pd.read_csv("School_1_Sample.csv")
data= df["Math_score"].tolist()

mean_of_sample1=statistics.mean(data)
print("mean of sample1=",mean_of_sample1)
fig=ff.create_distplot([mean_list],["students marks"], show_hist= False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="MEAN OF SAMPLE"))
fig.show()



#second intervention
df= pd.read_csv("School_2_Sample.csv")
data= df["Math_score"].tolist()

mean_of_sample2=statistics.mean(data)
print("mean of sample2=",mean_of_sample2)
fig=ff.create_distplot([mean_list],["students marks"], show_hist= False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample2, mean_of_sample2], y=[0, 0.17], mode="lines", name="MEAN OF SAMPLE"))
fig.show()


#third intervention 
df= pd.read_csv("School_3_Sample.csv")
data= df["Math_score"].tolist()

mean_of_sample3=statistics.mean(data)
print("mean of sample3=",mean_of_sample3)
fig=ff.create_distplot([mean_list],["students marks"], show_hist= False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample3, mean_of_sample3], y=[0, 0.17], mode="lines", name="MEAN OF SAMPLE"))
fig.show()




