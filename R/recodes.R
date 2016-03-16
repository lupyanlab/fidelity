
recode_distractors <- function(frame) {
  frame %>%
    mutate(distractors_c = ifelse(survey_label == "within", -0.5, 0.5))
}

recode_imitation_context <- function(frame) {
  frame %>%
    mutate(
      imitation_context_c = ifelse(game_name == "between-category-a", -0.5, 0.5)
    )
}

