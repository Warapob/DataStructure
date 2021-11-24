# """
# จงสร้าง vickrey auction แบบจำลอง
# Vickrey auction คือการประมวลที่ผู้ที่จะชนะการประมูล คือ ผู้ที่ยื่นซองเสนอราคาสูงที่สุด แต่จะจ่ายจริงในราคาที่สูงเป็นอันดับสองรองลงมา

# word
# "Enter All Bid : "
# "not enough bidder"
# "error : have more than one highest bid"
# "winner bid is $ need to pay $"

# """
x = [int(i) for i in input("Enter All Bid : ").split()]

highest = max(x)

if len(x) == 1:
    print("not enough bidder")
elif x.count(highest) > 1:
    print("error : have more than one highest bid")
else:
    x.remove(highest)
    nHigh = max(x)
    print("winner bid is {} need to pay {}".format(highest, nHigh))


