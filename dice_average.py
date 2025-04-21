import random
kaisuu = [10, 100, 1000, 10000, 1000000] # 平均値用のリスト

def roll_average(trial):
    average = 0 # 平均値の初期化
    total = 0 # サイコロの出目の合計値を記録する変数
    for n in range(trial): # trial分だけループ処理
        # この部分に具体的な処理を書く
        x=random.randint(1,6)
        total=total+x
    average=total/trial
    return average

# リスト[kaisuu]までの平均値を求める処理
for i in kaisuu:
    print(str(i)+"回試行の平均値："+str(roll_average(i)))

# 期待される実行結果例
""" 
10回試行の平均値：3.9
100回試行の平均値：3.38
1000回試行の平均値：3.435
10000回試行の平均値：3.5103
1000000回試行の平均値：3.498772 
"""
