"""CP=1404 progarmming languages exercise"""
from Prac_07.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

language_list = [ruby, python, visual_basic]

print("The dynamically typed languages are:")
for language in language_list:
    if language.is_dynamic():
        print(language.name)
