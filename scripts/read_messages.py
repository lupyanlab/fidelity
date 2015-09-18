import pandas as pd
import unipath as Path

messages = pd.read_json('messages.json')

del messages['model']

def unfold(json_frame, field):
    json_frame[field] = json_frame.fields.apply(lambda x: x[field])
    return json_frame

for message_field in ['generation', 'num_children', 'audio', 'chain', 'parent']:
    messages = unfold(messages, message_field)

del messages['fields']

def extract_from_path(frame, path_col, name, index):
    frame[name] = frame[path_col].str.split('/').str.get(index)
    return frame

for i, name in enumerate(['game_name', 'chain_name', 'message_name']):
    messages = extract_from_path(messages, 'audio', name, i)

messages = messages.ix[messages.game_name != 'test-game']

messages = messages.sort(['game_name', 'chain_name', 'message_name'])

messages = messages.rename(columns={'pk': 'message_id', 'chain': 'chain_id', 'parent': 'parent_id'})

messages.to_csv('messages.csv', index=False)
