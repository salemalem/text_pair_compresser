from pathlib import Path

initial_file = "words.txt"
compressed_file = "compressed.txt"

print("Initial file size:")
print(Path(initial_file).stat().st_size)

pairs = {}

with open(initial_file) as file: # source: https://www.reddit.com/r/learnpython/comments/3o930t/finding_pairs_of_letter_frequency_in_python/
    words = file.read().splitlines()
    for word in words:
        #treat the word as a sequence, skip the last letter
        for index, letter in enumerate(word[:-1]):
            #form a pair with its next letter
            next_letter = word[index+1]
            pair = letter + next_letter
            #count the pair in the dict by adding 1 to the current value
            #setdefault will return 0 if the pair is not yet in the dict
            pairs[pair] = pairs.setdefault(pair, 0) + 1
pair_keys_last_letter = []
for pair_key in list(pairs.keys()):
    pair_keys_last_letter.append(list(pair_key)[1])
pair_keys_last_letter_unique = list(set(pair_keys_last_letter))
del pair_keys_last_letter
most_frequent_pairs_times = sorted(pairs.values(), reverse = True)
if most_frequent_pairs_times[0] < 10:
    print("It's not benefitial to compress anyway.")
    exit()

frequent_pairs = {}
for most_frequent_pair_time in most_frequent_pairs_times:
    if most_frequent_pair_time < 5:
        break
    temp_index = most_frequent_pairs_times.index(most_frequent_pair_time)
    frequent_pair_key_from_sorted = most_frequent_pairs_times[temp_index]
    frequent_pair_index = list(pairs.values()).index(frequent_pair_key_from_sorted)
    frequent_pair_key = list(pairs.keys())[frequent_pair_index]
    frequent_pair_value = pairs[frequent_pair_key]

    frequent_pairs[frequent_pair_key] = frequent_pair_value

del pairs
del most_frequent_pairs_times

binding_last_to_frequent = {}  # binding last letter to frequent pair
for last_letter in pair_keys_last_letter_unique:
    for frequent_pair_letter in frequent_pairs:
        if last_letter == list(frequent_pair_letter)[1]:
            if last_letter in binding_last_to_frequent:
                if frequent_pairs[frequent_pair_letter] > binding_last_to_frequent[last_letter][1]:
                    binding_last_to_frequent[last_letter] = [frequent_pair_letter, frequent_pairs[frequent_pair_letter]]
            else:
                binding_last_to_frequent[last_letter] = [frequent_pair_letter, frequent_pairs[frequent_pair_letter]]
print(binding_last_to_frequent)

parsed_string_from_txtfile = ''
with open(initial_file, 'r') as txtfile:
    parsed_string_from_txtfile = txtfile.read()

new_string_created = parsed_string_from_txtfile
for binding_last_to_frequent_key in binding_last_to_frequent:
    new_string_created = new_string_created.replace(binding_last_to_frequent[binding_last_to_frequent_key][0], binding_last_to_frequent_key)

# print(parsed_string_from_txtfile)
print("====================")
print(new_string_created)
decompressed_string = new_string_created
for binding_last_to_frequent_key in binding_last_to_frequent:
    decompressed_string = decompressed_string.replace(binding_last_to_frequent_key, binding_last_to_frequent[binding_last_to_frequent_key][0])
print(decompressed_string)

