import yaml
import sqlparse
from string import Template

def generate_user_input(workspace):
    #User input - Basic
    read_user_input= open(f"{workspace}\\config\\user_input.yml", 'r')
    user_input = yaml.safe_load(read_user_input)
    user_input = user_input['user_input']

    #User input - Override
    read_user_input_override= open(f"{workspace}\\config\\user_input_override.yml", 'r')
    user_input_override = yaml.safe_load(read_user_input_override)
    user_input_override = user_input_override['user_input']

    #Update user input with override
    #Update dictionary with other dictionary
    #Using loop
    for key in user_input:
        if key in user_input_override:
            user_input[key] = user_input_override[key]

    return user_input

def generate_sql_script(workspace, sql_path, model):
    #SQL variables - Default
    read_sql_variables=open(f"{workspace}\\config\\sql_variables.yml", 'r')
    sql_variables = yaml.safe_load(read_sql_variables)
    #SQL variables - Override
    read_sql_variables_override= open(f"{workspace}\\config\\sql_variables_override.yml", 'r')
    sql_variables_override = yaml.safe_load(read_sql_variables_override)

    for key in sql_variables:
        if key in sql_variables_override:
            sql_variables[key] = sql_variables_override[key]


    #Read file location 
    #Full Path required so it can be done in the Windows Scheduler double :\\ (workspace location approach)
    sql_file_path = f"{workspace}\\{sql_path}" 
    sql_script = open(sql_file_path,'r')
    script = sql_script.read()
    script = sqlparse.format(script, strip_comments=True).strip()
    try:
        script = Template(script).safe_substitute(sql_variables[f'{model}'])
    except:
        print('No templatized model aligned')
        
    return script