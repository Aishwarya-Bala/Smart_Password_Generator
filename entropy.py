class PasswordStrength:
    def __init__(self):
        import re
        self.numeric = re.compile('\d')
        self.loweralpha = re.compile('[a-z]')
        self.upperalpha = re.compile('[A-Z]')

        self.symbols = re.compile('[-_.:,;<>?"#$%&/()!@~]')
        self.num_of_symbols = 30

    def calculate_entropy(self, password = ''):
        import re
        from math import log, pow
        charset = 0
        if self.numeric.search(password):
            charset += 10
        if self.loweralpha.search(password):
            charset += 26
        if self.upperalpha.search(password):
            charset += 26
        if self.symbols.search(password):
            charset += self.num_of_symbols

        entropy = log(pow(charset, len(password)),2)
        return entropy