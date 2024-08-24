from webdriver_manager.chrome import ChromeDriverManager
from botcity.web import WebBot, Browser, By
from botcity.web.browsers.chrome import default_options
from time import sleep
import sys
import json


class Service():

    def __init__(self):
        # >>>>>>>>>Bot Configurations#>>>>>>>>>
        self.bot = WebBot()
        self.headless = False
        self.options = default_options(headless=self.headless)
        self.browser = Browser.CHROME
        # Download Chrome Driver automatically
        self.driver_path = ChromeDriverManager().install()
        # <<<<<<<<<Bot Configurations<<<<<<<<<

    # >>>>>>>>>Function to paste "text" in a input field>>>>>>>>>
    def paste(self, bot, text):
        try:
            bot.paste(text)
            return {"status": True, "bot": bot}
        except Exception as e:
            # >>>>>>>>>Tracing the Error>>>>>>>>>
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback_details = {
                'filename': exc_traceback.tb_frame.f_code.co_filename,
                'line_number': exc_traceback.tb_lineno,
                'function_name': exc_traceback.tb_frame.f_code.co_name,
                'exception_type': exc_type.__name__,
                'exception_message': str(exc_value)
            }
            # print("=-==-==-=ERROR=-==-==-=")
            # print(traceback_details)
            # print("=-==-==-=ERROR=-==-==-=")
            # <<<<<<<<<Tracing the Error<<<<<<<<<
            return {"status": False, "msg": json.dumps(traceback_details)}
    # <<<<<<<<<Function to paste "text" in a input field<<<<<<<<<

    # >>>>>>>>>Function to type "Enter" key>>>>>>>>>
    def enter(self, bot):
        try:
            bot.enter()
            return {"status": True, "bot": bot}
        except Exception as e:
            # >>>>>>>>>Tracing the Error>>>>>>>>>
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback_details = {
                'filename': exc_traceback.tb_frame.f_code.co_filename,
                'line_number': exc_traceback.tb_lineno,
                'function_name': exc_traceback.tb_frame.f_code.co_name,
                'exception_type': exc_type.__name__,
                'exception_message': str(exc_value)
            }
            # print("=-==-==-=ERROR=-==-==-=")
            # print(traceback_details)
            # print("=-==-==-=ERROR=-==-==-=")
            # <<<<<<<<<Tracing the Error<<<<<<<<<
            return {"status": False, "msg": json.dumps(traceback_details)}
    # <<<<<<<<<Function to type "Enter" key<<<<<<<<<

    # >>>>>>>>>Function to press "type up" key>>>>>>>>>
    def type_up(self, bot):
        try:
            bot.type_up()
            return {"status": True, "bot": bot}
        except Exception as e:
            # >>>>>>>>>Tracing the Error>>>>>>>>>
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback_details = {
                'filename': exc_traceback.tb_frame.f_code.co_filename,
                'line_number': exc_traceback.tb_lineno,
                'function_name': exc_traceback.tb_frame.f_code.co_name,
                'exception_type': exc_type.__name__,
                'exception_message': str(exc_value)
            }
            # print("=-==-==-=ERROR=-==-==-=")
            # print(traceback_details)
            # print("=-==-==-=ERROR=-==-==-=")
            # <<<<<<<<<Tracing the Error<<<<<<<<<
            return {"status": False, "msg": json.dumps(traceback_details)}
    # <<<<<<<<<Function to press "type up" key<<<<<<<<<

    # >>>>>>>>>Function to start bot>>>>>>>>>
    def start_bot(self, link=None):
        try:
            # >>>>>>>>>Bot Configurations#>>>>>>>>>
            bot = self.bot
            bot.headless = self.headless
            bot.options = self.options
            bot.browser = self.browser
            bot.driver_path = self.driver_path
            # <<<<<<<<<Bot Configurations<<<<<<<<<

            # >>>>>>>>>Open Browser>>>>>>>>>
            bot.browse(f"{link}")
            bot.maximize_window()
            return {"status": True, "bot": bot}
            # <<<<<<<<<Open Browser<<<<<<<<<
        except Exception as e:
            # >>>>>>>>>Tracing the Error>>>>>>>>>
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback_details = {
                'filename': exc_traceback.tb_frame.f_code.co_filename,
                'line_number': exc_traceback.tb_lineno,
                'function_name': exc_traceback.tb_frame.f_code.co_name,
                'exception_type': exc_type.__name__,
                'exception_message': str(exc_value)
            }
            # print("=-==-==-=ERROR=-==-==-=")
            # print(traceback_details)
            # print("=-==-==-=ERROR=-==-==-=")
            # <<<<<<<<<Tracing the Error<<<<<<<<<
            return {"status": False, "msg": json.dumps(traceback_details)}
    # <<<<<<<<<Function to start bot<<<<<<<<<

    # >>>>>>>>>Function to click on elements by xpath>>>>>>>>>
    def xpath_elements_click(self, bot=None, father_name=None, son_name=None, son_content=None, index=None, scroll=False, maximum_attempts=45):
        try:
            # >>>>>>>>>Loop to maximize bot execution time>>>>>>>>>
            # Variable to control the loop
            attempt = True
            # Variable to count the loop iterations
            count_attempts = 0
            while attempt:
                # Limit the loop iterations
                if count_attempts >= maximum_attempts:
                    return {"status": False, "msg": "Maximum attempts.", "bot": bot}
                try:
                    # >>>>>>>>>Click on element by xpath>>>>>>>>>
                    if index is None:
                        bot.find_element(f"//{father_name}[@{son_name}='{son_content}']", By.XPATH, waiting_time=10000).click()
                    else:
                        bot.find_elements(f"//{father_name}[@{son_name}='{son_content}']", By.XPATH, waiting_time=10000)[index].click()
                    # <<<<<<<<<Click on element by xpath<<<<<<<<<
                    # Stop the loop
                    attempt = False
                    continue
                except:
                    # >>>>>>>>>LOGICAL CONTROL>>>>>>>>>
                    if scroll:
                        # Scroll down to make element visible
                        bot.scroll_down(clicks=1)

                    # Append 1 to the loop counter
                    count_attempts += 1
                    continue
                    # <<<<<<<<<LOGICAL CONTROL<<<<<<<<<
            # <<<<<<<<<Loop to maximize bot execution time<<<<<<<<<
            return {"status": True, "bot": bot}
        except Exception as e:
            # >>>>>>>>>Tracing the Error>>>>>>>>>
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback_details = {
                'filename': exc_traceback.tb_frame.f_code.co_filename,
                'line_number': exc_traceback.tb_lineno,
                'function_name': exc_traceback.tb_frame.f_code.co_name,
                'exception_type': exc_type.__name__,
                'exception_message': str(exc_value)
            }
            # print("=-==-==-=ERROR=-==-==-=")
            # print(traceback_details)
            # print("=-==-==-=ERROR=-==-==-=")
            # <<<<<<<<<Tracing the Error<<<<<<<<<
            return {"status": False, "msg": json.dumps(traceback_details), "bot": bot}
    # <<<<<<<<<Function to click on elements by xpath<<<<<<<<<

    # >>>>>>>>>Function to click on elements by id>>>>>>>>>
    def id_element_click(self, bot=None, id=None, scroll=False, maximum_attempts=45):
        try:
            # >>>>>>>>>Loop to maximize bot execution time>>>>>>>>>
            # Variable to control the loop
            attempt = True
            # Variable to count the loop iterations
            count_attempts = 0
            while attempt:
                # Limit the loop iterations
                if count_attempts >= maximum_attempts:
                    return {"status": False, "msg": "Maximum attempts.", "bot": bot}
                try:
                    # >>>>>>>>>Click on element by xpath>>>>>>>>>
                    bot.find_element(f"{id}", By.ID, waiting_time=10000).click()
                    # <<<<<<<<<Click on element by xpath<<<<<<<<<
                    # Stop the loop
                    attempt = False
                    continue
                except:
                    # >>>>>>>>>LOGICAL CONTROL>>>>>>>>>
                    if scroll:
                        # Scroll down to make element visible
                        bot.scroll_down(clicks=1)

                    # Append 1 to the loop counter
                    count_attempts += 1
                    continue
                    # <<<<<<<<<LOGICAL CONTROL<<<<<<<<<
            # <<<<<<<<<Loop to maximize bot execution time<<<<<<<<<
            return {"status": True, "bot": bot}
        except Exception as e:
            # >>>>>>>>>Tracing the Error>>>>>>>>>
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback_details = {
                'filename': exc_traceback.tb_frame.f_code.co_filename,
                'line_number': exc_traceback.tb_lineno,
                'function_name': exc_traceback.tb_frame.f_code.co_name,
                'exception_type': exc_type.__name__,
                'exception_message': str(exc_value)
            }
            # print("=-==-==-=ERROR=-==-==-=")
            # print(traceback_details)
            # print("=-==-==-=ERROR=-==-==-=")
            # <<<<<<<<<Tracing the Error<<<<<<<<<
            return {"status": False, "msg": json.dumps(traceback_details), "bot": bot}
    # <<<<<<<<<Function to click on elements by id<<<<<<<<<
