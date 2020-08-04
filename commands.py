import pprint

import pld
import pld_messages


def duration_cmd(pld_content, verbose=False):
    estimated_duration = pld.total_estimated_work_duration(pld_content, verbose)
    print(f'Total estimated work duration : {pld_messages.estimated_duration_message(estimated_duration)}')


def distribution_cmd(pld_content):
    distribution = pld.get_distribution(pld_content)
    print(distribution)


def assignees_cmd(pld_content, user=None):
    assignees = pld.get_user_stories_by_user(pld_content, user)
    pprint.pprint(assignees, width=120, sort_dicts=False, compact=False)
    print()
    print(f'{len(assignees)} user stories found for "{user}" user')
