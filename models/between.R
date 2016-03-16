library(dplyr)
library(lme4)
library(broom)

devtools::load_all()
data(fidelity)

between <- filter(fidelity, survey_label == "between")

between %>%
  group_by(generation) %>%
  summarize(accuracy = mean(is_correct))

between %>%
  summarize(accuracy = mean(is_correct))

between_mod <- glmer(is_correct ~ generation + (generation|chain_name),
                     offset = chance, family = "binomial", data = between)
summary(between_mod)
