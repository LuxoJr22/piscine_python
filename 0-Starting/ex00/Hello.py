ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here
ft_list[1] = "World!"

temp = list(ft_tuple)
temp[1] = "France!"
ft_tuple = tuple(temp)

ft_set.remove("tutu!")
ft_set.add("Nice!")

ft_dict["Hello"] = "42Nice!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
