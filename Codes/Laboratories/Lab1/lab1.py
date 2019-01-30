# Author: Israel Castro Gonzalez A01228769
# Compilers - Victor Rodriguez
# ENE-MAY 2019
# Laboratory 1


index_of_foo = -1
index_of_main = -1
temp_index = 0

size_of_foo = 0
size_of_main = 0

foo_method_dictonary = {}
main_method_dictonary = {}

print("\n") 

with open('log.txt', mode='r') as my_file:
    file_content = my_file.readlines()
    if "00401410 <_foo>:\n" in file_content:
        print("Found FOO! in the address: 00401410")
        index_of_foo = file_content.index("00401410 <_foo>:\n")
    
    if "00401438 <_main>:\n" in file_content:
        print("Found MAIN! in the address: 00401438")
        index_of_main = file_content.index("00401438 <_main>:\n")

current_index = index_of_foo
while (file_content[current_index] != "\n"):
    current_index = current_index + 1
    instruction_strings = file_content[current_index].split()
    if "push" in instruction_strings:
        if "push" in foo_method_dictonary:
            foo_method_dictonary["push"] += 1
        else:
            foo_method_dictonary["push"] = 1

    if "mov" in instruction_strings:
        if "mov" in foo_method_dictonary:
            foo_method_dictonary["mov"] += 1
        else:
            foo_method_dictonary["mov"] = 1

    if "sub" in instruction_strings:
        if "sub" in foo_method_dictonary:
            foo_method_dictonary["sub"] += 1
        else:
            foo_method_dictonary["sub"] = 1

    if "fld1" in instruction_strings:
        if "fld1" in foo_method_dictonary:
            foo_method_dictonary["fld1"] += 1
        else:
            foo_method_dictonary["fld1"] = 1

    if "fstps" in instruction_strings:
        if "fstps" in foo_method_dictonary:
            foo_method_dictonary["fstps"] += 1
        else:
            foo_method_dictonary["fstps"] = 1

    if "flds" in instruction_strings:
        if "flds" in foo_method_dictonary:
            foo_method_dictonary["flds"] += 1
        else:
            foo_method_dictonary["flds"] = 1

    if "fmulp" in instruction_strings:
        if "fmulp" in foo_method_dictonary:
            foo_method_dictonary["fmulp"] += 1
        else:
            foo_method_dictonary["fmulp"] = 1

    if "faddp" in instruction_strings:
        if "faddp" in foo_method_dictonary:
            foo_method_dictonary["faddp"] += 1
        else:
            foo_method_dictonary["faddp"] = 1

    if "leave" in instruction_strings:
        if "leave" in foo_method_dictonary:
            foo_method_dictonary["leave"] += 1
        else:
            foo_method_dictonary["leave"] = 1

    if "ret" in instruction_strings:
        if "ret" in foo_method_dictonary:
            foo_method_dictonary["ret"] += 1
        else:
            foo_method_dictonary["ret"] = 1

current_index = index_of_main
while (file_content[current_index] != "\n"):
    current_index = current_index + 1
    instruction_strings = file_content[current_index].split()
    if "push" in instruction_strings:
        if "push" in main_method_dictonary:
            main_method_dictonary["push"] += 1
        else:
            main_method_dictonary["push"] = 1

    if "mov" in instruction_strings:
        if "mov" in main_method_dictonary:
            main_method_dictonary["mov"] += 1
        else:
            main_method_dictonary["mov"] = 1

    if "sub" in instruction_strings:
        if "sub" in main_method_dictonary:
            main_method_dictonary["sub"] += 1
        else:
            main_method_dictonary["sub"] = 1

    if "and" in instruction_strings:
        if "and" in main_method_dictonary:
            main_method_dictonary["and"] += 1
        else:
            main_method_dictonary["and"] = 1

    if "call" in instruction_strings:
        if "call" in main_method_dictonary:
            main_method_dictonary["call"] += 1
        else:
            main_method_dictonary["call"] = 1

    if "movl" in instruction_strings:
        if "movl" in main_method_dictonary:
            main_method_dictonary["movl"] += 1
        else:
            main_method_dictonary["movl"] = 1

    if "fstps" in instruction_strings:
        if "fstps" in main_method_dictonary:
            main_method_dictonary["fstps"] += 1
        else:
            main_method_dictonary["fstps"] = 1

    if "flds" in instruction_strings:
        if "flds" in main_method_dictonary:
            main_method_dictonary["flds"] += 1
        else:
            main_method_dictonary["flds"] = 1

    if "leave" in instruction_strings:
        if "leave" in main_method_dictonary:
            main_method_dictonary["leave"] += 1
        else:
            main_method_dictonary["leave"] = 1

    if "ret" in instruction_strings:
        if "ret" in main_method_dictonary:
            main_method_dictonary["ret"] += 1
        else:
            main_method_dictonary["ret"] = 1
    
    if "fstpl" in instruction_strings:
        if "fstpl" in main_method_dictonary:
            main_method_dictonary["fstpl"] += 1
        else:
            main_method_dictonary["fstpl"] = 1

    if "nop" in instruction_strings:
        if "nop" in main_method_dictonary:
            main_method_dictonary["nop"] += 1
        else:
            main_method_dictonary["nop"] = 1

    if "xchg" in instruction_strings:
        if "xchg" in main_method_dictonary:
            main_method_dictonary["xchg"] += 1
        else:
            main_method_dictonary["xchg"] = 1

print("You currently have: 2 functions")
print("This is the count of the instructions in the _foo function:")
print("The format in the list is the following\ninstruction : number_of_excecutions")
print(foo_method_dictonary)
print("\n")
print("and this is the count of the instructions in the _main function:")
print(main_method_dictonary)

#size_of_foo = current_index - index_of_foo



#print(index_of_foo)
#print(index_of_main)

    