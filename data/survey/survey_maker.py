import pandas as pd

messages = pd.read_csv('messages-cleaned.csv')

messages['remove'] = messages.remove.fillna(0)
messages = messages[messages.remove == 0]

between_messages = messages[messages.game_name == 'between-category-game-a']

between_survey = {}
seeds = (between_messages.generation == 0)
between_survey['choices'] = between_messages[seeds].pk.values
between_survey['given'] = between_messages[~seeds].pk.values

within_messages = messages[messages.game_name == 'within-category-game-a']

within_survey = {}
seeds = (within_messages.generation == 0)
within_survey['choices'] = within_messages[seeds].pk.values
within_survey['given'] = within_messages[~seeds].pk.values
