import json
import subprocess

import click
from bash import bash


bash_success_code = 0


def run_and_return_output(command, command_for_print=None, print_command=False, confirm_prompt=False, print_output=False):

    if command_for_print:
        print('\n> Running command:\n')
        print(command_for_print + '\n')

    if print_command:
        print('\n> Running command:\n')
        print(command + '\n')

    if confirm_prompt:

        if confirm('>> Do you want to continue?'):
            pass
        else:
            print('## Command did not run.')
            return

    result = bash(command)
    output = result.value()

    if print_output:
        print('\n## Output:')
        print('\n' + 44 * '-')

        print('')
        print(output)

        print('\n' + 44 * '-')

    return output

run_command = run_and_return_output
run = run_and_return_output


def run_confirm_and_return_dict(command):

    json_output = run_and_return_output(
        command,
        print_command=True,
        confirm_prompt=True,
        print_output=True
    )

    return json.loads(json_output)


def run_and_return_json_object(command, print_command=False):

    json_output = run_and_return_output(command, print_command)

    json_object = json.loads(json_output)

    return json_object


def run_print_and_return_output(command):

    print('\n> Running command:\n')
    print(command)

    output = run_and_return_output(command)

    return output


def run_and_print(command,
                  confirm_prompt=False,
                  skip_confirm=True,
                  hide_echo=True,
                  decorate_command=False,
                  allow_error=False):

    if confirm_prompt or not skip_confirm:
        print('\n>> Confirm command:\n')
    else:
        print('\n> Running command:\n')

    custom_command = customize_command(command, hide_echo)

    if decorate_command:
        print('--------------------------------\n')

    print(custom_command, '\n')

    if decorate_command:
        print('--------------------------------\n')

    if confirm_prompt or not skip_confirm:
        if confirm('>> Do you want to continue?'):
            pass
        else:
            print('## Command did not run.')
            return

    print('\n## Output:')
    print('\n' + 44*'-')

    print('')
    return_code = subprocess.call(command, shell=True)

    print('\n' + 44 * '-')

    if not allow_error and return_code != bash_success_code:
        message = '\n[ERROR] Command failed with code:', return_code, '\n'
        raise ValueError(message)

    return return_code


def run_and_get_return_code(command):

    command_result = bash(command)

    return_code = command_result.code

    return return_code


def customize_command(command, hide_echo):

    if hide_echo:
        command_parts = command.split('\n')

        custom_command_parts = []
        for part in command_parts:
            if part.startswith('echo'):
                continue
            custom_command_parts.append(part)

        custom_command = '\n'.join(custom_command_parts)

    else:
        custom_command = command

    return custom_command


def run_and_confirm(command, allow_error=False):

    return_code = run_and_print(command, confirm_prompt=True, allow_error=allow_error)

    return return_code


def confirm(message, default=True):

    return click.confirm(message, default)
