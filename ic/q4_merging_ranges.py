# Your company built an in-house calendar tool called HiCal. 
# You want to add a feature to see the times in a day when everyone is available.

# For example, given:   [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
# Return:   [(0, 1), (3, 8), (9, 12)]

# Do not assume meetings are in order.

# Solution
# First, sort the input list in order based on start time of each meeting.
# This way, any meetings that can be merged are right next to each other

# Then we walk through our sorted meetings from left to right. At each step, either:
# 1. We can merge the current meeting with the previous one
# 2. We can't merge the current meeting with the previous one, so we know 
#    the previous meeting can't be merged with any future meetings. Put it inside
#    of merged_meetings.

# Runtime: O(n log n), O(n) space
def merge_ranges(meetings):

  # Sort by the start times
  sorted_meetings = sorted(meetings)

  # Initialize merged_meetings with the earliest meeting
  merged_meetings = [sorted_meetings[0]]

  # Iterate over the rest of the meetings
  for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
    last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

    # If the current and last meetings overlap, use the latest end time
    if current_meeting_start <= last_merged_meeting_end:
      # Store the last meeting of the day
      merged_meetings[-1] = (last_merged_meeting_start, max(last_merged_meeting_end, current_meeting_end))

    # If no overlap between last meeting and current meeting:
    else:
      merged_meetings.append((current_meeting_start, current_meeting_end))

  return sorted_meetings


meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
print merge_ranges(meetings)