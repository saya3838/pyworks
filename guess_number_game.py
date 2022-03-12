#数あてゲーム
import random
try:
  while True:
    x = input('当てる数字の範囲を指定してください。（正の整数で入力。）')
    if len(x) !=0:
      answer = random.randint(1, int(x))
      while True:
        guess = int(input('数字を当ててください。答えは…'))
        if answer == guess:
          print('あたりです！！')
          break
        elif answer > guess:
          print('答えはそれよりも大きいです。')
        else:
          print('答えはそれよりも小さいです。')
    else:
      print('終了します。')
      break
except:
  print('半角数字で入力してください！')