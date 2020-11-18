# write your code here
def add(*args):
    total = 0
    for n in args:
        total += int(n)
    return total

def substract(*args):
    total = int(args[0])
    args = args[1:len(args) + 1]
    for n in args:
        total -= int(n)
    return total

def multiply(*args):
    total = int(args[0])
    args = args[1:len(args) + 1]
    for n in args:
        total = total * int(n)
    return total

def divide(*args):
    total = int(args[0])
    args = args[1:len(args) + 1]
    for n in args:
        total = total // int(n)
    return total

def calculate(inp):  # evaluate in-fix input
    # invalid - not integers
    if len(inp) == 1:
        return inp[0]
    else:
        while len(inp) > 1:
            calc_group = []
            calc_group.extend(inp[0:3])
            if "+" in calc_group[1]:
                del calc_group[1]
                del inp[0:3]
                result = add(*calc_group)
                inp.insert(0, result)
            elif "-" in calc_group[1]:
                if len(calc_group[1]) % 2 == 0:
                    del calc_group[1]
                    del inp[0:3]
                    result = add(*calc_group)
                    inp.insert(0, result)
                else:
                    del calc_group[1]
                    del inp[0:3]
                    result = substract(*calc_group)
                    inp.insert(0, result)
        return result

inp_storage = {}

def inp_process(inp):  # assign variable or return number only to be processed
    global inp_storage
    # print("storage dictionary", inp_storage)
    # we process the input based on potential delimiters
    if "(" in inp:
        inp = "( ".join(inp.split("("))

    if ")" in inp:
        inp = " )".join(inp.split(")"))

    if "+" in inp and "+++" not in inp:
        inp = " + ".join(inp.split("+"))

    if "-" in inp and "--" not in inp:
        inp = " - ".join(inp.split("-"))

    if "*" in inp:
        inp = " * ".join(inp.split("*"))

    if "/" in inp and not inp.startswith("/"):
            inp = " / ".join(inp.split("/"))

    if "=" in inp:
        new_inp = inp.replace(" ", "").split("=")
    # at this point, we have a list delimited by operation characters



    else:
        new_inp = inp.split()

        # print("after", inp)
        # new_inp = inp.split() # in this case, it's just operations, we check every isalpha()
    # print(new_inp)
    # print("length of input", new_inp, len(new_inp))
    if len(new_inp) == 1:
        if new_inp[0] in inp_storage:
            return inp_storage[new_inp[0]]
        elif new_inp[0][0] in ["+", "-"]:
            return new_inp
        else:
            return "Unknown variable"

    # the follow code block represents the if equal sign exists block and only 3 characters

    elif len(new_inp) == 2:
        if "=" in inp:  #assignment
            if any(char.isdigit() for char in new_inp[0]):
                    return "Invalid identifier"
                # any var with int is wrong, otherwise it's good

            if new_inp[1].isalpha():
                if new_inp[1] in inp_storage:
                      inp_storage[new_inp[0]] = inp_storage[new_inp[1]]
                      # store new value of new key as old value of old key
                else:
                    return "Invalid assignment"

            elif new_inp[1].isnumeric():
                inp_storage[new_inp[0]] = new_inp[1]  # stores variables
        # when assignment is done correctly, we return None
            else:
                return "Invalid assignment"
    else:  # operation
        # print("operation input list", new_inp)
        if "=" in inp:
            return "Invalid assignment"

        else:
            for i, j in enumerate(new_inp):
                if j.isalpha():
                    if j in inp_storage:
                        new_inp[i] = inp_storage[j]
                    else:
                        return "variable not defined yet (do we need this)"
            # print("new_inp_end", new_inp)
            # print("output from inp_process", new_inp)
            return new_inp  #we return a list
            # return " ".join(new_inp)  # this entire function returns 1) error message if occurs
                              # 2) clean string separate by space for calculate step
                              # 3) a single value if input len is 1

