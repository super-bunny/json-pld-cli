def total_estimated_duration(pld_content) -> int:
    total_duration = 0
    if 'deliverables' in pld_content:
        for deliverables in pld_content['deliverables']:
            if 'subsets' in deliverables:
                for subset in deliverables['subsets']:
                    if 'userStories' in subset:
                        for user_story in subset['userStories']:
                            total_duration += user_story['estimatedDuration']
    return total_duration
