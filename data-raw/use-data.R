library(dplyr)
library(devtools)
options(stringsAsFactors = FALSE)

tidy_responses <- function(frame) {
  frame %>%
    mutate(
      is_correct = as.numeric(selection == answer),
      chance = 0.25
    )
}

fidelity <- read.csv("data-raw/responses.csv") %>% tidy_responses

splish <- read.csv("data-raw/splish.csv") %>% tidy_responses

use_data(fidelity, splish, overwrite = TRUE)
