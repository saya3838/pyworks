initial_balance = int(input("残高により利子率が変わります。残高はおいくらですか? "))
RATE = 1.1 if initial_balance >= 100_000 else 1.01  #この書き方の場合、最後に：は必要ない。
print(f"残高から、利子率は{RATE:.2f}％になります。")
after = int(input("何年後まで計算しますか？"))
for year in range(0, after+1):
  print(f"{year}年: {initial_balance * RATE ** year:,.2f}円")
