"""
simple helpers for casting response objects
Also, there's a nice decorator at the bottom
called jsoncast
"""

def cast_to_dict(model_object):
    d = {}
    try:
        for k, v in model_object.__dict__.items():
            try:
                # some nasty instance state object blah
                if v.__class__.__name__ != 'InstanceState':
                    # print(v)
                    d[k] = v
            except Exception as e:
                continue
    except Exception as e:
        return model_object
    return d


def cast_to_nested_list(model_objects):
    tmp = []
    try:
        for item in model_objects:
            tmp.append(cast_to_dict(item))
        return tmp
    except Exception as e:
        return model_objects


def jsoncast(output_type):

    def dec_function(request_method):

        def wrapper(*args, **kwargs):

            response, code = request_method(*args, **kwargs)
            if output_type == 'list':
                return cast_to_nested_list(response), code
            elif output_type == 'dict':
                return cast_to_dict(response), code
            else:
                return {}, code
        return wrapper

    return dec_function
