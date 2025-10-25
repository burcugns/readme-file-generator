#create README file function
 
def createReadmeFile(prompt):
    return f"""
  
# {prompt.title.capitalize()}


{prompt.description.capitalize()}


## Installation
 ```bash
{prompt.installation}
```

## Usage
```python
{prompt.usage}
```

## License
{prompt.license}


## Author
{prompt.author.capitalize()}

## Contact
{prompt.contact}

  """

# get user input function
def getUserInput(prompt_message):
    while True:
      prompt = input(prompt_message)
      if(checkEmptyInput(prompt)):
          return prompt
      else:
          print("Input cannot be empty. Please try again.")

# check empty input function
def checkEmptyInput(prompt):
      if(prompt.strip() != ''):
         return True
      return False