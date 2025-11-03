import random
import time

directions = ["右", "左", "上", "下"]
score = 0

print("=== あっち向いてほい ゲーム ===")
print("3回勝負")

for round_num in range(1, 4):
    print(f"\n【{round_num}回戦】")
    input("じゃんけん ...（Enterを押して開始）")

    # じゃんけん部分
    janken = ["グー", "チョキ", "パー"]
    user_hand = input("グー・チョキ・パー のどれ？: ")
    computer_hand = random.choice(janken)
    print(f"あなた: {user_hand}　コンピュータ: {computer_hand}")

    # 勝敗判定
    if user_hand == computer_hand:
        print("あいこ！もう一度！")
        continue
    elif (user_hand == "グー" and computer_hand == "チョキ") or \
         (user_hand == "チョキ" and computer_hand == "パー") or \
         (user_hand == "パー" and computer_hand == "グー"):
        winner = "あなた"
    else:
        winner = "コンピュータ"

    print("あっち向いて〜")
    time.sleep(1)
    user_dir = input("右・左・上・下のどれ？: ")
    comp_dir = random.choice(directions)
    print(f"あなた: {user_dir}　コンピュータ: {comp_dir}")

    if user_dir == comp_dir:
        if winner == "あなた":
            print("あなたの勝ち！")
            score += 1
        else:
            print("あなたの負け")
    else:
        print("引き分け！")

print(f"\n=== 結果: {score}勝 ===")
if score >= 2:
    print("あなたの勝ち！")
else:
    print("コンピュータの勝ち！")

