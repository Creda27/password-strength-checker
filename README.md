# Password Strength Checker

A beginner-friendly Python tool that checks how strong a password is and explains how to make it stronger. Built while learning cybersecurity fundamentals.

## Features
- Checks password length (minimum 12 characters)
- Checks for uppercase, lowercase, digits, and symbols
- Compares against a blocklist of common passwords
- Scores the password out of 5 and gives a verdict: Weak, Okay, or Strong
- Prints specific tips for what to add (e.g. "add number")
- Never prints the password back - by design, for security

## How to run
1. Clone this repository
2. Run: `python password_checker.py`
3. Type a password and read the feedback

## What I learned
- Python input, loops, and conditionals
- Checking character types with string methods
- Why normalizing input (lowercasing) matters before comparing
- Git and GitHub: cloning, committing, and pushing from VS Code

## Future improvements
- Hide the password while it's being typed (Python's `getpass`)
- Use a much larger real-world common-password list
- Catch variations of common passwords, not just exact matches
