def is_ascii(word):
  try:
    word.encode ('ascii')
    return True
  except UnicodeEncodeError:
      return False