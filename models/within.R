library(dplyr)
library(lme4)
library(broom)

devtools::load_all()

within <- get_responses() %>%
  filter(survey_label == "within") %>%
  mutate(generation_1 = generation - 1)

within %>%
  group_by(generation) %>%
  summarize(accuracy = mean(is_correct))

within %>%
  summarize(accuracy = mean(is_correct))

within_mod <- glmer(is_correct ~ offset(logit(chance)) + generation_1,
                     data = within, family = binomial)
summary(within_mod)
