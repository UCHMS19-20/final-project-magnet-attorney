# Setting Up Your Programming Environment at Home

## Software

You'll need a text editor to write your code in, Python to test your code, and Git for version control. You will also likely want GitHub Desktop to use the graphical interface for Git. If you already have preferences regarding the programs you use for this, go ahead and use what you like, but if you want to match your home environment to what we use at the school, you should use the following:

| Program        | Link                                                 | Notes                                        |
|----------------|------------------------------------------------------|----------------------------------------------|
| Python         | https://www.python.org/downloads/release/python-381/ | Make sure you use Python 3 (currently 3.8.1) |
| VS Code        | https://code.visualstudio.com/download               |                                              |
| Git            | https://git-scm.com/                                 |                                              |
| GitHub Desktop | https://desktop.github.com/                          |                                              |

## Setup

Install all the software. For Python on Windows, you may be asked if you want to add it to path. Choose yes, or you'll have to add it manually. OS X and most Linux installations will already have Python installed, but it will almost certainly be Python 2. Make sure you install Python 3, as it works a little differently from Python 2.

To use VS Code with Python, install the Python extension from Microsoft. Use <kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>p</kbd> to open the command palette and choose the "Install extensions" command. You can use search to find the extension. Install it, and reload VS code if needed.

## Git

Note: you'll need to sign in to authorize Git to access your GitHub account. The easiest way to do that, even if you primarily want to use the command line, is to sign in with GitHub Desktop. You don't have to do this if you're using the command line, though - you can also sign in at the command line (just be aware that you won't be able to see anything when you type in your password).

1. Clone your repository. Either use the graphcial interface through GitHub Desktop, or use the `git clone` command at the command line
2. Remember to always pull (if using the command line) or sync (if using the graphical interface) every time you resume work at a particular computer, and to always push when you're done. This will make sure you're always using the most up-to-date version and that you don't end up with merge conflicts.
