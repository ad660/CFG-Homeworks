"""A] Simulate clicking around the CFG Website. Keep track of the URL changes and
print the current URL after each move.

● You will need to display the options for each link, and include an option for
‘Back’ if not on the Base URL.
● You do not need to worry about error handling
● You are recommended to keep the simulation going within a while True loop
so the logic keeps looping until an exit is forced.

You only need to consider the following URLs for your solution:
1. Base URL: https://codefirstgirls.com/
2. Category URLs: /courses ,/opportunities/
3. Sub-category URLs: /courses/cfgdegree/ , /opportunities/ambassadors/"""

sub_url = {
    '/': ['Courses', 'Opportunities'],
    '/opportunities': ['Ambassadors', 'Back'],
    '/opportunities/ambassadors': ['Back'],
    '/courses': ['CFGDegree', 'Back'],
    '/courses/cfgdegree': ['back']}

base_url = 'https://codefirstgirls.com'
where = 'Where are you clicking?'

def clickAround():
    while sub_url:
        current_url = '/'
        if current_url == '/':
            q1 = input(f'You are currently on {base_url} \n{where} \n{sub_url.get(current_url)} \n')
            first_value, second_value = list(sub_url.items())[0][1]  # 0 = courses 1 = opportunities
            # print(first_value, second_value)
            if q1 == first_value:
                current_url = '/courses'
                course_keys = list(sub_url.items())[3]
                k, v = course_keys
                q2 = input(f'You are currently on {base_url}{current_url} \n{where} \n{sub_url.get(current_url)} \n')
                if q2 == v[0]:
                    current_url = current_url + '/cfgdegree'
                    q3 = input(f'You are currently on {base_url}{current_url} \n{where} \n{sub_url.get(current_url)} \n')
                    if q3 == 'Back':
                        current_url = '/'.join(current_url.split('/')[:-1])
                        q6 = input(
                            f'You are currently on {base_url}{current_url} \n{where} \n{sub_url.get(current_url)} \n')
                        continue
            if q1 == second_value:  # Opportunities
                current_url = '/opportunities'
                q4 = input(f'You are currently on {base_url}{current_url} \n{where} \n{sub_url.get(current_url)} \n')
                course_keys = list(sub_url.items())[1]
                k, v = course_keys
                if q4 == v[0]:
                    current_url = current_url + '/ambassadors'
                    q5 = input(f'You are currently on {base_url}{current_url} \n{where} \n{sub_url.get(current_url)} \n')
                    if q5 == 'Back':
                        current_url = '/'.join(current_url.split('/')[:-1])
                        q6 = input(f'You are currently on {base_url}{current_url} \n{where} \n{sub_url.get(current_url)} \n')
                        continue

clickAround()


"""B] What is the time and space complexity of your solution? If you are making any
assumptions, list them.

Add your answer to this as a comment above or below your solution to Part A

The Time complexity for this answer I believe O(n) because it is dependent on (n) which 
is the number of times the while loop will run. my split and join elements are within nested
loops so should not have a great impact on the time complexity. 
The space complexity is considered O(1) or linear as the variables and data structures 
needed remain constant and they aren't predicted to grow very high due to the expected inputs 
being low"""

