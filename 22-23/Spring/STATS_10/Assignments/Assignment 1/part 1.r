# 1. Vectors
# a) Create a vector named heights that contains the heights, in inches, of yourself and two students near you. Print the contents of this vector.
heights <- c(75, 68, 71)
print(heights)

# b) Create a vector named names that contains the names of yourself and the two students near you. Print the contents of this vector.  
names <- c("Sanjit", "Dan", "Ella")
print(names)

# c) Try typing cbind(heights, names). What did this command do? What class is this new object? Hint: use the class() function.
print(class(cbind(heights, names)))
# cbind() combines two vectors into a matrix. The class of the new object is matrix.
# the bindedClass returns matrix

# 2. Downloading Data
# a) Download the dataset births.csv from the course site and upload it into R Studio. Name the data frame NCbirths.
setwd("C:/Users/sanji/Documents/School/Classes/Stats 10/Assignment 1")
NCbirths <- read.csv("./births.csv")
print(head(NCbirths))

# 3. Package Loading
# a) Install the maps package. Verify its installation by typing find.package("maps") and include the output in your answer
# # install.packages("maps")
print(find.package("maps"))
# b) Type library(maps) to load up the package. Type map("state") and include the plot output in your answer.
library(maps)
map("state")


# 4. Vector Operations
# a) Extract the weight variable as a vector from the NCbirths data frame. Print the first 10 elements of this vector.
weight <- NCbirths$weight
# b) what units are the weights in? 
print(weight[1:10]) # Ounces
# c) Create a new vector named weight_in_pounds which are the weights of the babies in pounds. You can look up conversion factors on the internet. Print the first 10 elements of this vector.
weight_in_pounds <- weight/16
# d) Demonstrate your success by typing weights_in_pounds[1:20] and including the output in your word processing document.
print(weight_in_pounds[1:20])

library(mosaic)
# 5. Mean weight of babies
# a) What is the mean weight of babies in pounds?
print(mean(weight_in_pounds))
# a) What percentage of the mothers in the sample smoke? Hint: use the tally function with the format argument. Use the help screen for guidance.
print(tally(NCbirths$smoke, format = "percent"))
# b) According to the Centers for Disease Control, approximately 21% of adult Americans are smokers. How far off is the percentage you found in 2 from the CDC’s report?
