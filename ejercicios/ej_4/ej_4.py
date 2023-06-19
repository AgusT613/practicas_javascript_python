from random import choice

class Password():
    # Default password constructor
    def __init__(
        self,
        length: int = 8,
        numbers_or_without: bool = True,
        uppercase_or_lower = 'lower',
        symbols_or_without: bool = False
    ):
        self.length = length
        self.numbers_or_without = numbers_or_without
        self.upper_or_lower = uppercase_or_lower
        self.symbols_or_without = symbols_or_without
    
    @staticmethod
    def output_message(password: str, length: int, with_numbers: str, with_letters: str, with_symbols: str):
        message = f"""
        Password config:
            - Length: {length}
            - Numbers: {with_numbers.capitalize()}
            - Letters: {with_letters.capitalize()}
            - Symbols: {with_symbols.capitalize()}
            
            - Password --> {password}
        """
        print(message)
    
    # Function for numbers
    @staticmethod
    def numbers(): 
        return list(range(48, 58))
    # Function for uppercase or lowercase
    @staticmethod
    def text_case(lower_or_upper: str = 'lower') -> list:
        # ASCII Code
        if lower_or_upper == 'upper': return list(range(65, 91))
        return list(range(97, 123))
    # Function for symbols
    @staticmethod
    def symbols():
        return \
        list(range(33, 48)) + \
        list(range(58, 65)) + \
        list(range(91, 97)) + \
        list(range(123, 127))
    
    # Generates a password with the default parameters
    def generate(self):
        full_password = str()
        
        # 3° Condition - No numbers, no letters, symbols
        if not self.numbers_or_without and self.upper_or_lower == "" and self.symbols_or_without:
            while len(full_password) < self.length:
                full_password += chr(choice(Password.symbols()))
            return Password.output_message(
                full_password,
                self.length,
                with_numbers='no',
                with_letters='no',
                with_symbols='yes'
            )
        
        # 2° Condition - No numbers, letters, symbols
        if not self.numbers_or_without and self.upper_or_lower != "" and self.symbols_or_without:
            while len(full_password) < self.length:
                if self.upper_or_lower == 'lower':
                    letters_and_symbols = Password.text_case() + Password.symbols()
                    full_password += chr(choice(letters_and_symbols))
                else: 
                    letters_and_symbols = Password.text_case('upper') + Password.symbols()
                    full_password += chr(choice(letters_and_symbols))
            return Password.output_message(
                full_password,
                self.length,
                with_numbers='no',
                with_letters='yes',
                with_symbols='yes'
            )
        
        # 1° Condition - No numbers, letters, no symbols
        if not self.numbers_or_without and self.upper_or_lower != "":
            while len(full_password) < self.length:
                if self.upper_or_lower == 'lower': full_password += chr(choice(Password.text_case()))
                else: full_password += chr(choice(Password.text_case('upper')))
            return Password.output_message(
                full_password, 
                self.length,
                with_numbers='no',
                with_letters='yes',
                with_symbols='no'
            )
 
        # Default Condition - Numbers, letters, no symbols
        while len(full_password) < self.length:
            full_password += chr(choice(Password.numbers() + Password.text_case()))
        return Password.output_message(
            full_password,
            self.length,
            with_letters='yes',
            with_numbers='yes',
            with_symbols='no'
        )

#TEST
if __name__ == '__main__':
    Password().generate()
    Password(length=16).generate()
    Password(numbers_or_without=False).generate()
    Password(numbers_or_without=False, uppercase_or_lower='lower').generate()
    Password(numbers_or_without=False, uppercase_or_lower='upper').generate()
    Password(numbers_or_without=False, uppercase_or_lower="", symbols_or_without=True).generate()
    pass