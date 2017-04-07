# Write a Python procedure fix_machine to take 2 string inputs
# and returns the 2nd input string as the output if all of its
# characters can be found in the 1st input string and "Give me
# something that's not useless next time." if it's impossible.
# Letters that are present in the 1st input string may be used
# as many times as necessary to create the 2nd string (you
# don't need to keep track of repeat usage).

#one way to def fix_machine
def fix_machine(debris,product):
    i = 0
    while i < len(product):
        if debris.find(product[i]) != -1:
            i = i + 1
        else:
            return "Give me something that's not useless next time."
    return product


#another way to def fix_machine

def fix_machine(a, b):
    return b if set(a)>=set(b) else "Give me something that's not useless next time."

### TEST CASES ###
print "Test case 1: ", fix_machine('UdaciousUdacitee', 'Udacity') == "Give me something that's not useless next time."
print "Test case 2: ", fix_machine('buy me dat Unicorn', 'Udacity') == 'Udacity'
print "Test case 3: ", fix_machine('AEIOU and sometimes y... c', 'Udacity') == 'Udacity'
print "Test case 4: ", fix_machine('wsx0-=mttrhix', 't-shirt') == 't-shirt'
