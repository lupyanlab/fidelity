library(dplyr)
library(lme4)

options(stringsAsFactors = FALSE)

devtools::load_all()

responses <- get_responses() %>%
  filter(survey_label %in% c("between-splish", "within-splish"),
         chain_name == "splish") %>%
  mutate(survey_label = ifelse(survey_label == "within-splish", "within", "between"))

responses <- responses %>%
  recode_imitation_context %>%
  recode_distractors

splish_mod <- glm(is_correct ~ generation * distractors_c * imitation_context_c,
                  family = binomial, data = responses)
summary(splish_mod)
