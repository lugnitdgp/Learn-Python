# python sampleexceptions.py

# Minimal types of exceptions are used in this sample.
# For a list of built in python exceptions see https://docs.python.org/2/library/exceptions.html


# Expected Output:
#
# Basic exception raised.
# Basic exception with message: ERROR.
# Caught non basic exception: No module named badimport.
# Caught non basic exception: unsupported operand type(s) for +: 'int' and 'str'.
# Demonstrated how to handle multiple types of exceptions the same way.
# Demonstrated how to handle multiple types of exceptions the same way with a message: No module named badimport.
# Demonstrated how to handle exceptions differently.
# This should appear.
# Demonstrated how finally is run after exceptions.
# Demonstrated how else is run when no exceptions occur.
# Demonstrated how to use a basic custom exception: Custom Exception.


try:
    raise Exception
except:
    print "Basic exception raised."


try:
    raise Exception("ERROR")
except Exception as e:
    print "Basic exception with message: %s." % str(e)


try:
    import badimport
except ImportError as e:
    print "Caught non basic exception: %s." % str(e)


try:
    test = 1 + '1'
except TypeError as e:
    print "Caught non basic exception: %s." % str(e)


try:
    import badimport
except ImportError, TypeError:
    print "Demonstrated how to handle multiple types of exceptions the same way."


try:
    import badimport
except (ImportError, TypeError) as e:
    print "Demonstrated how to handle multiple types of exceptions the same way with a message: %s." % str(e)


try:
    import badimport
except ImportError:
    print "Demonstrated how to handle exceptions differently."
except TypeError:
    print "This should not appear."


try:
    import badimport
except ImportError:
    print "This should appear."
finally:
    print "Demonstrated how finally is run after exceptions."


try:
    test = 1 + 1
except:
    print "This should not appear."
else:
    print "Demonstrated how else is run when no exceptions occur."


class CustomBasicError(Exception):
    """ Custom Exception Type - Can be customised further """
    pass


try:
    raise CustomBasicError("Custom Exception")
except CustomBasicError as e:
    print "Demonstrated how to use a basic custom exception: %s." % str(e)
