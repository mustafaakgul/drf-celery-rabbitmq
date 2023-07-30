# from django.test import TestCase
# from tasks import add
#
#
# result = add.delay(4, 5) # delay() is used to call the task asynchronously
# print(result.ready()) # ready() is used to check if the task has finished processing or not
# print(result.get()) # get() is used to get the result of the task execution
# result.get(propagate=False) # In case the task raised an exception, get() will re-raise the exception, but you can override this by specifying the propagate argument