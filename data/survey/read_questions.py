import pandas as pd

questions = pd.read_json('questions.json')

def unfold(json_frame, field):
    json_frame[field] = json_frame.fields.apply(lambda x: x[field])
    return json_frame

for question_field in ['choices', 'given', 'survey', 'answer']:
    questions = unfold(questions, question_field)

del questions['fields']

messages = pd.read_csv('messages.csv')

def pick_ancestor(message):
    if message in [1,2,3,4] + [138,139,140,141]:
        return message
    else:
        parent = messages.ix[messages.pk == message, 'parent']
        return pick_ancestor(int(parent))

questions['answer'] = questions.given.apply(pick_ancestor)

del questions['model']
del questions['choices']

questions = questions.rename(columns={'pk': 'question_id'})

questions = questions.merge(messages, left_on='given', right_on='pk')

questions = questions[['survey', 'question_id', 'given', 'generation', 'answer']]

questions.to_csv('questions.csv', index=False)
