def ganita(operation, num1, num2):
    if operation == 'jodana':
        return num1 + num2
    elif operation == 'vayjana':
        return num1 - num2
    elif operation == 'gunana':
        return num1 * num2
    elif operation == 'bhajana':
        if num2 == 0:
            return "Error: Division by zero"
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation"
