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
