import pandas as pd
import json

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

if __name__ == '__main__':
    create_surveys_a()
    create_surveys_b()
