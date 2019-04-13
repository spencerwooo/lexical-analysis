#! /usr/local/bin/python3

import sys

cKeywords = ['auto', 'break', 'case', 'char', 'const',
             'continue', 'default', 'do', 'double', 'else',
             'enum', 'extern', 'float', 'for', 'goto',
             'if', 'inline', 'int', 'long', 'register',
             'restrict', 'return', 'short', 'signed', 'sizeof',
             'static', 'struct', 'switch', 'typedef', 'union',
             'unsigned', 'void', 'volatile', 'while']

badChar = ''
index = 0


def preProcess(content):
  code = ''
  # Trim '\n'
  for character in content:
    if character != '\n':
      code = code + character

  return code


def scanner(code):
  global index
  wordType = ''

  codeWord = ''
  character = code[index]
  index = index + 1

  # Ignore white space
  while character == ' ':
    character = code[index]
    index = index + 1

  # Identifier!
  if character.isalpha() or character == '_':
    while character.isalpha() or character.isdigit() or character == '_':
      codeWord = codeWord + character
      character = code[index]
      index = index + 1
    # index = index - 1
    wordType = 'identifier'
    # Keyword!
    for keyword in cKeywords:
      if codeWord == keyword:
        wordType = 'keyword'
        break

  # String!
  elif character == '"':
    bracketCount = 0
    while index < len(code):
      codeWord = codeWord + character
      if character == '"':
        bracketCount = (bracketCount + 1) % 2
        if bracketCount == 0:
          break
      character = code[index]
      index = index + 1

    if bracketCount == 1:
      print('Illegal string.')
    else:
      wordType = 'string'
    # print(codeWord)
    # index = index - 1

  # Print identified word type and word itself
  if wordType != '':
    # if wordType == 'string':
    print(wordType + ': ' + codeWord)


def main():
  # Print usage if arguments are not legal
  if len(sys.argv) < 2:
    print('[Usage] ./scan.py <C source file path>')
    sys.exit(0)

  # Read file from file path taken from command line arguments
  filePath = sys.argv[1]
  with open(filePath, 'r', encoding='utf-8') as f:
    content = f.read()

  # Preprocess C source file
  code = preProcess(content)
  print(code)
  while index != len(code):
    scanner(code)


if __name__ == "__main__":
  main()
