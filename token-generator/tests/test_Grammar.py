
import unittest
import tempfile
from project4 import *
from unittest.mock import patch
import os
from contextlib import redirect_stdout
from io import StringIO
"""
Apply test double to check input/output/print/random.choice
"""

class Test_Grammar_class(unittest.TestCase):

    def test_Grammar_Parse(self):
        # Create a temporary file
        with tempfile.NamedTemporaryFile(mode = 'w', delete = False) as temp_file:
            temp_file.write("{\nHowIsBoo\n1 [today] Boo is [Adjective]\n}\n <I am comment>"
                            "\n{\ntoday\n1 \n}\n<I am comment>\n{\nAdjective\n3 happy\n}")

        try:
            generator = Grammar(temp_file.name, 'HowIsBoo')
            generator.parse()
            self.assertEqual(generator.rules, {
                Variable('[HowIsBoo]'): [
                    (1, [
                        Variable('[today]'),
                        Terminal('Boo'),
                        Terminal('is'),
                        Variable('[Adjective]')
                    ])
                ],
                Variable('[today]'): [
                    (1, [Terminal('')])
                ],
                Variable('[Adjective]'): [
                    (3, [Terminal('happy')])
                ]
            })
        finally:
            temp_file.close()
            os.remove(temp_file.name)


    def test_Grammar_random_match(self):
        with tempfile.NamedTemporaryFile(mode = 'w', delete = False) as temp_file:
            temp_file.write('{\nBoo\n2 happy\n3 sad\n2 relaxing\n}')

        try:
            generator = Grammar(temp_file.name, 'Boo')
            generator.parse()
            with patch('random.choices', return_value = [Terminal('happy')]):
                result = generator.randomly_match_var(Variable('[Boo]'))
            self.assertEqual(result, Terminal('happy'))
        finally:
            temp_file.close()
            os.remove(temp_file.name)


    def test_Grammar_generate_full_sentence_Muti_Replacement(self):
        with tempfile.NamedTemporaryFile(mode = 'w', delete = False) as temp_file:
            temp_file.write('{\nBoo\n3 [happy]\n}\n{\nhappy\n1 smile\n}'
                            '\n{\nQuestion\n1 Is Boo [Boo]\n}')

        try:
            generator = Grammar(temp_file.name, 'Question')
            generator.parse()

            # Use the actual variable from the grammar
            initial_sentence = generator.rules[generator.start_var][0][1]

            processed_sentence = generator.generate_full_sentence(initial_sentence)
            self.assertEqual(processed_sentence,
                             [Terminal('Is'), Terminal('Boo'), Terminal('smile')])
        finally:
            temp_file.close()
            os.remove(temp_file.name)

    def test_Grammar_generate_full_sentence_Muti_Variable(self):
        with tempfile.NamedTemporaryFile(mode = 'w', delete = False) as temp_file:
            temp_file.write('{\nBoo\n3 [happy]\n}\n{\nhappy\n1 smile\n}'
                            '\n{\nQuestion\n1 [Is] Boo [Boo]\n}'
                            '\n{\nIs\n2 How\n}')

        try:
            generator = Grammar(temp_file.name, 'Question')
            generator.parse()

            # Use the actual variable from the grammar
            initial_sentence = generator.rules[generator.start_var][0][1]

            processed_sentence = generator.generate_full_sentence(initial_sentence)
            self.assertEqual(processed_sentence,
                             [Terminal('How'), Terminal('Boo'), Terminal('smile')])
        finally:
            temp_file.close()
            os.remove(temp_file.name)

    def test_Grammar_generator(self):
        output_buffer = StringIO()
        with tempfile.NamedTemporaryFile(mode = 'w', delete = False) as temp_file:
            temp_file.write('{\nBoo\n3 [happy]\n}\n{\nhappy\n1 smile\n}'
                            '\n{\nQuestion\n1 Is Boo [Boo]\n}')


        try:
            with redirect_stdout(output_buffer):
                    test_class = Grammar(temp_file.name, 'Question')
                    test_class.Grammar_generator()
            output = output_buffer.getvalue()
            expected_output = "Is Boo smile\n"
            self.assertEqual(output, expected_output)

        finally:
            temp_file.close()
            os.remove(temp_file.name)
                

        








