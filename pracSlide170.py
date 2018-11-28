rude_word = ["damn","hell","ass","piss","silly","idiotic"]
comment = input("Please comment our service : ")
commentsplit = comment.split(' ')
rudeSet = set(rude_word)
commentSet = set(commentsplit)
if len(commentSet & rudeSet ) > 0:
    print("Can't Show {0}".format(comment))
else:
    print("Can Show {0}".format(comment))


