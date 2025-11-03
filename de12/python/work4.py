for i in range(1,4): #コロンが入っていることに注意1以上3未満
    print(i,"人目") #タブでずらしていることに注意！
    name=input("やぎ")
    waist=float(input("腹囲は？"))
    age=int(input("年齢は？"))

    print(name, "さんは、身長",waist,"cm、年齢",age,"才ですね。")

    if waist>=160 and age>=19:
        print(name,"さん、内臓脂肪蓄積注意です")
    else:
        print(name,"さん、腹囲は問題ありません")

# 出力結果
# 0 人目
# 1 人目
# 2 人目
