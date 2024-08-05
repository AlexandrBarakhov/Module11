def introspection_info(obj):
    info = {
        'type': type(obj).__name__,
        'attributes': [attr for attr in dir(obj) if not callable(getattr(obj, attr))],
        'methods': [attr for attr in dir(obj) if callable(getattr(obj, attr))],
        'module': obj.__module__ if hasattr(obj, '__module__') else '__main__',
    }

    return info


print(introspection_info(42))
print(introspection_info(42.0))
print(introspection_info('42'))
print(introspection_info(True))
print(introspection_info((1, 2, 3)))
print(introspection_info([1, 2, 3]))
print(introspection_info({'a': 1, 'b': 2, 'c': 3}))
