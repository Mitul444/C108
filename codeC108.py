import pandas as pd 
import plotly.figure_factory as ff
import statistics 


df=pd.read_csv("height-weight.csv")
height_list=df["Height(Inches)"].tolist()
mean=statistics.mean(height_list)
std_deviation=statistics.stdev(height_list)
median=statistics.median(height_list)
mode=statistics.mode(height_list)
print("mean,median,mode of the height is {}, {} and {} respectively".format(mean,median,mode))
#draw distribution plot of data 
first_std_dev_start,first_std_dev_end=mean-std_deviation,mean+std_deviation
second_std_dev_start,second_std_dev_end=mean-std_deviation,mean+std_deviation
list_of_data_within_first_std_deviation=[result for result in  height_list if result > first_std_dev_start and   result <first_std_dev_end]
print("{} % of data for height lies within 1 standard deviation".format(len(list_of_data_within_first_std_deviation)*100.0/len(height_list)))