library(caret)
library(reticulate)

azureml_core = import("azureml.core")
run = azureml_core$Run$get_context()
run$log("test", 1)

print(c("runid",run$id))

# attach the iris dataset to the environment
data(iris)
# rename the dataset
dataset <- iris

# list types for each attribute
sapply(dataset, class)

# take a peek at the first 5 rows of the data
head(dataset)

# list the levels for the class
levels(dataset$Species)

# summarize the class distribution
percentage <- prop.table(table(dataset$Species)) * 100
cbind(freq=table(dataset$Species), percentage=percentage)

# summarize attribute distributions
summary(dataset)

# split input and output
x <- dataset[,1:4]
y <- dataset[,5]

# density plots for each attribute by class value
scales <- list(x=list(relation="free"), y=list(relation="free"))

pdf('outputs/plots.pdf')
featurePlot(x=x, y=y, plot="density", scales=scales)

run$'_client'$flush()

