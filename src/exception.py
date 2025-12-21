import sys
from src.logger import logging

class CustomException(Exception):
    """
    Docstring for CustomException
    """

    def __init__(self, error_massage: str, error_detail: sys):
        """
        Docstring for __init__
        
        :param self: Description
        :param error_massage: Description
        :type error_massage: str
        :param error_detail: Description
        :type error_detail: sys
        """

        super().__init__(error_massage)
        
        self.error_massage = self._generate_detailed_error_massage(error_massage, error_detail)

    @staticmethod
    def _generate_detailed_error_massage(error_message: str, error_detail: sys) -> str:
        """
        Docstring for _generate_detailed_error_massage
        
        :param error_massage: Description
        :type error_massage: str
        :param error_detail: Description
        :type error_detail: sys
        :return: Description
        :rtype: str
        """

        _, _, exc_tb = error_detail.exc_info()

        file_name = exc_tb.tb_frame.f_code.co_filename

        detailed_massage = (
            f"\nError occured in Pytthon script:"
            f"\n-> File name: {file_name}"
            f"\n-> Line number: {exc_tb.tb_lineno}"
            f"\n-> Error massage: {str(error_message)}"
        )

        logging.error(detailed_massage)

        return detailed_massage
    
def __str__(self) -> str:
        """
        Docstring for __str__
        
        :param self: Description
        :return: Description
        :rtype: str
        """

        return self.error_massage