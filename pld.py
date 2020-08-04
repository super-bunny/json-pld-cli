import pld_messages


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
