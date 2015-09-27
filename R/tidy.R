
get_responses <- function() {
  read.csv("data/responses.csv") %>%
    mutate(
      is_correct = as.numeric(answer == selection),
      chance = 0.25
    )
}
