import pandas as pd
import json

import random

def create_surveys_a():
    messages = pd.read_csv('messages-cleaned.csv')

    # Remove messages that are null in the to_remove column
    messages = messages.ix[messages.to_remove.notnull()]

    # Remove messages that shouldn't be used in the surveys
    messages = messages.ix[messages.to_remove == 0]

    # Split seed messages from imitations
    seeds = messages.ix[messages.generation == 0]
    imitations = messages.ix[messages.generation != 0]

    between_game_name = 'between-category-game-a'
    between_survey = {}
    between_survey['choices'] = seeds.ix[seeds.game_name == between_game_name, 'message_id'].tolist()
    between_survey['given'] = imitations.ix[imitations.game_name == between_game_name, 'message_id'].tolist()
    with open('between_survey_a.json', 'w') as f:
        f.write(json.dumps(between_survey))

    within_game_name = 'within-category-game-a'
    within_survey = {}
    within_survey['choices'] = seeds.ix[seeds.game_name == within_game_name, 'message_id'].tolist()
    within_survey['given'] = imitations.ix[imitations.game_name == within_game_name, 'message_id'].tolist()
    with open('within_survey_a.json', 'w') as f:
        f.write(json.dumps(within_survey))

def create_surveys_b():
    messages = pd.read_csv('messages-cleaned.csv')

    # Split off the seeds
    seeds = messages.ix[messages.generation == 0]

    # Select only the messages that are null in the to_remove column
    # These messages are valid recordings that are not seeds and have
    # not been tested in a survey
    imitations = messages.ix[messages.to_remove.isnull()]

    between_game_name = 'between-category-game-a'
    between_survey = {}
    between_survey['choices'] = seeds.ix[seeds.game_name == between_game_name, 'message_id'].tolist()
    between_survey['given'] = imitations.ix[imitations.game_name == between_game_name, 'message_id'].tolist()
    with open('between_survey_b.json', 'w') as f:
        f.write(json.dumps(between_survey))

    within_game_name = 'within-category-game-a'
    within_survey = {}
    within_survey['choices'] = seeds.ix[seeds.game_name == within_game_name, 'message_id'].tolist()
    within_survey['given'] = imitations.ix[imitations.game_name == within_game_name, 'message_id'].tolist()
    with open('within_survey_b.json', 'w') as f:
        f.write(json.dumps(within_survey))

def create_surveys_c():
    """ In this survey people are given imitations from the between-category-game-a
    and choices from the within-category-game."""
    messages = pd.read_csv('messages-cleaned.csv')

    # Get rid of bad recordings
    messages['to_remove'] = messages.to_remove.fillna(0)
    messages = messages.ix[messages.to_remove == 0]

    # Split off the seeds
    seeds = messages.ix[messages.generation == 0]
    imitations = messages.ix[messages.generation != 0]

    between_game_name = 'between-category-game-a'
    within_game_name = 'within-category-game-a'


    between_choices = seeds.ix[seeds.game_name == between_game_name, 'message_id'].tolist()
    within_choices = seeds.ix[seeds.game_name == within_game_name, 'message_id'].tolist()

    between_imitations = imitations.ix[imitations.game_name == between_game_name, 'message_id'].tolist()
    within_imitations = imitations.ix[imitations.game_name == within_game_name, 'message_id'].tolist()

    # shuffle so that surveys are split by generation
    random.seed(100)
    random.shuffle(between_imitations)
    random.shuffle(within_imitations)

    between_to_within = {}
    between_to_within['given'] = between_imitations[:len(between_imitations)/2]
    between_to_within['choices'] = within_choices
    with open('between_imitations_to_within_choices_survey_part_1.json', 'w') as f:
        f.write(json.dumps(between_to_within))

    between_to_within = {}
    between_to_within['given'] = between_imitations[len(between_imitations)/2:]
    between_to_within['choices'] = within_choices
    with open('between_imitations_to_within_choices_survey_part_2.json', 'w') as f:
        f.write(json.dumps(between_to_within))


    within_to_between = {}
    within_to_between['given'] = within_imitations[len(within_imitations)/2:]
    within_to_between['choices'] = between_choices
    with open('within_imitations_to_between_choices_survey_part_1.json', 'w') as f:
        f.write(json.dumps(within_to_between))

    within_to_between = {}
    within_to_between['given'] = within_imitations[:len(within_imitations)/2]
    within_to_between['choices'] = between_choices
    with open('within_imitations_to_between_choices_survey_part_2.json', 'w') as f:
        f.write(json.dumps(within_to_between))


if __name__ == '__main__':
    create_surveys_a()
    create_surveys_b()
    create_surveys_c()
