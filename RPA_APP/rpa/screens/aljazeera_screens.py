from RPA_APP.rpa.services.service import Service
from RPA_APP.rpa.services.aljazeera_service import AljazeeraService
from botcity.web import By
from time import sleep
import json
import sys

service = AljazeeraService()


class AljazeeraScreensService(Service):

    # >>>>>>>>>Aljazeera RPA logic>>>>>>>>>
    def rpa_aljazeera(self, payload):
        try:
            # >>>>>>>>>OPEN ALJAZEERA WEBSITE>>>>>>>>>
            bot = self.start_bot("https://www.aljazeera.com/")
            if not bot["status"]:
                return {"status": False, "msg": bot["msg"]}
            # <<<<<<<<<OPEN ALJAZEERA WEBSITE<<<<<<<<<

            # >>>>>>>>>EXTRACT ALJAZEERA DATA>>>>>>>>>
            bot = self.extract_data(bot["bot"], payload)
            if not bot["status"]:
                # Kill bot
                bot["bot"]["bot"].stop_browser()
                return {"status": False, "msg": bot["msg"]}
            # <<<<<<<<<EXTRACT ALJAZEERA DATA<<<<<<<<<

            # >>>>>>>>>Close bot process and return success>>>>>>>>>
            bot["bot"].stop_browser()
            return {"status": True, "data": bot["data"]}
            # <<<<<<<<<Close bot process and return success<<<<<<<<<
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
            print("=-==-==-=ERROR=-==-==-=")
            print(traceback_details)
            print("=-==-==-=ERROR=-==-==-=")
            # <<<<<<<<<Tracing the Error<<<<<<<<<
            return {"status": False, "msg": json.dumps(traceback_details)}
    # <<<<<<<<<Aljazeera RPA logic<<<<<<<<<

    # >>>>>>>>>Extract newest data from "https://www.aljazeera.com/">>>>>>>>>
    def extract_data(self, bot, payload):
        try:
            # >>>>>>>>>Click on "SEARCH" input field, fill it and advance>>>>>>>>>
            bot = self.xpath_elements_click(bot=bot, father_name="button", son_name="type", son_content="button")
            if not bot["status"]:
                return {"status": False, "msg": bot["msg"], "bot": bot["bot"]}
            bot = self.paste(bot=bot["bot"], text=payload["search_phrase"])
            if not bot["status"]:
                return {"status": False, "msg": bot["msg"], "bot": bot["bot"]}
            bot = self.enter(bot=bot["bot"])
            if not bot["status"]:
                return {"status": False, "msg": bot["msg"], "bot": bot["bot"]}
            # <<<<<<<<<Click on "SEARCH" input field, fill it and advance<<<<<<<<<

            # >>>>>>>>>Filter the newest news>>>>>>>>>
            bot = self.id_element_click(bot=bot["bot"], id="search-sort-option")
            if not bot["status"]:
                return {"status": False, "msg": bot["msg"], "bot": bot["bot"]}
            bot = self.type_up(bot=bot["bot"])
            if not bot["status"]:
                return {"status": False, "msg": bot["msg"], "bot": bot["bot"]}
            bot = self.enter(bot=bot["bot"])
            if not bot["status"]:
                return {"status": False, "msg": bot["msg"], "bot": bot["bot"]}
            # <<<<<<<<<Filter the newest news<<<<<<<<<

            # >>>>>>>>>Load all news to be extracted>>>>>>>>>
            # Get the total of possible results
            total_results = int(bot["bot"].find_element(f"//span[@class='search-summary__query']", By.XPATH, waiting_time=10000).text.split(" ")[1]) // 10
            # Define how many times "Show more" button will be clicked
            show_more = payload["show_more"] if payload["show_more"] <= total_results else total_results - 1
            for h in range(show_more):
                sleep(1)
                if total_results != int(bot["bot"].find_element(f"//span[@class='search-summary__query']", By.XPATH, waiting_time=10000).text.split(" ")[1]) // 10:
                    break
                # "Show more" button click
                bot = self.xpath_elements_click(bot=bot["bot"], father_name="button", son_name="class", son_content="show-more-button grid-full-width", scroll=True, maximum_attempts=450)
                if not bot["status"]:
                    return {"status": False, "msg": bot["msg"], "bot": bot["bot"]}
            # <<<<<<<<<Load all news to be extracted<<<<<<<<<

            # >>>>>>>>>Extract news>>>>>>>>>
            bot = service.extract_aljazeera_news(bot["bot"])
            if not bot["status"]:
                return {"status": False, "msg": bot["msg"], "bot": bot["bot"]}
            # <<<<<<<<<Extract news<<<<<<<<<

            return {"status": True, "bot": bot["bot"], "data": bot["data"]}
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
            print("=-==-==-=ERROR=-==-==-=")
            print(traceback_details)
            print("=-==-==-=ERROR=-==-==-=")
            # <<<<<<<<<Tracing the Error<<<<<<<<<
            return {"status": False, "msg": json.dumps(traceback_details), "bot": bot}
    # <<<<<<<<<Extract newest data from "https://www.aljazeera.com/"<<<<<<<<<
