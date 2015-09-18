library(dplyr)
library(lme4)

options(stringsAsFactors = FALSE)

devtools::load_all()

responses <- get_responses()

fidelity_mod <- glm(is_correct ~ generation * contrast_c, family = binomial, data = responses)
summary(fidelity_mod)
