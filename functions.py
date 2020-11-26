
#function to flatten dictionary results
def flatten_json(nested_json):
    """
        Flattens a json object with nested keys into a single level.
        Args:
            nested_json: A nested json object.
        Returns:
            The flattened json object if successful, None otherwise.
    """
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '.')
#         #Uncomment to flatten lists as well -> current_key.i where i=item_#_in_the_list
#         elif type(x) is list:
#             i = 0
#             for a in x:
#                 flatten(a, name + str(i) + '.')
#                 i += 1
        else: #add item to flattened dict
            out[name[:-1]] = x    # -1 excludes hanging . from name string

    flatten(nested_json)
    return out