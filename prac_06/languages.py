from prac_06.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

program_languages = [ruby, python, visual_basic]
print("The dynamically typed languages are:")
for language in program_languages:
    if language.is_dynamic():
        print(language.name)

print("\n",ruby)
