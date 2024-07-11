
# Date : 7/11/2024
# Name:Ilyosbek
# Telegram : @valixonov04
#instagram : valixono.v_04
# Checking whether the products are available or not
print("Please. Can you choose 5 things!")
products = ["olma", "hurmo", "shaftoli", "behi", "sholg'om", "anjir", "sabzi", "kartoshka", "tuhum", "non", "tuz"]
basket = []

for numer in range(5):
    basket.append(input(f"Can you choose {numer + 1}-product? "))
if basket:
 for product in basket:
    if product in products:
        print(f"This is {product}. We have it!")
    else:
        print(f"This is {product}. We do not have it.")
else:
    print("Your basket empty")