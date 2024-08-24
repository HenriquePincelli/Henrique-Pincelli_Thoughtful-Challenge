from RPA_APP.rpa.services.service import Service
from botcity.web import By
from time import sleep
import json
import sys


class AljazeeraService(Service):

    # >>>>>>>>>Function to extract all data from Aljazeera website>>>>>>>>>
    def extract_aljazeera_news(self, bot):
        try:
            # Give time to load all elements in HTML
            sleep(5)

            # Pick news title, date and description
            list_news_data = bot.find_elements(f"//div[@class='gc__content']", By.XPATH, waiting_time=10000)
            # Pick news images
            list_news_images = bot.find_elements(f"//img[@class='article-card__image gc__image']", By.XPATH, waiting_time=10000)

            # >>>>>>>>>Make a list for news informations and one for news images>>>>>>>>>
            news = [data.text.split("\n") for data in list_news_data]
            news_images = [data.get_attribute("src") for data in list_news_images]
            # <<<<<<<<<Make a list for news informations and one for news images<<<<<<<<<
            # >>>>>>>>>Iterates over "news" and "news_images" at the same time, adding each image to the corresponding list>>>>>>>>>
            for news_item, image in zip(news, news_images):
                news_item.append(image)
            # <<<<<<<<<Iterates over "news" and "news_images" at the same time, adding each image to the corresponding list<<<<<<<<<

            return {
                "status": True,
                "bot": bot,
                "data": news
            }
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
    # <<<<<<<<<Function to extract all data from Aljazeera website<<<<<<<<<

    # >>>>>>>>>Prompts for a valid email>>>>>>>>>
    def get_valid_email(self):
        while True:
            email = input("Enter email to receive excel file: ")
            if email.strip():  # Check if the email is not empty after removing spaces
                return email
            else:
                print("Email cannot be empty. Please enter a valid email.")
    # <<<<<<<<<Prompts for a valid email<<<<<<<<<

    # >>>>>>>>>Prompts for a valid search phrase>>>>>>>>>
    def get_valid_search_phrase(self):
        while True:
            search_phrase = input("Enter the search phrase for Aljazeera's Website: ")
            if search_phrase.strip():  # Check if the search phrase is not empty after removing spaces
                return search_phrase
            else:
                print("Search phrase cannot be empty. Please enter a valid search phrase.")
    # <<<<<<<<<Prompts for a valid search phrase<<<<<<<<<

    # >>>>>>>>>Prompts for a number between 0 and 9>>>>>>>>>
    def get_valid_show_more(self):
        while True:
            show_more = input("Show more how many times (0-9): ")
            if show_more.isdigit() and 0 <= int(show_more) <= 9:  # Check if it's a number and between 0 and 9
                return int(show_more)
            else:
                print("Please enter a valid number between 0 and 9.")
    # <<<<<<<<<Prompts for a number between 0 and 9<<<<<<<<<

    # >>>>>>>>>Prompts for sending the report via email (Yes or No)>>>>>>>>>
    def get_valid_send_email(self):
        while True:
            send_email = input("Do you want to send the report by email? (Yes/No): ").strip().upper()
            if send_email in ['YES', 'NO']:
                return True if send_email == "YES" else False
            else:
                print("Please enter 'Yes' or 'No'.")
    # <<<<<<<<<Prompts for sending the report via email (Yes or No)<<<<<<<<<
