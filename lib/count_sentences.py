#!/usr/bin/env python3

class MyString:
  def __init__(self, value = ''):
    self.value = value

  def get_value(self):
    return self._value
  
  def set_value(self, value):
    if type(value) is str:
      self._value = value
    else:
      print("The value must be a string.")
  
  value = property(get_value, set_value)

  def is_sentence(self):
    if self._value.endswith('.'):
      return True
    return False

  def is_question(self):
    if self._value.endswith('?'):
      return True
    return False

  def is_exclamation(self):
    if self._value.endswith('!'):
      return True
    return False

  def count_sentences(self):
    sentence_ends = ('.', '!', '?')
    count = 0
    for word in self._value.split():
      if word[-1] in sentence_ends:
        count += 1
    return count
