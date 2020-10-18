import datetime
import json
from functools import reduce

import pld_messages


def init_pld(file_name: str) -> None:
    pld = {
        "$schema": "https://raw.githubusercontent.com/super-bunny/pld-json-schema/master/schemas/pld.json",
        "config": {
            "dateFormat": "dd/mm/yy"
        },
        "title": "Project Log Document",
        "subTitle": "",
        "description": "PLD document",
        "authors": ["you"],
        "versions": [{
            "version": "1.0.0",
            "date": f"{datetime.datetime.now():%d/%m/%Y}",
            "author": ["you"],
            "sections": "All",
            "comment": "First version"
        }],
        "deliverables": [{
            "type": "deliverable",
            "name": "PLD (example)",
            "subsets": [{
                "type": "subset",
                "name": "PLD first version (example)",
                "userStories": [{
                    "type": "userStory",
                    "name": "Init PLD (example)",
                    "description": "Create PLD from scratch",
                    "user": "Project members",
                    "action": "Follow project progression with a document",
                    "definitionOfDone": ["PLD document"],
                    "assignments": ["You"],
                    "estimatedDuration": 1,
                    "status": "To do"
                }]
            }]
        }]
    }
    f = open(file_name, 'w')
    json.dump(pld, f, indent=2)
    f.close()


def total_estimated_work_duration(pld_content, verbose_print=False) -> int:
    total_duration = 0
    if 'deliverables' in pld_content:
        for deliverables in pld_content['deliverables']:
            if 'subsets' in deliverables:
                for subset in deliverables['subsets']:
                    if 'userStories' in subset:
                        for user_story in subset['userStories']:
                            if verbose_print:
                                print(f'{pld_messages.estimated_duration_message(user_story["estimatedDuration"])} '
                                      f'{user_story["name"]}')
                            total_duration += user_story['estimatedDuration']
    return total_duration


def get_distribution(pld_content):
    distribution = {}
    if 'deliverables' in pld_content:
        for deliverables in pld_content['deliverables']:
            if 'subsets' in deliverables:
                for subset in deliverables['subsets']:
                    if 'userStories' in subset:
                        for user_story in subset['userStories']:
                            assignments = user_story['assignments']
                            for user in assignments:
                                if distribution.get(user):
                                    distribution[user] += user_story['estimatedDuration'] / len(assignments)
                                else:
                                    distribution[user] = user_story['estimatedDuration'] / len(assignments)
    return distribution


def get_user_stories_by_user(pld_content, user):
    user_stories = []
    if 'deliverables' in pld_content:
        for deliverables in pld_content['deliverables']:
            if 'subsets' in deliverables:
                for subset in deliverables['subsets']:
                    if 'userStories' in subset:
                        for user_story in subset['userStories']:
                            assignments = map(str.lower, user_story['assignments'])
                            if user in assignments:
                                user_stories.append(user_story)
    return user_stories


def compare_version(a, b):
    a_arr = a["version"].split('.')
    b_arr = b["version"].split('.')

    a_arr = list(map(lambda x: int(x), a_arr))
    b_arr = list(map(lambda x: int(x), b_arr))
    if a_arr[0] != b_arr[0]:
        return a if a_arr[0] > b_arr[0] else b
    if a_arr[1] != b_arr[1]:
        return a if a_arr[1] > b_arr[1] else b
    if a_arr[2] != b_arr[2]:
        return a if a_arr[2] > b_arr[2] else b


def get_last_version(pld_content):
    if 'versions' in pld_content:
        return reduce(lambda a, b: compare_version(a, b), pld_content['versions'])
    return None
