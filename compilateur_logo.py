def compile_logo(commands):
    html_commands = []
    for command in commands :
    	if command[0] == "repete":
    		times = command[1];
    		reapeated_commands = (deal_with_functions(deal_with_brackets(command)))
    		result = "for (int i = 0; i < "+times+"; i = i+1){\n"+ reapeated_commands +"\n}"
    		html_commands.append(result)
    	else :
       		html_commands.append ("{}({});".format(command[0], command[1]))
    return '\n'.join(html_commands)

#given a command, extract the commands inside the brackets
def deal_with_brackets(command):
	for i in range(len(command)):
		if "[" in command[i] :
			start_index = i
			bracket = command.pop(i)
			no_bracket = ''.join(list(bracket)[1:])
			command.insert(i,no_bracket)
		elif "]" in command[i] :
			end_index = i +1
			bracket = command.pop(i)
			no_bracket = ''.join(list(bracket)[:-1])
			command.insert(i,no_bracket)
	bracketless_command = command[start_index:end_index]
	return bracketless_command

#given a command, extract the commands
def deal_with_functions(command):
	html_commands = []
	known_functions_with_argument = ["av", "td"]
	known_functions_without_argument = ['trait']
	while len(command) >= 1 :
		function_in_list = command.pop(0)
		if function_in_list in known_functions_with_argument :
			html_commands.append ("{}({});".format(function_in_list, command.pop(0)))
		elif function_in_list in known_functions_without_argument : 
			html_commands.append ("{}();".format(function_in_list))
		else :
			raise NameError("{} is not defined".format(command[i]))
	return '\n'.join(html_commands)
