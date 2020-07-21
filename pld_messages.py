def estimated_duration_message(man_day_duration, hours_in_man_day=8):
    return f'{man_day_duration} man-day ({str(man_day_duration * hours_in_man_day).zfill(2)}h)'
