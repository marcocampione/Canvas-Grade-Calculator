import sys
from canvasapi import Canvas,exceptions
from tqdm import tqdm
import re 
from  hints import HINTS


# Since you have to submit all the flags to pass the course, we can just check if you have submitted all the flags 
# and with this check we can say that the user has passed or not the course. The program will exit if you have not submitted even one of the flags.
# and will return the flag not submitted.
# The assignment id for the flags are from 259162 to 259179 that's why I'm iterating over this range. 
# This function is also generating a dictionary with all the information needed later for the grade calculation
def check_if_passed(course, user):
    info_dict = {}

    for i in tqdm(range(259162, 259180), desc="Checking assignments"):
        assignment = course.get_assignment(i)
        assignment_info ={
            "id": assignment.id,
            "flag_name": (assignment.name).split()[2],
            "max_points": assignment.points_possible,
        }
        submission = assignment.get_submission(user.id)
        submission_info = {
            "final_points": submission.score,
            "state": submission.workflow_state,
        }   
        hints_info ={
            "hints_points": HINTS[i]['hints']
        }
        
        assignment_info['submissions'] = submission_info
        assignment_info['hints'] = hints_info
        info_dict[assignment.id] = assignment_info

        if submission.workflow_state != 'graded':
            sys.exit(f"You have not submitted the flag {(assignment.name).split()[2]}, so you have not passed the course. Retry next year!")
    
    print("You submitted all the flags, so you can pass the course if you have enough points")
    return info_dict

def user_check_enrollment(canvas):
    try:
        course = canvas.get_course(41678)
    except exceptions.Forbidden:
        print("You are not enrolled in the course.")
        return
    except exceptions.InvalidAccessToken:
        print("Invalid access token.")
        return 
    return course

def points_to_letter_grade(points):
    if 0 <= points <= 180:
        if points >= 162:
            return 'A'
        elif points >= 126:
            return 'B'
        elif points >= 90:
            return 'C'
        elif points >= 54:
            return 'D'
        elif points >= 36:
            return 'E'
        else:
            return 'F'
    else:
        return 'Invalid points'

def max_points_for_assignment(dict_assignments):
    max_points = 0
    for i in range(259162, 259180):
        max_points += dict_assignments[i]['max_points']
    return max_points

def is_string_in_dictionary(my_string, my_dict):
    for key, value in my_dict.items():
        if 'flag_name' in value and value['flag_name'] == my_string:
            return True
    return False

def grade_after_hints(dict_assignments,user):
    num_hint_asked = 0
    for group in user.get_groups():
        match = re.match(r'^Flag ([0-9a-fA-F]{6}) Hint (\d+$)', group.name)
        if match:
            match_flag_name = match.group(1)
            hint_number = int(match.group(2))

            for key, value in dict_assignments.items():
                if 'flag_name' in value and value['flag_name'] == match_flag_name:
                    num_hint_asked += 1
                    flag = dict_assignments[key]
                    hint_value = flag['hints']['hints_points'][hint_number - 1]
                    dict_assignments[key]['max_points'] = max(0,dict_assignments[key]['max_points'] - hint_value)
    return num_hint_asked

def CalculateGrade(canvas): 
    #Check if the user is enrolled in the course and is using the correct token
    course = user_check_enrollment(canvas)

    user = canvas.get_current_user()
    print(f'Student name: {user}')

    dict_assignments={}

    # Check if the user has submitted all the flags, and generate a dictionary with all the information
    # needed to do all the calculation later  
    dict_assignments = check_if_passed(course,user)
    
    # Calculate how many points you can get at max for the course
    max_points = max_points_for_assignment(dict_assignments)

    # Calculate the grade after the hints points deduction return the number of hints asked
    hint_asked = grade_after_hints(dict_assignments,user)

    # Calculate the final grade
    final_grade = 0
    for i in tqdm(range(259162, 259180), desc="Calculating final grade"):
        final_grade += dict_assignments[i]['max_points']
    
    # Check if the final grade is above 20% of the total points that are needed to pass the course 
    if final_grade > 0.2 * max_points:
        print('Congratulation!! Your score is above the 20% threshold so you passed the course!')
        print(f'You got a total of {final_grade} / {max_points} points, you asked {hint_asked} hints to complete the course, your final grade is {points_to_letter_grade(final_grade)}.')
    else:
        print('Your score is below the 20% threshold so unfortunately you have not passed the course.')
        print(f"You got a total of {final_grade} / {max_points} points, you asked {hint_asked} hints, your final grade is {points_to_letter_grade(final_grade)}.")
    
    




