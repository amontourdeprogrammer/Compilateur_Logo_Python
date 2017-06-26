def compile_logo(commands):
    html_commands = []
    for command in commands :
        html_commands.append ("{}({});".format(command[0], command[1]))
    return '\n'.join(html_commands)
