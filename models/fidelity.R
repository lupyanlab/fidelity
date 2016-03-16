library(dplyr)
library(lme4)
library(broom)

options(stringsAsFactors = FALSE)

devtools::load_all()
data(fidelity)

responses <- fidelity %>% filter(survey_label %in% c("between", "within"))

responses <- recode_distractors(responses)

fidelity_mod <- glmer(is_correct ~ generation * distractors_c + (generation|chain_name),
                      data = responses, family = binomial)
summary(fidelity_mod)

generation_mod_within <- glmer(is_correct ~ generation + (generation|chain_name),
                               data = filter(responses, survey_label == "within"),
                               family = binomial)
tidy(generation_mod_within, effects = "fixed")

generation_mod_between <- glmer(is_correct ~ generation + (generation|chain_name),
                               data = filter(responses, survey_label == "between"),
                               family = binomial)
tidy(generation_mod_between, effects = "fixed")
