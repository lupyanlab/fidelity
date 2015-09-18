
def unfold(json_frame, field):
    json_frame[field] = json_frame.fields.apply(lambda x: x[field])
    return json_frame
