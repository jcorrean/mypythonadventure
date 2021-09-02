library(readr)
newdata <- read_csv("~/Documents/GitHub/WebMining-OFD/newdata.csv")
commentscost <- newdata[c(1, 5,8)]
library(writexl)
write_xlsx(commentscost, "commentscost.xlsx")