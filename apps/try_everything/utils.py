import datetime


def from_resource_to_filename(resource):
    return f"{resource.Meta.model.__name__} {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
