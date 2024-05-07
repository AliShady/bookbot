def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        c = script(file_contents)
        diction = count(file_contents)
        list_dict = dict_to_list(diction)
        list_dict.sort(reverse=True, key=sort_on)

        report(list_dict, c)
        # print(list_dict)

def dict_to_list(dict):
    dlist = []
    for value in dict:
        d = {}
        d["letter"] = value
        d["num"] = dict[value]
        dlist.append(d)
    # print(dlist)
    return dlist

def report(list_dict, count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document")
    print(" ")
    for dict in list_dict:
        if(dict["letter"].isalpha()):
            print(f"The {dict["letter"]} character was found {dict["num"]} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["num"]
    
def script(book):
    words = book.split()
    # print(words)
    # print(len(words))
    return len(words)

def count(book):
    script = book.lower()
    res = []
    res[:] = script
    count_letter = {}
    for letter in res:
        if letter in count_letter:
            count_letter[letter] = count_letter[letter]+1
        else:
            count_letter[letter] =  1
    return (count_letter)

main()
