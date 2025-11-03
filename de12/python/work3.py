name=input("名前を教えて下さい")
waist=input("腹囲は？")
age=input("年齢は？")

print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

#ここが修正されています
if waist>=85 and age>=40:
    print(name,"さん、内臓脂肪蓄積注意です")
else:
    print(name,"さん、腹囲は問題ありません")

a=int("10")#10という文字列を整数に変換してaに代入
b=float("1.5")#1.5という文字列を数字に変換してbに代入

name=input("名前を教えて下さい")
waist=float(input("腹囲は？"))
age=int(input("年齢は？"))
