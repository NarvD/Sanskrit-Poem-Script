def siddhanta(variable_name, value):
    global_variables = globals()
    if variable_name not in global_variables:
        global_variables[variable_name] = value
