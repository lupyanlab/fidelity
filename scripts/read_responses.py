import pandas as pd
from unipath import Path

from __init__ import unfold, survey_dir, csv_output_dir

responses = pd.read_json(Path(survey_dir, 'responses.json'))

for response_field in ['selection', 'question']:
    responses = unfold(responses, response_field)

del responses['fields']

responses = responses[['selection', 'question']]
responses.rename(columns={'question': 'question_id'}, inplace=True)

questions = pd.read_csv(Path(survey_dir, 'questions.csv'))

responses = responses.merge(questions)

responses = responses[[
    'survey_id', 'survey_label',
    'question_id', 'given', 'generation', 'given_game', 'given_chain',
    'answer', 'selection',
]]

responses.to_csv(Path(csv_output_dir, 'responses.csv'), index=False)
