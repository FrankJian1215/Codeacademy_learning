def pattern_search(text, pattern, replacement, case_sensitive=True):
    fixed_text = []
    num_skips = 0

    for index in range(len(text)):
        print(text[index])
        print('+++++')
        if num_skips > 0: # where it controls whether proceeding or not
            num_skips -= 1
            print(num_skips)
            print('=+=================')
            continue # Skips the remaining code in this iteration

        match_count = 0
        if case_sensitive:
            for char in range(len(pattern)):
                
                if pattern[char] == text[index + char]:
                    print(pattern[char])
                    print('***********')
                    match_count += 1
                else:
                    break
            if match_count == len(pattern):
                # The extend() method is used to add multiple elements to the end of a list.
                # where it adds replacement in the list
                fixed_text.extend(replacement) 
                num_skips = len(pattern) - 1
                print(num_skips)
                print('=++=================')
                continue # Skips the remaining code in this iteration
        else:
            for char in range(len(pattern)):
                if pattern[char].lower() == text[index + char].lower():
                    match_count += 1
                else:
                    break
            if match_count == len(pattern):
                fixed_text.extend(replacement)
                num_skips = len(pattern) - 1
                print(num_skips)
                continue # Skips the remaining code in this iteration

        fixed_text.append(text[index])

    fixed_text = ''.join(fixed_text)
    print(fixed_text)

friends_intro = "Pylhon is a wonderful Language that zzz is beloved for its ease zzz of use and simple syntacs. While zzz at some times the performance can be less than iDil, by properly zzz utilizing built-in libraries and other languuUuage features, pylhon's performance zzz can approach that of C."

pattern_search(friends_intro, "Language", "language")
# pattern_search(friends_intro, "pylhon", "Python", False)
# pattern_search(friends_intro, "idil", "ideal", False)
# print(pattern_search(friends_intro, "zzz ", ""))



def update_order(new_item, current_order=None):
  if current_order is None:
    current_order = []

  current_order.append(new_item)
  return current_order
 
# First order, burger
order1 = update_order({'item': 'burger', 'cost': '3.50'})
 
# Second order, just a soda
order2 = update_order({'item': 'soda', 'cost': '1.50'})

 