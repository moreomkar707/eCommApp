import  logging

class LogGen:

    @staticmethod
    def loggen():
        logging.basicConfig(filename="F:\\Automation_Projects_Selenium_Python\eComm\Logs\\eComm_Automation_logs.log",
                            format= '%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger