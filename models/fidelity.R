library(dplyr)
library(lme4)

options(stringsAsFactors = FALSE)

devtools::load_all()

responses <- get_responses() %>%
  filter(survey_label %in% c("between", "within"))

fidelity_mod <- glm(is_correct ~ generation * survey_label, family = binomial, data = responses)
summary(fidelity_mod)

responses$given_chain_group <- with(responses, paste0(given_game,given_chain))

fidelity_mod <- glmer(is_correct ~ generation * survey_label + (generation|given_chain),
                      data = responses, family = binomial)
summary(fidelity_mod)
