import ccxt

binance = ccxt.binance({
    'apiKey': 'BINANCE_API_KEY',
    'secret': 'BINANCE_SECRET',
    'enableRateLimit': True,
})

# Parameters
coin = 'USDT'
amount = 10
address = 'YOUR_WHITELISTED_ADDRESS'
network = 'TRC20'  # Optional
tag = None  # Use if needed (e.g., for XRP)

# Withdraw
result = binance.withdraw(
    code=coin,
    amount=amount,
    address=address,
    tag=tag,
    params={'network': network}
)
print("Binance withdrawal:", result)
