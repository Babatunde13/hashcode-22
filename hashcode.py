# inputs
# 1. contributors list
# project list with skill requirements
# contributors can improve skills
# contributors can mentor others

import json
import os
from typing import Any, Dict, List

def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        return lines

def get_contributors_and_projects(lines: List[str]):
    contributors = {}
    projects = {}
    [contributor_count, project_count] = map(int, lines[0].replace('\n', '').split(' '))
    lines = list(map(lambda x: x.replace('\n', ''), lines[1:]))
    count = 0
    while contributor_count > len(contributors.keys()):
        [name, skill_count] = lines[count].split(' ')
        skill_count = int(skill_count)
        count += 1
        skills = {}
        for i in range(skill_count):
            [skill, level] = lines[count + i].split(' ')
            skills[skill] = int(level)
        count += skill_count
        contributors[name] = {
            'skills': skills,
            'name': name,
            'level': skill_count
        }
    
    while project_count > len(projects.keys()):
        [name, days_to_complete, score, best_before, num_of_roles] = lines[count].split(' ')
        num_of_roles = int(num_of_roles)
        count += 1
        skills = {}
        for i in range(num_of_roles):
            [skill, level] = lines[count + i].split(' ')
            skills[skill] = int(level)
        count += num_of_roles
        projects[name] = {
            'skills': skills,
            'name': name,
            'days to complete': days_to_complete,
            'best before': best_before,
            'score': score,
            'number of roles': num_of_roles
        }
    return [contributors, projects]

def map_project_to_contributor(projects, contributors):
    answer = f'{len(projects)}\n'
    for project in projects.values():
        skills = project['skills']
        answer += project['name'] + '\n'
        for [skill, level] in skills.items():
            for contributor in contributors.values():
                if skill in contributor['skills'].keys():
                    if contributor['skills'][skill] >= level:
                        answer += contributor['name'] + ' '
                    elif level - contributor['skills'][skill] == 1:
                        answer += contributor['name'] + ' '
        answer += '\n'

    return answer

def generate_output():
    for file in os.listdir('./inputfiles'):
        print(file)
        if file.endswith(".in.txt"):
            print(f'Generating output for {file}')
            lines = read_file(f'./inputfiles/{file}')
            file_name = file.replace('.in.txt', '.out.txt')

            [contributors, projects] = get_contributors_and_projects(lines)
            resp = map_project_to_contributor(projects, contributors)
            if not os.path.exists('./outputfiles'):
                os.makedirs('./outputfiles')
            with open(f'./outputfiles/{file_name}', 'w') as f:
                f.write(resp)
            print(f'Output generated for {file}')

generate_output()
