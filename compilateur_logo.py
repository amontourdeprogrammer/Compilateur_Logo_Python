CONTENT = ''

def compile_logo(commands):
    global CONTENT
    CONTENT = ''
    html_commands = []
    for command in commands:
        manicured_command = seperate_brackets_from_content(command)
        print manicured_command
        deal_with_deepest_brackets(manicured_command)
        html_commands.append(CONTENT)
        CONTENT = ''
    return '\n'.join(html_commands)

def deal_with_deepest_brackets(command):
    global CONTENT
    item = find_deepest_brackets(command)
    print item
    print CONTENT
    if item == None :
        deal_with_functions(command)
        return CONTENT
    else :
        deal_with_functions(item[0]) #"av(20);"
        context = item[1]
        deepest_brackets_context_index = (context.index("CONTENT"))-2
        deepest_brackets_condition_index = (context.index("CONTENT"))-1
        times = context[deepest_brackets_condition_index]
        CONTENT = "for (int i = 0; i < "+ str(times)+"; i = i+1){\n"+ CONTENT +"\n}"
        context.pop(deepest_brackets_condition_index)
        context.pop(deepest_brackets_context_index)
        return deal_with_deepest_brackets(context)


def find_deepest_brackets(command):
    index_start = None
    index_end = None
    for i in range(len(command)) : 
        if "[" in command[i] :
            index_start = i
    for word in command[index_start:] :
        if "]" in word :
            index_end = command.index(word) +1
            break
    if index_start == None and index_end == None :
        return None
    elif index_start == None and index_end == None :
        raise SyntaxError("Bracket not open or not closed")
    else :
        inside_deepest_bracket = command[index_start+1:index_end-1]
        outside_deepest_bracket = command[:index_start] + ["CONTENT"] + command[index_end:]
        return [inside_deepest_bracket, outside_deepest_bracket]


#given a command, extract the commands
def deal_with_functions(command):
    global CONTENT
    html_commands = []
    known_functions_with_argument = ["av", "td", "tg"]
    known_functions_without_argument = ['origin']
    while len(command) >= 1 :
        function_in_list = command.pop(0)
        if function_in_list in known_functions_with_argument :
            html_commands.append ("{}({});".format(function_in_list, command.pop(0)))
        elif function_in_list in known_functions_without_argument :
            html_commands.append ("{}();".format(function_in_list))
        elif function_in_list == "CONTENT" :
            html_commands.append(CONTENT)
        else :
            raise NameError("{} is not defined".format(function_in_list))
    if CONTENT == '' :
        CONTENT = '\n'.join(html_commands)
    else :
        CONTENT = CONTENT +'\n'+ '\n'.join(html_commands)
    return '\n'.join(html_commands)

def seperate_brackets_from_content(command):
    count = 0
    command_without_bracket_attached = []
    for i in range(len(command)) :
        item_reviewed = command[i]
        if ("[" not in item_reviewed ) and ("]" not in item_reviewed) :
            command_without_bracket_attached.append(item_reviewed)
        else :
            while "[" in item_reviewed :
                item_reviewed = ''.join(list(item_reviewed)[1:])
                command_without_bracket_attached.append("[")
                if "[" in item_reviewed :
                    pass
                else :
                    command_without_bracket_attached.append(item_reviewed)
            while "]" in item_reviewed :
                item_reviewed = ''.join(list(item_reviewed)[:-1])
                count += 1
                if "]" in item_reviewed :
                    pass
                else :
                    command_without_bracket_attached.append(item_reviewed)
                    for j in range(count):
                        command_without_bracket_attached.append("]")
                        count = 0
    return command_without_bracket_attached


#print compile_logo([["av","50"], ["td","90"]]) == "av(50);\ntd(90);"
#print compile_logo([["av","50"], ["td","90"],["repete", "12", "[origin", "td", "30]"], ["av","50"], ["td","90"]])== "av(50);\ntd(90);\nfor (int i = 0; i < 12; i = i+1){\norigin();\ntd(30);\n}\nav(50);\ntd(90);"
print compile_logo([["av","50"], ["td","90"],["repete", "12", "[origin", "td", "30]"], ["av","50"], ["td","90"]])
