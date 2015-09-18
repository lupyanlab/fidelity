
get_responses <- function() {
  read.csv("data/responses.csv") %>%
    rename(contrast = survey) %>%
    mutate(
      contrast = ifelse(contrast == 1, "between", "within"),
      contrast_c = ifelse(contrast == "between", -0.5, 0.5),
      is_correct = as.numeric(answer == selection)
    )
}
