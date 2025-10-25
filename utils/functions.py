def getUserInput(prompt_message):
    while True:
      prompt = input(prompt_message)
      if(checkEmptyInput(prompt)):
          return prompt
      else:
          print("Input cannot be empty. Please try again.")
   
def checkEmptyInput(prompt):
      if(prompt.strip() != ''):
         return True
      return False