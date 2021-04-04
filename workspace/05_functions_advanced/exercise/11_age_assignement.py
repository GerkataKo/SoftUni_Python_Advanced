def age_assignment(*args, **kwargs, ):
    for name in args:
        if name[0] in kwargs:
            kwargs[name] = kwargs.pop(name[0])
    return kwargs