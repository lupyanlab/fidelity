library(dplyr)
library(lme4)
library(broom)

devtools::load_all()

between <- get_responses() %>%
  filter(survey_label == "between")

between %>%
  group_by(generation) %>%
  summarize(accuracy = mean(is_correct))

between %>%
  summarize(accuracy = mean(is_correct))

between_mod <- glmer(is_correct ~ offset(logit(chance)) + generation + (generation|chain_name),
                     data = between, family = binomial)
summary(between_mod)
