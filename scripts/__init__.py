from unipath import Path

csv_output_dir = Path('data-raw')
survey_dir = Path('data-raw/survey')

def unfold(json_frame, field):
    json_frame[field] = json_frame.fields.apply(lambda x: x[field])
    return json_frame
