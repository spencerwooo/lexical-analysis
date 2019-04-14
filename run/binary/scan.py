#! /usr/local/bin/python3

import sys

# 关键词
cKeywords = ['auto', 'break', 'case', 'char', 'const',
             'continue', 'default', 'do', 'double', 'else',
             'enum', 'extern', 'float', 'for', 'goto',
             'if', 'inline', 'int', 'long', 'register',
             'restrict', 'return', 'short', 'signed', 'sizeof',
             'static', 'struct', 'switch', 'typedef', 'union',
             'unsigned', 'void', 'volatile', 'while']
# 转义字符
cEscSequence = ['\'', '"', '?', '\\', 'a', 'b', 'f', 'n', 'r', 't', 'v']

# 指针查找位置
index = 0

# Token 属性
codeNum = 1
wordType = ''
codeLine = 1
codeValue = ''
codeValid = 0

# 自动机状态
charState = 0
stringState = 0


def preProcess(content):
  code = ''
  # Trim leading white space 去掉每行最前面的空白
  for line in content:
    if line != '\n':
      code = code + line.lstrip()
    else:
      code = code + line
  return code


def scanner(code):
  # 当前扫描代码位置
  global index
  # 当前识别符数
  global codeNum
  # 当前代码行
  global codeLine

  # 识别到词语的类别
  global wordType
  wordType = ''
  # 识别到的词语
  global codeValue
  codeValue = ''
  # 当前识别字符
  character = code[index]
  index = index + 1

  # Ignore white space 忽略空白字符
  while character == ' ':
    character = code[index]
    index = index + 1

  # Identifier! 识别到了标识符！
  if character.isalpha() or character == '_':
    while character.isalpha() or character.isdigit() or character == '_':
      codeValue = codeValue + character
      character = code[index]
      index = index + 1
    wordType = 'identifier'
    # Keyword!
    for keyword in cKeywords:
      if codeValue == keyword:
        wordType = 'keyword'
        break

  # String! 识别到了字符串！
  elif character == '"':
    global stringState
    while index < len(code):
      codeValue = codeValue + character
      if stringState == 0:
        if character == '"':
          stringState = 1
      elif stringState == 1:
        if character == '\\':
          stringState = 3
        elif character == '"':
          stringState = 2
          break
      elif stringState == 2:
        break
      elif stringState == 3:
        if character in cEscSequence:
          stringState = 1
      character = code[index]
      index = index + 1

    if stringState == 2:
      wordType = 'string'
    else:
      print('Illegal string.')

  # Char! 识别到了字符！
  elif character == '\'':
    global charState
    while index < len(code):
      codeValue = codeValue + character
      if charState == 0:
        if character == '\'':
          charState = 1
      elif charState == 1:
        if character == '\'':
          charState = 2
          break
        elif character == '\\':
          charState = 3
      elif charState == 2:
        break
      elif charState == 3:
        if character in cEscSequence:
          charState = 1
      character = code[index]
      index = index + 1
    if charState == 2:
      wordType = 'character'
      charState = 0
    else:
      wordType = 'illegal char'
      charState = 0

  # # Operators!
  # elif character == '':

  # End of a line
  elif character == '\n':
    codeLine = codeLine + 1


def main():
  # Print usage if arguments are not legal
  if len(sys.argv) < 2:
    print('[Usage] ./scan.py <C source file path>')
    sys.exit(0)

  # Read file from file path taken from command line arguments
  filePath = sys.argv[1]
  with open(filePath, 'r', encoding='utf-8') as f:
    content = f.readlines()

  # Pre process C source file
  code = preProcess(content)
  print(code)
  while index < len(code):
    scanner(code)
    # Print identified word type and word itself
    if wordType != '':
      # if wordType == 'character':
      print('Line:', codeLine, wordType.upper() + ': ' + codeValue)


if __name__ == "__main__":
  main()
