cong={
    7:5,
    18:22,
    32:8,
    71:5,
    66:6
}
bjp={
    7:15,
    18:20,
    32:4,
    71:9,
    66:2
}
c_sum=0
b_sum=0
for age,votes in cong.items():
    if age>=18:
        c_sum+=votes
for age,votes in bjp.items():
    if age>=18:
        b_sum+=votes
diff=abs(c_sum-b_sum)
if c_sum>b_sum:
    print('cong_win',diff)
else:
    print('bjp_wins',diff)
        