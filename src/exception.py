import sys

def error_message_detail(error,error_detail:sys): # this function is used to get the error message
    _,_,exc_tb=error_detail.exc_info() # this is used to get the error information
    file_name=exc_tb.tb_frame.f_code.co_filename # this is used to get the file name
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))  # this is used to format the error message
    return error_message

class CustomException(Exception): # this is a custom exception class that inherits from the Exception class
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self): # this is a magic method that returns the error message
        return self.error_message

