from InquirerPy import inquirer
from rich import print
from prompt import Prompt
from utils.functions import getUserInput
from utils.functions import createReadmeFile


if __name__ == "__main__":
    # welcome message
    print("[bold dark_turquoise]WELCOME TO README.md FILE GENERATOR[/bold dark_turquoise]")
    print("[italic dark_red]Please enter the following information:[/italic dark_red]")
    
    # get user inputs
    title = getUserInput("Please enter title : ")
    description = getUserInput("Please enter description : ")
    installation = getUserInput("Please enter installation : ")
    usage = getUserInput("Please enter usage : ")
    author = getUserInput("Please enter author : ")
    contact = getUserInput("Please enter contact : ")
    license = inquirer.select(
        message="Please select a licence:",
        choices=[
            "No license",
            "Apache License 2.0",
            "GNU General Public License v3.0",
            "MIT License",
            "BSD 2-Clause Simplified License",
            "Boost Software License 1.0",
            "Eclipse Public License 2.0",
            "Mozilla Public License 2.0",
            "Creative Commons Zero v1.0 Universal",
        ],
    ).execute()
    
    print(f"[bold green]README.md file created successfully ![/bold green]")
    
    # create Prompt object
    prompt = Prompt(title,description,installation,usage,author,contact,license)
    readme_file= createReadmeFile(prompt)
    
    # write to README.md file
    with open("output/README.md", "w") as f:
        f.write(readme_file)


