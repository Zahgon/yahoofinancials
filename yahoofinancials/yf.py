"""
==============================
The Yahoo Financials Module
Version: 1.20
==============================

Author: Connor Sanders
Email: jecsand@pm.me
Version Released: 12/17/2023
Tested on Python 3.7, 3.8, 3.9, 3.10, 3.11, and 3.12

Copyright (c) 2023 Connor Sanders
MIT License

List of Included Functions:

1) get_financial_stmts(frequency, statement_type, reformat=True)
   - frequency can be either 'annual' or 'quarterly'.
   - statement_type can be 'income', 'balance', 'cash'.
   - reformat optional value defaulted to true. Enter False for unprocessed raw data from Yahoo Finance.
2) get_stock_price_data(reformat=True)
3) get_stock_earnings_data()
   - reformat optional value defaulted to true. Enter False for unprocessed raw data from Yahoo Finance.
4) get_summary_data(reformat=True)
   - reformat optional value defaulted to true. Enter False for unprocessed raw data from Yahoo Finance.
5) get_stock_quote_type_data()
6) get_historical_price_data(start_date, end_date, time_interval)
   - Gets historical price data for currencies, stocks, indexes, cryptocurrencies, and commodity futures.
   - start_date should be entered in the 'YYYY-MM-DD' format. First day that financial data will be pulled.
   - end_date should be entered in the 'YYYY-MM-DD' format. Last day that financial data will be pulled.
   - time_interval can be either 'daily', 'weekly', or 'monthly'. Parameter determines the time period interval.

Usage Examples:
from yahoofinancials import YahooFinancials
#tickers = 'AAPL'
#or
tickers = ['AAPL', 'WFC', 'F', 'JPY=X', 'XRP-USD', 'GC=F']
yahoo_financials = YahooFinancials(tickers)
balance_sheet_data = yahoo_financials.get_financial_stmts('quarterly', 'balance')
earnings_data = yahoo_financials.get_stock_earnings_data()
historical_prices = yahoo_financials.get_historical_price_data('2015-01-15', '2017-10-15', 'weekly')
"""

from yahoofinancials.calcs import num_shares_outstanding, eps
from yahoofinancials.data import YahooFinanceData

__version__ = "1.20"
__author__ = "Connor Sanders"


# Class containing methods to create stock data extracts
class YahooFinancials(YahooFinanceData):
    """
    Arguments
    ----------
    tickers: str or list
        Ticker or listed collection of tickers
    Keyword Arguments
    -----------------
    concurrent: bool, default False, optional
        Defines whether the requests are made synchronously or asynchronously.
    country: str, default 'US', optional
        This allows you to alter the region, lang, corsDomain parameter sent with each request based on selected country
    max_workers: int, default 8, optional
        Defines the number of workers used to make concurrent requests.
        Only relevant if concurrent=True
    timeout: int, default 30, optional
        Defines how long a request will stay open.
    proxies: str or list, default None, optional
        Defines any proxies to use during this instantiation.
    flat_format: bool, default False, optional
        If set to True, returns fundamental data in a flattened format, i.e. without the list of dicts.
    """

    # Private method that handles financial statement extraction
    def _run_financial_stmt(self, statement_type, report_num, frequency, reformat):
        pass

    # Public Method for the user to get financial statement data
    def get_financial_stmts(self, frequency, statement_type, reformat=True):
        pass

    # Public Method for the user to get stock price data
    def get_stock_price_data(self, reformat=True):
        pass

    # Public Method for the user to return key-statistics data
    def get_key_statistics_data(self, reformat=True):
        pass

    # Public Method for the user to get company profile data
    def get_stock_profile_data(self, reformat=True):
        pass

    # Public Method for the user to get stock earnings data
    def get_stock_earnings_data(self):
        pass

    # Public Method for the user to return financial data
    def get_financial_data(self, reformat=True):
        pass

    # Public Method for the user to get stock summary data
    def get_summary_data(self, reformat=True):
        pass

    # Public Method for the user to get the yahoo summary url
    def get_stock_summary_url(self):
        pass

    # Public Method for the user to get stock quote data
    def get_stock_quote_type_data(self):
        pass

    # Public Method for the user to get stock quote data
    def get_esg_score_data(self):
        pass

    def _get_analytic_data(self, tech_type):
        pass

    # Public Method for user to get historical price data with
    def get_historical_price_data(self, start_date, end_date, time_interval):
        pass

    # Private Method for Functions needing stock_price_data
    def _stock_price_data(self, data_field):
        pass

    # Private Method for Functions needing stock_price_data
    def _stock_summary_data(self, data_field):
        pass

    # Private Method for Functions needing financial statement data
    def _financial_statement_data(self, stmt_type, stmt_code, field_name, freq):
        pass

    # Public method to get daily dividend data
    def get_daily_dividend_data(self, start_date, end_date):
        pass

    # Public Price Data Methods
    def get_current_price(self):
        pass

    def get_current_change(self):
        pass

    def get_current_percent_change(self):
        pass

    def get_current_volume(self):
        pass

    def get_prev_close_price(self):
        pass

    def get_open_price(self):
        pass

    def get_ten_day_avg_daily_volume(self):
        pass

    def get_stock_exchange(self):
        pass

    def get_market_cap(self):
        pass

    def get_daily_low(self):
        pass

    def get_daily_high(self):
        pass

    def get_currency(self):
        pass

    # Public Summary Data Methods
    def get_yearly_high(self):
        pass

    def get_yearly_low(self):
        pass

    def get_dividend_yield(self):
        pass

    def get_annual_avg_div_yield(self):
        pass

    def get_five_yr_avg_div_yield(self):
        pass

    def get_dividend_rate(self):
        pass

    def get_annual_avg_div_rate(self):
        pass

    def get_50day_moving_avg(self):
        pass

    def get_200day_moving_avg(self):
        pass

    def get_beta(self):
        pass

    def get_payout_ratio(self):
        pass

    def get_pe_ratio(self):
        pass

    def get_price_to_sales(self):
        pass

    def get_exdividend_date(self):
        pass

    # Financial Statement Data Methods
    def get_book_value(self):
        pass

    def get_ebit(self):
        pass

    def get_net_income(self):
        pass

    def get_interest_expense(self):
        pass

    def get_operating_income(self):
        pass

    def get_total_operating_expense(self):
        pass

    def get_total_revenue(self):
        pass

    def get_cost_of_revenue(self):
        pass

    def get_income_before_tax(self):
        pass

    def get_income_tax_expense(self):
        pass

    def get_gross_profit(self):
        pass

    def get_net_income_from_continuing_ops(self):
        pass

    def get_research_and_development(self):
        pass

    def get_recommendations(self):
        pass

    def get_insights(self):
        pass

    # Calculated Financial Methods
    def get_earnings_per_share(self):
        pass

    def get_num_shares_outstanding(self, price_type='current'):
        pass
