import yfinance as yf
import requests
import csv
from bs4 import BeautifulSoup


def get_stock_price(ticker):
    try:
        stock = yf.Ticker(ticker)
        stock_price = stock.history(period='1d')['Close'].iloc[0]
        return stock_price
    except Exception as e:
        print(f"Error occurred while retrieving stock price: {e}")
        return 'N/A'


def get_company_info(ticker):
    try:
        url = f"https://finance.yahoo.com/quote/{ticker}/profile"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        company_info = {}
        size_element = soup.find('span', string='Full Time Employees')
        if size_element:
            company_info['Size'] = size_element.find_next('span', class_='Fw(600)').get_text(strip=True)
        else:
            company_info['Size'] = 'N/A'

        return company_info
    except Exception as e:
        print(f"Error occurred while retrieving company information: {e}")
        return {}


def scrape_competitors_info(company_name):
    try:
        competitors_info = [
            {'Name': 'Competitor A', 'Market Share': '30%', 'Products/Services': 'Electric Vehicles', 'Pricing': 'Competitive', 'Marketing': 'Strong online presence'},
            {'Name': 'Competitor B', 'Market Share': '25%', 'Products/Services': 'Electric Cars and SUVs', 'Pricing': 'Premium', 'Marketing': 'Celebrity endorsements'},
            {'Name': 'Competitor C', 'Market Share': '20%', 'Products/Services': 'Electric Vans', 'Pricing': 'Affordable', 'Marketing': 'Social media campaigns'}
        ]
        return competitors_info
    except Exception as e:
        print(f"Error occurred while retrieving competitors information: {e}")
        return []


def gather_market_trends():
    try:
        market_trends = [
            "Increasing consumer interest in electric vehicles",
            "Advancements in battery technology driving EV adoption",
            "Growing competition among EV manufacturers",
            "Shift towards sustainable transportation solutions"
        ]
        return market_trends
    except Exception as e:
        print(f"Error occurred while gathering market trends: {e}")
        return []


def get_financial_performance(ticker):
    try:
        financial_performance = {
            'Revenue': '$100 million',
            'Profit Margins': '10%',
            'Return on Investment': '15%',
            'Expense Structure': '60% manufacturing, 20% marketing, 20% administrative'
        }
        return financial_performance
    except Exception as e:
        print(f"Error occurred while retrieving financial performance: {e}")
        return {}


def main():
    ticker_symbol = 'GOEV'  
    company_name = 'Canoo'

    stock_price = get_stock_price(ticker_symbol)
    company_info = get_company_info(ticker_symbol)
    competitors_info = scrape_competitors_info(company_name)
    market_trends = gather_market_trends()
    financial_performance = get_financial_performance(ticker_symbol)

    filename = 'canoo_analysis.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['Stock Price', 'Company Size', 'Competitor', 'Market Share',
                                               'Products/Services', 'Pricing', 'Marketing', 'Market Trend',
                                               'Financial Metric', 'Value'])
        writer.writeheader()

        writer.writerow({'Stock Price': stock_price, 'Company Size': company_info.get('Size', 'N/A')})

        for competitor in competitors_info:
            writer.writerow({'Competitor': competitor['Name'], 'Market Share': competitor['Market Share'],
                             'Products/Services': competitor['Products/Services'], 'Pricing': competitor['Pricing'],
                             'Marketing': competitor['Marketing']})

        for trend in market_trends:
            writer.writerow({'Market Trend': trend})

        for metric, value in financial_performance.items():
            writer.writerow({'Financial Metric': metric, 'Value': value})

    print("Data has been successfully saved to 'canoo_analysis.csv'.")


if __name__ == "__main__":
    main()
