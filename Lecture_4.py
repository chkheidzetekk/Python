# striq_count = 0
# f = open('files.txt', 'r')
# lines= f.readlines()
#
# for striq in  lines:
#     striq_count +=1
# f.close()
#
# print(striq_count)

# # davaleba 1
# striq_count = 0
# with open('files.txt', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#
#     for striq in lines:
#         striq_count += 1
#
# print(striq_count)


# # davaleba 2
# sity_count = 0
# f = open('files.txt', 'r', encoding='utf-8')
# lines = f.readlines()
#
# for line in lines:
#     sity_count += len(line.split())
#
# f.close()
#
# print(sity_count)

# # davaleba 3
# unique_words = set()
# f = open('files.txt', 'r')
# lines = f.readlines()
# for line in lines:
#     words = line.split()
#     unique_words.update(words)
#
# print(len(unique_words))


# # davaleba 4
# from collections import Counter
# 
# with open('files.txt', 'r') as f:
#     word_count = Counter(f.read().split())
#
# print(sum(1 for count in word_count.values() if count > 1))
