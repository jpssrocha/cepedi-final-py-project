def checkin_dict(keys: list[str], dict_ : dict) ->  bool:
    """Check if all the strings in `keys` are in the `dict` keys"""
    return all([True if key in keys else False for key in dict_.keys()])
