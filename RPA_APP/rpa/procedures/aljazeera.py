from RPA_APP.rpa.screens.aljazeera_screens import AljazeeraScreensService
from RPA_APP.sql.services.aljazeera_service import AljazeeraDatabaseService
from func_timeout import func_timeout, FunctionTimedOut
import json
import sys


# >>>>>>>>>INITIALIZE SERVICES>>>>>>>>>
service = AljazeeraDatabaseService()
service_screen = AljazeeraScreensService()
# <<<<<<<<<INITIALIZE SERVICES<<<<<<<<<


class RPAAljazeera:

    def newest_news(email, search_phrase, show_more):
        try:
            # >>>>>>>>>RPA Payload>>>>>>>>>
            payload = {
                "email": email,
                "search_phrase": search_phrase,
                "show_more": show_more
            }
            # <<<<<<<<<RPA Payload<<<<<<<<<

            # >>>>>>>>>Start RPA process>>>>>>>>>
            print("Starting RPA process.........")
            try:
                return_rpa = func_timeout(245, service_screen.rpa_aljazeera, args=([payload]))
            except FunctionTimedOut:
                print("=-==-==-==-==-=RPA TIMED OUT=-==-==-==-==-=")
                return {"status": False, "msg": "RPA Timed Out."}
            if not return_rpa["status"]:
                return {"status": False, "msg": return_rpa["msg"]}
            # <<<<<<<<<Start RPA process<<<<<<<<<

            # >>>>>>>>>Save Aljazeera news data in DataBase>>>>>>>>>
            print("Saving Aljazeera news data in DataBase.........")
            return_database = service.save_aljazeera_data(payload, return_rpa["data"])
            if not return_database["status"]:
                return {"status": False, "msg": return_database["msg"]}
            # <<<<<<<<<Save Aljazeera news data in DataBase<<<<<<<<<

            # >>>>>>>>>Save Aljazeera data in 'output/aljazeera_news.xlsx'>>>>>>>>>
            print("Saving Aljazeera data in 'output/aljazeera_news.xlsx'.........")
            return_excel = service.aljazeera_excel_file()
            if not return_excel["status"]:
                return {"status": False, "msg": return_excel["msg"]}
            # <<<<<<<<<Save Aljazeera data in 'output/aljazeera_news.xlsx'<<<<<<<<<

            # >>>>>>>>>Send excel file by email>>>>>>>>>
            if payload["email"] is not None:
                print("Sending excel file by email.........")
                return_email = service.aljazeera_excel_email(payload["email"])
                if not return_email["status"]:
                    return {"status": False, "msg": return_email["msg"]}
                return {"status": True, "msg": f"News Storaged and Sent to Email: {payload['email']}"}
            # <<<<<<<<<Send excel file by email<<<<<<<<<

            return {"status": True, "msg": f"News Storaged."}
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
