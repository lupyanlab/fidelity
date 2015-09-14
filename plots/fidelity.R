library(dplyr)
library(ggplot2)
library(scales)

options(stringsAsFactors = FALSE)

between_responses <- read.csv("data/between_responses.csv")
between_responses <- between_responses %>%
  mutate(
    is_correct = as.numeric(answer == selection),
    contrast = "between"
  )

within_responses <- read.csv("data/within_responses.csv")
within_responses <- within_responses %>%
  mutate(
    is_correct = as.numeric(answer == selection),
    contrast = "within"
  )

accuracies <- rbind(between_responses, within_responses) %>%
  group_by(contrast, given_gen) %>%
  summarize(accuracy = mean(is_correct))

base_plot <- ggplot(accuracies, aes(x = given_gen, y = accuracy, color = contrast)) +
  geom_point(shape = 1, size = 3) +
  geom_smooth(method = "lm", formula = "y ~ poly(x,2)", se = FALSE)

max_gen = max(accuracies$given_gen)
styled_plot <- base_plot +
  scale_x_continuous("Generation") +
  scale_y_continuous("Accuracy", breaks = seq(0.1, 1.0, by = 0.1), labels = percent) +
  coord_cartesian(xlim = c(0.5, max_gen + 0.5)) +
  geom_hline(yintercept = 0.25, lty = 2) +
  annotate("text", x = 0.6, y = 0.27, label = "chance", hjust = 0) +
  theme_classic()
styled_plot

ggsave("plots/fidelity.png")
