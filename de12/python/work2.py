name=input("名前を教えて下さい")
waist=float(input("腹囲は？"))
age=int(input("年齢は？"))

print(name, "さんは、身長",waist,"cm、年齢",age,"才ですね。")

if waist>=160 and age>=19:
    print(name,"さん、内臓脂肪蓄積注意です")
else:
    print(name,"さん、腹囲は問題ありません")

