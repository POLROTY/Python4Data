ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here
ft_list[1] = "World!" # the list data structure can be modified like so

ft_tuple = ("Hello", "France!") # A tuple is a list that can't be modified so we need to redefine it

ft_set.remove("tutu!") # A set is a data structure that takes unordered unique elements, so we need to remove the element we don't need and add an other one
ft_set.add("Paris!")

ft_dict["Hello"] = "42Paris!" # a dictionary you change the item coresponding to the key (key-value pairs)

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)