from lark import Lark
from esperanto.Evaluator import Evaluator
from grammar import grammar

#evaluates the expression
def evaluate(expression):
  try:
    result = parser.parse(expression)
    return result
  except Exception as e:
    return f"Error: {e}" 

#creates the parser using the grammar
parser = Lark(grammar, parser='lalr', transformer=Evaluator())

#creates an expression
#expression = "${word_count}(test.txt)"
#expression = '${translate from "es" to "en"}(test.txt)(translate.txt)'
#expression = '${speech}("test.txt")("audio.mp3")'


#main function
def main():
    expression = input('Enter the expression in Esperanto: ')
    result = evaluate(expression)
    print(result)

if __name__ == '__main__':
    main()



