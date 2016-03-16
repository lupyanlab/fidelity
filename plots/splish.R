source("models/splish.R")

library(ggplot2)
library(scales)
library(AICcmodavg)

accuracies <- responses %>%
  group_by(survey_label, game_name, generation, message_id) %>%
  summarize(
    num_ratings = n(),
    is_correct = mean(is_correct)
  )

game_name <- list(
  "between-category-game-a" = "Imitating between categories",
  "within-category-game-a" = "Imitating within category"
)

facet_labeller <- function(variable,value){
  return(game_name[value])
}

color_scheme = c("#8da0cb", "#66c2a5")

ggplot(responses, aes(x = generation, y = is_correct, color = survey_label)) +
  geom_point(aes(alpha = num_ratings), data = accuracies,
             position = position_jitter(width = 0.2, height = 0.0), size = 3) +
  geom_smooth(method = "lm", se = FALSE) +
  scale_x_continuous("Generation", breaks = 1:13) +
  scale_y_continuous("Accuracy", breaks = seq(0, 1, by = 0.25), labels = percent) +
  scale_color_manual("Distractors", labels = c("Between Category", "Within Category"),
                     values = color_scheme) +
  geom_hline(yintercept = 0.25, lty = 2, color = "gray", alpha = 0.6) +
  guides(alpha = "none") +
  theme_classic() +
  theme(
    legend.title.align = 0.5,
    legend.background = element_blank(),
    legend.position = c(0.85, 0.8)
  ) + facet_grid(. ~ game_name, labeller = facet_labeller)

ggsave("plots/splish.png", width = 5, height = 4, units = "in")
