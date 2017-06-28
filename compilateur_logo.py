def compile_logo(commands):
    html_commands = []
    for command in commands:
        html_commands.append(switch_board(command))
    return '\n'.join(html_commands)

#given a command, extract the commands inside the brackets
def deal_with_brackets(command):
    found_opening_bracket = False
    found_closing_bracket = False
    after_commands = []
    while found_opening_bracket == False :
        item_reviewed = command.pop(0)
        if "[" in item_reviewed :
            no_bracket = ''.join(list(item_reviewed)[1:])
            command.insert(0,no_bracket)
            found_opening_bracket = True
    while found_closing_bracket == False :
        item_reviewed = command.pop(-1)
        if "]" in item_reviewed :
            no_bracket = ''.join(list(item_reviewed)[:-1])
            command.append(no_bracket)
            found_closing_bracket = True
        else :
            after_commands.insert(0,item_reviewed)
    result = [command,after_commands]
    print 'deqling zith braket result'
    print result
    return result

#given a command, extract the commands
def deal_with_functions(command):
    html_commands = []
    known_functions_with_argument = ["av", "td", "tg"]
    known_functions_without_argument = ['origin']
    while len(command) >= 1 :
        function_in_list = command.pop(0)
        if function_in_list in known_functions_with_argument :
            html_commands.append ("{}({});".format(function_in_list, command.pop(0)))
        elif function_in_list in known_functions_without_argument :
            html_commands.append ("{}();".format(function_in_list))
        else :
            raise NameError("{} is not defined".format(function_in_list))
    return '\n'.join(html_commands)

#print compile_logo([["av","50"]])

def switch_board(command):
  
    if command[0] == "repete":
        times = command[1];
        reapeated_commands = switch_board(deal_with_brackets(command)[0])
        after_commands =''
        if len(after_commands) == 0 :
            after_commands =''
        else :
            after_commands = switch_board(deal_with_brackets(command)[1])
         
        print("for (int i = 0; i < "+times+"; i = i+1){\n"+ reapeated_commands +"\n}"+after_commands)
        return "for (int i = 0; i < "+times+"; i = i+1){\n"+ reapeated_commands +"\n}"+after_commands

    else :
        return deal_with_functions(command)
#repete 12 [repete 4 [av 20] td 30]
print compile_logo([["repete", "12", "[repete", "4", "[av", "20]", "td", "30]"]])
print deal_with_brackets(["repete", "12", "[repete", "4", "[av", "20]", "td", "30]"])