import calendar
import datetime
import logging
import random
import time
from functools import partial
from json import loads
from multiprocessing import Pool
import pytz

from yahoofinancials.maps import COUNTRY_MAP, REQUEST_MAP, USER_AGENTS
from yahoofinancials.sessions import SessionManager, _init_session
from yahoofinancials.utils import remove_prefix, get_request_config, get_request_category

# track the last get timestamp to add a minimum delay between gets - be nice!
_lastget = 0


# Custom Exception class to handle custom error
class ManagedException(Exception):
    pass


# Class used to get data from urls
class UrlOpener:
    request_headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "origin": "https://finance.yahoo.com",
        "referer": "https://finance.yahoo.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
    }
    user_agent = random.choice(USER_AGENTS)
    request_headers["User-Agent"] = user_agent

    def __init__(self, session):
        self._session_manager = SessionManager(session=session)

    def open(self, url, request_headers=None, params=None, proxy=None, timeout=30):
        pass

    def get_data(self, session, url, request_headers=None, params=None, proxy=None, timeout=30):
        pass


class YahooFinanceData(object):

    def __init__(self, ticker, **kwargs):
        self.ticker = ticker.upper() if isinstance(ticker, str) else [t.upper() for t in ticker]
        self.country = kwargs.get("country", "US")
        if self.country.upper() not in COUNTRY_MAP.keys():
            raise ReferenceError("invalid country: " + self.country)
        self.concurrent = kwargs.get("concurrent", False)
        self.max_workers = kwargs.get("max_workers", 8)
        self.timeout = kwargs.get("timeout", 30)
        self.proxies = kwargs.get("proxies")
        self.session = kwargs.pop("session", None)
        self.flat_format = kwargs.get("flat_format", False)
        self._cache = {}

    # Minimum interval between Yahoo Finance requests for this instance
    _MIN_INTERVAL = 7

    # Meta-data dictionaries for the classes to use
    YAHOO_FINANCIAL_TYPES = {
        'income': [
            'income_statement',
            'incomeStatementHistory',
            'incomeStatementHistoryQuarterly',
            'incomeStatements'
        ],
        'balance': [
            'balance_sheet',
            'balanceSheetHistory',
            'balanceSheetHistoryQuarterly',
            'balanceSheetStatements',
        ],
        'cash': [
            'cash_flow',
            'cashflowStatementHistory',
            'cashflowStatementHistoryQuarterly',
            'cashflowStatements',
        ],
        'keystats': ['key-statistics'],
        'history': ['history'],
        'profile': ['summaryProfile']
    }

    # Interval value translation dictionary
    _INTERVAL_DICT = {
        'daily': '1d',
        'weekly': '1wk',
        'monthly': '1mo'
    }

    # Base Yahoo Finance URL for the class to build on
    _BASE_YAHOO_URL = 'https://finance.yahoo.com/quote/'

    # private static method to get the appropriate report type identifier
    @staticmethod
    def get_report_type(frequency):
        pass

    # Public static method to format date serial string to readable format and vice versa
    @staticmethod
    def format_date(in_date):
        pass

    # Private Static Method to Convert Eastern Time to UTC
    @staticmethod
    def _convert_to_utc(date, mask='%Y-%m-%d %H:%M:%S'):
        pass

    # _get_proxy randomly picks a proxy in the proxies list if not None
    def _get_proxy(self):
        pass

    # Private method that determines number of workers to use in a process
    def _get_worker_count(self):
        pass

    # Private method to construct historical data url
    def _construct_url(self, symbol, config, params, freq, request_type):
        pass

    # Private method to execute a web scrape request and decrypt the return
    def _request_handler(self, url, res_field=""):
        pass

    @staticmethod
    def _format_raw_fundamental_data(raw_data):
        pass

    @staticmethod
    def _format_raw_module_data(raw_data, tech_type):
        pass

    # Private method to _get_historical_data from yahoo finance
    def _get_historical_data(self, url, config, tech_type, statement_type):
        pass

    # Private static method to determine if a numerical value is in the data object being cleaned
    @staticmethod
    def _determine_numeric_value(value_dict):
        pass

    # Private method to format date serial string to readable format and vice versa
    def _format_time(self, in_time):
        pass

    # Private method to return a sub dictionary entry for the earning report cleaning
    def _get_cleaned_sub_dict_ent(self, key, val_list):
        pass

    # Private method to process raw earnings data and clean
    def _clean_earnings_data(self, raw_data):
        pass

    # Private method to clean summary and price reports
    def _clean_reports(self, raw_data):
        pass

    # Private Static Method to ensure ticker is URL encoded
    @staticmethod
    def _encode_ticker(ticker_str):
        pass

    # Private Method to clean the dates of the newly returns historical stock data into readable format
    def _clean_historical_data(self, hist_data, last_attempt=False):
        pass

    # Private Static Method to build API url for GET Request
    def _build_api_url(self, hist_obj, up_ticker, v="2", events=None):
        pass

    # Private Method to get financial data via API Call
    def _get_api_data(self, api_url, tries=0):
        pass

    # Private Method to clean API data
    def _clean_api_data(self, api_url):
        pass

    # Private Method to Handle Recursive API Request
    def _recursive_api_request(self, hist_obj, up_ticker, clean=True, i=0):
        pass

    # Private Method to take scrapped data and build a data dictionary with, used by get_stock_data()
    def _create_dict_ent(self, up_ticker, statement_type, tech_type, report_name, hist_obj):
        pass

    def _retry_create_dict_ent(self, up_ticker, statement_type, tech_type, report_name, hist_obj):
        pass

    # Private method to return the stmt_id for the reformat_process
    def _get_stmt_id(self, statement_type, raw_data):
        pass

    # Private Method for the Reformat Process
    @staticmethod
    def _reformat_stmt_data_process(raw_data):
        pass

    # Private Method for the Flat Reformat Process
    @staticmethod
    def _reformat_stmt_data_process_flat(raw_data):
        pass

    # Private Method to return subdict entry for the statement reformat process
    def _get_sub_dict_ent(self, ticker, raw_data):
        pass

    # Public method to get time interval code
    def get_time_code(self, time_interval):
        pass

    # Public Method to get stock data
    def get_stock_data(self, statement_type='income', tech_type='', report_name='', hist_obj={}):
        pass

    # Public Method to get technical stock data
    def get_stock_tech_data(self, tech_type):
        pass

    # Public Method to get reformatted statement data
    def get_reformatted_stmt_data(self, raw_data):
        pass

    # Public method to get cleaned report data
    def _clean_data_process(self, tick, report_type, raw_report_data):
        pass

    # Public method to get cleaned summary and price report data
    def get_clean_data(self, raw_report_data, report_type):
        pass

    # Private method to handle dividend data requests
    def _handle_api_dividend_request(self, cur_ticker, start, end, interval):
        pass

    # Public method to get daily dividend data
    def get_stock_dividend_data(self, start, end, interval):
        pass
