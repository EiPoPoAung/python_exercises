from sys import argv
script, user_name=argv
prompt='>'
print (f"Hi %s,I'm the %s script."%(user_name,script))
print("I'd like to ask you a few question.")
print(f"Do you like me %s?"%user_name)
likes=input(prompt)
print(f"Where do you live %s?"%user_name)
lives=input(prompt)
print("Whar kind of computer do you have")
computer=input(prompt)
print(f"""Alright,so you said %r about like me.
        You live in %r.Not sure where that is.
        And you have a %r computer.Nice.
        """% (likes,lives,computer))
