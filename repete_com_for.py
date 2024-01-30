#! bin/ usr/ env python3

# for loops/ laço for

original = [1,2,3,4]
dobrada = []
for n in original:
    dobrada.append(n*2)
print(dobrada)

# list comprehesion

dobrada2 = [n * 2 for n in original]
print(dobrada2)

# printar apenas os resultados da multiplicação que sejam par

dobradapar = [n * 2 for n in range(1,700,6) if n * 2 % 2 == 0]
print(dobradapar)

# podemos também fazer o dict comprehesion

clientes = {
            line.split(",")[0]:line.split(",")[1].strip()
            for line in open("emails.txt")
}
print(clientes)

# Podemos também seguir com o processo normal

clientes2 = {}
for line in open("emails.txt"):
    key,value = line.split(",")
    clientes2[key]=value.strip()
print(clientes2)