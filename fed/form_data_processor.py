def get_field_name(field):
    return field.name.split('-')[1]


def form_to_dict(form):
    data = dict()
    for field in form:
        field_name = get_field_name(field)
        if field_name not in ["csrf_token", "visible"]:
            data[field_name] = field.data
    return data


def get_version(form):
    return form_to_dict(form)


def get_event(form):
    event = form_to_dict(form)
    print(event)
    return ''


def get_data_from_forms(forms):
    events = []
    for f in forms:
        if f.name == 'version':
            version = get_version(f)
        elif f.visible.data:
            events.append(get_event(f))