class Stack:
    def __init__(self):
        self.items = []  # stack itself is a list

    def push(self, items):
        self.items.append(items)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def isEmpty(self):
        return self.items == []

    def count(self):
        return len(self.items)

def postfix_eval(inp):   # evaluate based on postfix input
    # Iterate over the expression for conversion
    temp = []
    inp = inp.split()
    for i in inp:
        # If the scanned character is an operand
        # (number here) push it to the stack
        if i.isdigit():
            temp.append(i)

        # If the scanned character is an operator,
        # pop two elements from stack and apply it.
        elif i == "+" or i == "--" or i == "+++" or i == "+++++":
            val1 = temp.pop()
            val2 = temp.pop()
            temp.append(add(val1, val2))
        elif i == "-":
            val2 = temp.pop()
            val1 = temp.pop()
            temp.append(substract(val1, val2))
        elif i == "*":
            val1 = temp.pop()
            val2 = temp.pop()
            temp.append(multiply(val1, val2))
        elif i == "/" or i == "//":
            val2 = temp.pop()
            val1 = temp.pop()
            temp.append(divide(val1, val2))

    return int(temp.pop())

def infix_postfix(inp):  # convert to postfix
    oup = []  # contain character and then function adds
    # operator at the right time based on priority
    stack_1 = Stack()  # only contain operators or "()"
    prec_dict = {}
    prec_dict["+"] = 2
    prec_dict["-"] = 2
    prec_dict["--"] = 2
    prec_dict["+++"] = 2
    prec_dict["*"] = 3
    prec_dict["/"] = 3
    prec_dict["//"] = 3
    prec_dict["("] = 1
    prec_dict["+++++"] = 2
    # print("start of inflix", inp)
    for char in inp:
        if char.isalnum():
            oup.append(char)
        elif char == "(":
            stack_1.push(char)
        elif char == ")":
            top_token = stack_1.pop()
            while top_token != "(":
                oup.append(top_token)
                top_token = stack_1.pop()
                # pop the stack and append any operators onto the output
        elif len(char) > 1 and char.startswith("-") and char != "--":
            oup.append(char)
        # we then need to handle priorities
        else:
            while (not stack_1.isEmpty()) and \
                (prec_dict[stack_1.peek()] >= prec_dict[char]):
                oup.append(stack_1.pop())  # keep pop stack and append to
                # output list until stack is empty or precedence isn't met
            stack_1.push(char)  # once stack meeting equal or higher priority
            # is popped and appended, we push the new operator in.  this means
            # all * and / operators must cause all other * or / to be popped first
            # before they can be pushed into the stack
    while not stack_1.isEmpty():
        oup.append(stack_1.pop())  # lasty empty stack and FIFO
            # append to output list
    return " ".join(oup)  # output the string


while True:
    inp = input()
    total = 0
    count_left = 0
    count_right = 0
    for n in inp:
        if n == "(":
            count_left += 1
        if n == ")":
            count_right += 1

    if count_left != count_right:
        print("Invalid expression")
        continue

    if "*" in inp:
        if inp.count("*") >= 2:
            print("Invalid expression")
            continue

    if "//" in inp:
        print("Invalid expression")
        continue

    if not inp:
        pass

    elif inp == "/help":
        print("The program calculates a sequence of + and -")
    elif inp == "/exit":
        print("Bye!")
        break
    elif inp[0] == "/" and inp[1:len(inp) + 1] not in ["help", "exit"]:
        print("Unknown command")
    else:
        if inp_process(inp) == None:
            continue
        elif isinstance(inp_process(inp), list):
            # print(inp)
            inp = inp_process(inp)  # returns a list
            # print("after inp_process", inp)
            inp = infix_postfix(inp) # feeds the list and return a Postfix string
            # print("after infix_postfix", inp)
            print(postfix_eval(inp))
        else:
            print(inp_process(inp))

