# https://aonecode.com/amazon-online-assessment-secret-fruits
# https://leetcode.com/discuss/interview-question/1002811/Amazon-or-OA-20201-or-Fresh-Promotion

# 1. func that goes through curr_secret list and sees if there's a match.
# 2. loop customerpurchased:
def matchSecretLists(secretFruitList: List[List[str]], customerPurchasedList: List[str]) -> bool:
    if len(secretFruitList[0]) == 1 and secretFruitList[0][0] == "anything": return False

    m = len(customerPurchasedList)

    def valid_secret(sec_i, purch_i):
        print("sec_i = %d, purch_i = %d" % (sec_i, purch_i))
        for sec_fruit in secretFruitList[sec_i]:
            if purch_i >= m: return False
            c_fruit = customerPurchasedList[purch_i]
            if (sec_fruit == "anything" or c_fruit == "anything" or sec_fruit == c_fruit):
                purch_i += 1
                continue
            else:
                return False

        return True

    sec_i = 0
    purch_i = 0
    while purch_i < m:
        if valid_secret(sec_i, purch_i):
            print("VALID")

            purch_i += len(secretFruitList[sec_i]) - 1
            sec_i += 1
            # print("sec_i = %d, purch_i = %d"%(sec_i,purch_i))

        # check if reached end of secret List
        if sec_i == len(secretFruitList):
            return True
        purch_i += 1
        print("end while")

    return False