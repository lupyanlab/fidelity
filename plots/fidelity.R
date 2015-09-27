source("models/fidelity.R")

library(ggplot2)
library(scales)
library(AICcmodavg)

accuracies <- responses %>%
  group_by(survey_label, generation, given) %>%
  summarize(
    num_ratings = n(),
    accuracy = mean(is_correct)
  )

x_preds <- responses[,c("survey_label", "distractors_c", "generation")] %>% unique
glmer_preds <- predictSE(fidelity_mod, x_preds, se = TRUE, print.matrix = TRUE) %>%
  as.data.frame %>%
  rename(is_correct = fit, se = se.fit) %>%
  cbind(x_preds, .)


base_plot <- ggplot(responses, aes(x = generation, y = is_correct, color = survey_label)) +
  geom_point(aes(y = accuracy, alpha = num_ratings),
             position = position_jitter(width = 0.2, height = 0.0),
             size = 3, data = accuracies) +
  geom_smooth(aes(group = survey_label, ymin = is_correct-se, ymax = is_correct+se),
              data = glmer_preds, stat = "identity", size = 1.0)

color_scheme = c("#8da0cb", "#66c2a5")
# orange = "#fc8d62"

max_gen = max(accuracies$generation)
styled_plot <- base_plot +
  scale_x_continuous("Generation", breaks = 1:13) +
  scale_y_continuous("Accuracy", breaks = seq(0.0, 1.0, by = 0.25), labels = percent) +
  scale_color_manual("Distractors", labels = c("Between Category", "Within Category"),
                     values = color_scheme) +
  coord_cartesian(xlim = c(0.5, max_gen + 0.5)) +
  geom_hline(yintercept = 0.25, lty = 2, color = "gray", alpha = 0.6) +
  theme_classic() +
  guides(alpha = "none") +
  theme(
    legend.title.align = 0.5,
    legend.background = element_blank(),
    legend.position = c(0.8, 0.86)
  )

styled_plot

ggsave("plots/fidelity.png", width = 5, height = 4, units = "in")
