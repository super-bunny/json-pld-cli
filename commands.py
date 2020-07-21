import pld
import pld_messages


def duration_cmd(pld_content, verbose=False):
    estimated_duration = pld.total_estimated_work_duration(pld_content, verbose)
    print(f'Total estimated work duration : {pld_messages.estimated_duration_message(estimated_duration)}')
