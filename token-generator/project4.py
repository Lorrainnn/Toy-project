# project4.py
#
# ICS 33 Fall 2023
# Project 4: Still Looking for Something
import random

class Grammar:
    """
    The most outer Class that extract info from the input file_path
    and generate full sentences recursively.
    """
    def __init__(self, path, start_var):
        self.path = path
        self.rules = {}
        self.start_var = Variable('['+start_var+']')

    def parse(self):
        """
        Extract all valid info from file
        """
        with open(self.path, 'r') as f:
            content = f.readlines()
        content = [line.strip('\n') for line in content]

        while content:

            opener_index = content.index('{')
            closer_index = content.index('}')

            rule = content[opener_index + 1:closer_index]
            rule = Rule(rule).process_rule()
            self.rules.update(rule)
            content = content[closer_index + 1:]



    def randomly_match_var(self, var):
        """
        Process randomly choice based on weight
        """
        sentences = self.rules[var]
        weights, texts = zip(*((ele[0], ele[1]) for ele in sentences))
        chosen_text = random.choices(texts, weights = weights)[0]
        return chosen_text

    def generate_full_sentence(self, current_sentence):
        """
        Iterate among the rule and replace all variables until there is no variable
        for example, same to Apply A → 0 A 1 A | B
        """
        if any(isinstance(item, Variable) for item in current_sentence):

            index, item = next((i, item) for i, item in enumerate(current_sentence) if isinstance(item, Variable))
            current_sentence[index:index + 1] = self.randomly_match_var(item)
            return self.generate_full_sentence(current_sentence)
        else:
            # No more non-terminals, return the final list
            return current_sentence

    def Grammar_generator(self):
        """
        Integrations of all functions
        """
        self.parse()
        sentences = self.randomly_match_var(self.start_var)
        raw_content = self.generate_full_sentence(sentences)
        process_content = [ele.get_value() for ele in raw_content]
        print(' '.join(str(ele) for ele in process_content if ele != ''))




class Rule:
    """
    Process 1 rule (which is 1 line) and return a processed rule as {var:[(option1), {option2)...]}
    For example, the expected input should be ['HowIsBoo', '1 Boo is [Adjective] today']
    or ['Adjective', '3 happy', '3 perfect', ...]
    """
    def __init__(self, rule):
        self.rule = rule
        self.var_name = Variable('['+rule[0]+']')
        self.options = []

    def process_rule(self):
        """
        Extract different elements from a rule
        """
        rule = self.rule[1:]
        for ele in rule:
            elements = ele.split(' ')
            processed_rule = (elements[0], elements[1:])
            processed_rule = Options(processed_rule).process_option()
            self.options.append(processed_rule)
        return {self.var_name:self.options}


class Options:
    """
    Convert Options using basic tokens (variable and terminal)
    The expected input should be for example ('3', ['happy']) or
    ('1', ['Boo', 'is', '[Adjective]', 'today'])
    """
    def __init__(self, content):
        self.data = content[1]
        self.weigh = int(content[0])
        self.contents = []

    def process_option(self):
        """
        Separate one single rule's weight and tokens
        """
        for ele in self.data:
            if ele == '':
                self.contents.append(Terminal(ele))
            elif ele[0] == '[' and ele[-1] == ']':
                self.contents.append(Variable(ele))
            else:
                self.contents.append(Terminal(ele))

        return self.weigh, self.contents

class Variable:
    """
    Basic Symbol.
    Hashable as key used in self.rules(dict)
    """
    def __init__(self, var):
        self._var = var

    def __hash__(self):
        return hash(self._var)

    def __eq__(self, other):
        if isinstance(other, Variable):
            return self._var == other._var



class Terminal:
    """
    Basic Symbol.
    Hashable and has function: get_value to access the value stored in token.
    """
    def __init__(self, text):
        self._text = text


    def __hash__(self):
        return hash(self._text)

    def __eq__(self, other):
        if isinstance(other, Terminal):
            return self._text == other._text


    def get_value(self):
        return self._text



def main() -> None:
    # The user should only input these in order.
    path = input()
    num = int(input())
    start_var = input()

    generator = Grammar(path, start_var)
    # Call the generator for expected time and thus return expected num of statement
    for _ in range(num):
        generator.Grammar_generator()


if __name__ == '__main__':
    main()
