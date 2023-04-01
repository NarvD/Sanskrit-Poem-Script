def jnanam(variable_name):
    global_variables = globals()
    if variable_name in global_variables:
        return global_variables[variable_name]
    else:
        raise NameError(f"Name '{variable_name}' is not defined")
