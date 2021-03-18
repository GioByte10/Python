prompt = "Add the hidden word: "
inputStr = input(prompt).lower()
print('\033[1A' + prompt + '\033[K')


def clear_input(self):

    if self.has_input_:
      self.has_input_ = 0
      if self.input_ is not None: self.input_.Clear()

