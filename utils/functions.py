from rich.console import Console
from rich import print

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
    console = Console()
    while True:
      prompt = console.input("[bright_yellow]"+prompt_message+"[/bright_yellow]" )
      if(checkEmptyInput(prompt)):
          return prompt
      else:
          print("[bold red]Input cannot be empty. Please try again.[/bold red]")

# check empty input function
def checkEmptyInput(prompt):
      if(prompt.strip() != ''):
         return True
      return False