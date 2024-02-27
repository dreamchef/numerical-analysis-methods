import inspect

def printFloatVec(vec, precision=3, spacing=0, newLine=True):

    const_spacing = 8

    for c in vec:

        print('{0:<{1}.{2}g}'.format(c, precision+const_spacing+spacing, precision), end='')
        print(' '*spacing, end='')

    if newLine is True:
        print('\n')

def lambdaToString(lambda_func):
    try:
        code_obj = lambda_func.__code__
        arg_names = code_obj.co_varnames[:code_obj.co_argcount]
        source_lines = inspect.getsourcelines(lambda_func)[0]
        lambda_line = source_lines[-1]
        lambda_expr = lambda_line.split("lambda", 1)

        return f"f({', '.join(arg_names)}) = lambda {lambda_expr}"

    except Exception as e:
        return f"Error describing the lambda function: {str(e)}"