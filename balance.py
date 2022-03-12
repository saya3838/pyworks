initial_balance = int(input("残高により利子率が変わります。残高はおいくらですか? "))
RATE = 1.1 if initial_balance >= 100_000 else 1.01  #この書き方の場合、最後に：は必要ない。
print(f"残高から、利子率は{RATE:.2f}％になります。")
print(f"0年: {initial_balance:,.2f}円")
print(f"1年: {initial_balance * RATE:,.2f}円")
print(f"2年: {initial_balance * RATE * RATE:,.2f}円")