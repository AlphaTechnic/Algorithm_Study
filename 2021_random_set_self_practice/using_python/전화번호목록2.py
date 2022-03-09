phonebook_set = set()


def solution(phone_book):
    for num in phone_book:
        phonebook_set.add(num)
    for target_num in phone_book:
        accumulated = list()
        for ch in target_num:
            accumulated.append(ch)
            to_compare = ''.join(accumulated)
            if to_compare in phonebook_set and to_compare != target_num:
                return False
    return True


if __name__ == "__main__":
    print(solution(["119", "97674223", "1195524421"]))

