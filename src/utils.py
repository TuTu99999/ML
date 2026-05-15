import sys

def error_messgae_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    error_messgae_detail = 'Error occured in python script name [{0}] line number [{1}] error message [{2}]'.format( exc_tb.tb_frame.f_code.co_filename, exc_tb.tb_lineno, str(error)
    return error_messgae_detail
)

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_messgae_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message