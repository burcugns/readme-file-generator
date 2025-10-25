def checkEmptyInput(prompt_message):
    while True:
      prompt = input(prompt_message)
      if(prompt != ''):
         return prompt
   