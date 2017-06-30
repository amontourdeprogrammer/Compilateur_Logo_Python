class Commande_Logo :
    def __init__(self, logo_command):
        self.logo_command = self.seperate_brackets_from_content(logo_command)
        self.deepest_bracket = None
        self.context = self.logo_command
        self.processing_command =  ''

    def seperate_brackets_from_content(self, command):
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
        #print command_without_bracket_attached
        return command_without_bracket_attached

    def find_deepest_brackets(self):
        command = self.context
        index_start = None
        index_end = None
        for i in range(len(command)) : 
            if "[" in command[i] :
                index_start = i
        closing_bracket_list = command[index_start:]   
        for j in range(len(closing_bracket_list)) :
            if "]" in closing_bracket_list[j] :
                index_end = index_start+j +1
                break

        if index_start == None and index_end == None :
            self.deepest_bracket = False
            return False
        elif index_start == None or index_end == None :
            raise SyntaxError("Bracket not open or not closed")
        else :
            self.deepest_bracket = command[index_start+1:index_end-1]
            self.context = command[:index_start] + ["CONTENT"] + command[index_end:]
            return True

    def deal_with_complex_expression(self):
        bracket_are_in_context = self.find_deepest_brackets()

        if bracket_are_in_context == False :
            last_call = self.deal_with_braketless_expressions(self.context)
            if last_call != None :
                self.processing_command = last_call
            return self.processing_command
        elif bracket_are_in_context == True :
            self.processing_command += self.deal_with_braketless_expressions(self.deepest_bracket) #"av(20);"
            deepest_brackets_context_index = (self.context.index("CONTENT"))-2
            deepest_brackets_condition_index = (self.context.index("CONTENT"))-1
            times = self.context[deepest_brackets_condition_index]
            self.processing_command = "for (int i = 0; i < "+ str(times)+"; i = i+1){\n"+ self.processing_command +"\n}"
            self.context.pop(deepest_brackets_condition_index)
            self.context.pop(deepest_brackets_context_index)
            return self.deal_with_complex_expression()
        else :
            raise TypeError("self.deepest_bracket can't be None at this stage")

    def deal_with_braketless_expressions(self, command):
        if command == ['CONTENT'] :
            return None
        else :
            html_commands = []
            known_functions_with_argument = ["av", "td", "tg"]
            known_functions_without_argument = ['origine']
            while len(command) >= 1 :
                function_in_list = command.pop(0)
                if function_in_list in known_functions_with_argument :
                    html_commands.append ("{}({});".format(function_in_list, command.pop(0)))
                elif function_in_list in known_functions_without_argument :
                    html_commands.append ("{}();".format(function_in_list))
                elif function_in_list == "CONTENT" :
                    pass
                else :
                    raise NameError("{} is not defined".format(function_in_list))
            if self.processing_command == '' :
                return '\n'.join(html_commands)
            else :
                return '\n' + '\n'.join(html_commands)

braketless_logo_command = ["av","50"]
several_braketless_logo_command = ["av","50", "td","90", "origine"]
braketmedium_logo_command = ["repete", "12", "[origine", "td", "30", "td", "50]"]
braketfull_logo_command = ["repete", "12", "[repete", "4", "[av", "20]", "td", "30]"]
complex_braketfull_logo_command = ["repete", "12", "[origine","repete", "4", "[av", "20]","repete", "6", "[av", "20]", "td", "30]"]

#a = Commande_Logo(complex_braketfull_logo_command)
#print a.deal_with_complex_expression()

def compile_logo(commands):
    html_commands = []
    for command in commands:
        new_command = Commande_Logo(command)
        html_commands.append(new_command.deal_with_complex_expression())
    return '\n'.join(html_commands)