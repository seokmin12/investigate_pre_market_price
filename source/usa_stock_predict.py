from datetime import datetime
from dateutil.relativedelta import relativedelta
import FinanceDataReader as fdr
from pandas import DataFrame
from fbprophet import Prophet
import telegram
import math
import matplotlib.pyplot as plt

telegram_token = '1801532879:AAHdAYqh9cjMyoT4V4k0zTZe5t7iMRfmBHg'
bot = telegram.Bot(token=telegram_token)

now = datetime.now()

start = now - relativedelta(years=1)
end = now.strftime('%Y-%m-%d')

money = 95

symbol = input("Input a symbol to search: ")
symbol = symbol.upper()

df = fdr.DataReader(symbol, start, end)
df = df.reset_index()

raw_data = {'ds': list(df['Date']),
            'y': list(df['Close'])}

data = DataFrame(raw_data)

model = Prophet()
model.fit(data)

future = model.make_future_dataframe(periods=31, freq='D')
forecast = model.predict(future)

now_price = float(df['Close'].tail(1))

predict_trend = list(forecast['trend'])[-1]
predict_price = predict_trend - now_price

can_buy_stock_amount = math.trunc(float(money) / now_price)

profit = round(predict_price * can_buy_stock_amount, 3)

if predict_price > 0:
    if can_buy_stock_amount == 0:
        print("\n\n##########################")
        print("## It will be increased ##")
        print("##   You Can't Buy It   ##")
        print("##########################\n")
    else:
        print("\n\n#############################################################################")
        print("## It will be increased")
        print(f"## Now_Price: ${now_price}, Money($): {int(money)}, Predict_Profit: ${profit}")
        print("#############################################################################\n")
        bot.sendMessage(chat_id='1832322351', text=f"'{symbol}' wiil be increased\nNow_Price: ${now_price}, Money($): {int(money)}, Predict_Profit: ${profit}")
else:
    print("\n\n##########################")
    print("## It will be decreased ##")
    print("##########################\n")

# fig1 = model.plot(forecast)
# fig2 = model.plot_components(forecast)
# plt.show()

