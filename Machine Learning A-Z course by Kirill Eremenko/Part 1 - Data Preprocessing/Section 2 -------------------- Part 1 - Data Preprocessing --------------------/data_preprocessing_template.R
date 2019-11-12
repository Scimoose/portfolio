
dataset = read.csv('Data.csv')

dataset$Age = ifelse(is.na(dataset$Age))
dataset$Salary = ifelse(is.na(dataset$Salary))