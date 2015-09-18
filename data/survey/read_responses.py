import pandas as pd

responses = pd.read_json('responses.json')

def unfold(json_frame, field):
    json_frame[field] = json_frame.fields.apply(lambda x: x[field])
    return json_frame

for response_field in ['selection', 'question']:
    responses = unfold(responses, response_field)

del responses['fields']

responses = responses[['selection', 'question']]

questions = pd.read_csv('questions.csv')

responses = responses.merge(questions, left_on='question', right_on='question_id')

responses = responses[['survey', 'question', 'given', 'generation', 'answer', 'selection']]

responses.to_csv('../responses.csv', index=False)
