import pandas as pd 
import plotly.figure_factory as ff 
import csv
import random
import plotly.graph_objects as go 
import statistics

df = pd.read_csv('studentMarks.csv')
data = df['Math_score'].tolist()
mean_population = statistics.mean(data)
std_deviation_population = statistics.stdev(data)
# fig = ff.create_distplot([data],['Maths Score'],show_hist=False)
# fig.show()
print('Population mean: ',mean_population)
print('Population Standard deviation: ',std_deviation_population)

def random_set_of_mean(count):
            data_set = []
            for i in range(0,count):
                    random_index = random.randint(0,len(data)- 1)
                    value = data[random_index]
                    data_set.append(value)
            mean = statistics.mean(data_set)
            return mean

mean_list = []
for i in range(0,1000):
            setOfMeans = random_set_of_mean(100)
            mean_list.append(setOfMeans)
std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print('Mean: ',mean)
print('Standard deviation: ',std_deviation)

firstStdStart,firstStdEnd = mean - std_deviation,mean + std_deviation
secondStdStart,secondStdEnd = mean - (2 * std_deviation) , mean + (2 * std_deviation)
thirdStdStart,thirdStdEnd = mean - (3 * std_deviation) , mean + (3 * std_deviation)
# fig = ff.create_distplot([mean_list],['Maths Score'],show_hist=False)
# fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.2],mode = 'lines',name = 'MEAN'))
# fig.add_trace(go.Scatter(x = [firstStdStart,firstStdStart], y = [0,0.2],mode = 'lines',name = 'First standard deviation start'))
# fig.add_trace(go.Scatter(x = [firstStdEnd,firstStdEnd], y = [0,0.2],mode = 'lines',name = 'First standard deviation end'))
# fig.add_trace(go.Scatter(x = [secondStdStart,secondStdStart], y = [0,0.2],mode = 'lines',name = 'Second standard deviation start'))
# fig.add_trace(go.Scatter(x = [secondStdEnd,secondStdEnd], y = [0,0.2],mode = 'lines',name = 'Second standard deviation end'))
# fig.add_trace(go.Scatter(x = [thirdStdStart,thirdStdStart], y = [0,0.2],mode = 'lines',name = 'Third standard deviation start'))
# fig.add_trace(go.Scatter(x = [thirdStdEnd,thirdStdEnd], y = [0,0.2],mode = 'lines',name = 'Third standard deviation end'))
# fig.show()
df1 = pd.read_csv('data1.csv')
data1 = df1['Math_score'].tolist()
meanOfSample1 = statistics.mean(data1)
# fig = ff.create_distplot([mean_list],['Maths Score'],show_hist=False)
# fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.2],mode = 'lines',name = 'MEAN'))
# fig.add_trace(go.Scatter(x = [meanOfSample1,meanOfSample1], y = [0,0.2], mode = 'lines',name = 'Mean of sample1'))
# fig.add_trace(go.Scatter(x = [firstStdEnd,firstStdEnd], y = [0,0.2],mode = 'lines',name = 'First standard deviation end'))
# fig.show()

df2 = pd.read_csv('data2.csv')
data2 = df2['Math_score'].tolist()
meanOfSample2 = statistics.mean(data2)
# fig = ff.create_distplot([mean_list],['Maths Score'],show_hist=False)
# fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.2],mode = 'lines',name = 'MEAN'))
# fig.add_trace(go.Scatter(x = [meanOfSample2,meanOfSample2], y = [0,0.2], mode = 'lines',name = 'Mean of sample2'))
# fig.add_trace(go.Scatter(x = [firstStdEnd,firstStdEnd], y = [0,0.2],mode = 'lines',name = 'First standard deviation end'))
# fig.add_trace(go.Scatter(x = [secondStdEnd,secondStdEnd], y = [0,0.2],mode = 'lines',name = 'Second standard deviation end'))
# fig.show()

df3 = pd.read_csv('data3.csv')
data3 = df3['Math_score'].tolist()
meanOfSample3 = statistics.mean(data3)
fig = ff.create_distplot([mean_list],['Maths Score'],show_hist=False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.2],mode = 'lines',name = 'MEAN'))
fig.add_trace(go.Scatter(x = [meanOfSample3,meanOfSample3], y = [0,0.2], mode = 'lines',name = 'Mean of sample3'))
fig.add_trace(go.Scatter(x = [firstStdEnd,firstStdEnd], y = [0,0.2],mode = 'lines',name = 'First standard deviation end'))
fig.add_trace(go.Scatter(x = [secondStdEnd,secondStdEnd], y = [0,0.2],mode = 'lines',name = 'Second standard deviation end'))
fig.add_trace(go.Scatter(x = [thirdStdEnd,thirdStdEnd], y = [0,0.2],mode = 'lines',name = 'Third standard deviation end'))
fig.show()
zScore1 = (meanOfSample1 - mean)/std_deviation
print('Z score of sample1: ',zScore1)
zScore2 = (meanOfSample2 - mean)/std_deviation
print('Z score of sample2: ',zScore2)
zScore3 = (meanOfSample3 - mean)/std_deviation
print('Z score of sample3: ',zScore3)
