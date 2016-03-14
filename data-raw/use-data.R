library(dplyr)
library(devtools)
options(stringsAsFactors = FALSE)

fidelity <- read.csv("data-raw/responses.csv") %>%
  mutate(is_correct = as.numeric(selection == answer))

splish <- read.csv("data-raw/splish.csv") %>%
  mutate(is_correct = as.numeric(selection == answer))

use_data(fidelity, splish, overwrite = TRUE)
