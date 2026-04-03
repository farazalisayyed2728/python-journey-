def print_kwargs(**kwargs):
    for key ,value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name = "faraz" , power = "invisible")
print_kwargs(name = "faraz" )
print_kwargs(name = "faraz" , power = "invisible",enemy = "hayato") 