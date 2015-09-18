library(dplyr)
library(ggplot2)
library(scales)

options(stringsAsFactors = FALSE)

devtools::load_all()

responses <- get_responses()

accuracies <- responses %>%
  group_by(contrast, generation) %>%
  summarize(
    num_ratings = n(),
    accuracy = mean(is_correct)
  )

base_plot <- ggplot(responses, aes(x = generation, y = is_correct, color = contrast)) +
  geom_point(aes(y = accuracy, size = num_ratings), data = accuracies, shape = 1) +
  geom_smooth(aes(group = contrast), method = "lm", se = FALSE)

max_gen = max(accuracies$generation)
styled_plot <- base_plot +
  scale_x_continuous("Generation") +
  scale_y_continuous("Accuracy", breaks = seq(0.1, 1.0, by = 0.1), labels = percent) +
  coord_cartesian(xlim = c(0.5, max_gen + 0.5)) +
  geom_hline(yintercept = 0.25, lty = 2) +
  annotate("text", x = 0.6, y = 0.27, label = "chance", hjust = 0) +
  theme_classic()
styled_plot

ggsave("plots/fidelity.png")
