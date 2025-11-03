waist_list=[] #waist_listというリストを作る
for i in range(1,4):
    print(i,"人目")
    waist=float(input("腹囲は？"))

    waist_list.append(waist) #ここでwaistという変数の値をリストに追加している

l=len(waist_list) #waist_listというリストの件数
s=sum(waist_list) #waist_listというリストの合計
mean=s/l #合計を件数で割って平均を求めmeanという変数に代入

print("今回の腹囲の平均は",mean,"cmです")
