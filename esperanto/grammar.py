grammar = """
start: expr+

expr: operations

operations: count | sumary | translate | audio

count: "${" "word_count" "}""(" filename ")"

sumary: "${" "sumary" "}""(" filename ")""(" word ")"

translate: "${" "translate" "from" STRING "to" STRING "}" "(" filename ")" "(" filename ")"

audio: "${" "speech" "}""(" filename ")""(" filename ")"

filename: ALPHABET | NUMERIC | STRING | RELATIVE_PATH

word: ALPHABET | NUMERIC | STRING

RELATIVE_PATH: /(\/?(\.\.\/)+\w+(\.\w+)?)/

ALPHABET: /[A-Za-z._]+/
NUMERIC:  /[0-9]+/
STRING: /"[^"]*"/ | /'[^']*'/

%import common.WS
%ignore WS
%ignore /\\s+/
"""