


class InputChecks:
    def __init__(self, inp=""):
        self.inp = inp
        
    def check_int(self, inp):
        try:
            int(inp)
            return True
        except ValueError:
            return False
    
    def check_ssn(self, inp):
        count = 0
        for char in inp:
            if char.isdigit():
                count += 1
            else:
                return False
        
        if count == 10:
            if int(inp[0:2]) > 31:
                return False 
            elif int(inp[2:4]) > 12:
                return False
            elif int(inp[-1]) == 0 or int(inp[-1]) == 9:
                return True
            else:
                return False
        else:
            return False
                


a = InputChecks()
inp = input("enter input: ")
print(a.check_ssn(inp))
