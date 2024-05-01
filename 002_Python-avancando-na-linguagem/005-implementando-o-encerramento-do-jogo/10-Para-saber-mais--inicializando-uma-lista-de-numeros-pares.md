
# ###################################################################################################################################################################
# ###################################################################################################################################################################
# PUSH

git status
git add .
git commit -m "Módulo 5 - 10 Para saber mais: inicializando uma lista de números pares"
git push
git status


# ###################################################################################################################################################################
# ###################################################################################################################################################################
#   10 Para saber mais: inicializando uma lista de números pares

O recurso List Comprehension também permite utilizar condições para o preenchimento da lista. Considere o objetivo de inicializar uma lista com os números pares a partir de uma lista de números inteiros qualquer, por exemplo, os números 1,3,4,5,7,8,9. Para descobrir se um número é par, usamos a condição numero%2 == 0, que verifica se o resto de uma divisão por 2 é zero. O código abaixo usa um loop para inicializar a lista de pares.

~~~~python
inteiros = [1,3,4,5,7,8,9]
pares = []
for numero in inteiros:
    if numero % 2 == 0:
        pares.append(numero)
~~~~

Pesquise como o podemos usar o List Comprehension para fazer o mesmo que o código acima.




# ###################################################################################################################################################################
# ###################################################################################################################################################################
# RESPOSTA

Pesquise como o podemos usar o List Comprehension para fazer o mesmo que o código acima.


- Pesquisando

<https://realpython.com/list-comprehension-python/>

Earlier, you saw this formula for how to create list comprehensions:

~~~~python
new_list = [expression for member in iterable]
~~~~

While this formula is accurate, it’s also a bit incomplete. A more complete description of the comprehension formula adds support for optional conditionals.

Here, your conditional statement comes just before the closing bracket:

~~~~python
new_list = [expression for member in iterable if conditional]
~~~~

Conditionals are important because they allow list comprehensions to filter out unwanted values, which would normally require a call to filter():

>>> sentence = "the rocket came back from mars"
>>> [char for char in sentence if char in "aeiou"]
['e', 'o', 'e', 'a', 'e', 'a', 'o', 'a']

- Código deste exemplo acima:

~~~~python
sentence = "the rocket came back from mars"
[char for char in sentence if char in "aeiou"]
~~~~

Code Breakdown:

~~~~python
sentence = "the rocket came back from mars"
vowels = [char for char in sentence if char in "aeiou"]
~~~~

    sentence = "the rocket came back from mars":
        This line creates a variable named sentence and assigns it a string value, which is the sentence you want to analyze.

    vowels = [char for char in sentence if char in "aeiou"]:
        This line is a list comprehension in Python, which provides a concise way to create lists based on existing sequences.
        It breaks down as follows:
            vowels = []: Creates an empty list named vowels to store the extracted vowels.
            [char for char in sentence]: Iterates through each character (char) in the sentence string.
            if char in "aeiou": Checks if the current character (char) is present within the string "aeiou" (which represents all lowercase vowels).
            If the condition (if char in "aeiou") is True, the character (char) is added to the vowels list using list comprehension syntax.

Functionality:

    This code essentially extracts all the lowercase vowels (a, e, i, o, u) from the given sentence.
    The list comprehension iterates through each character in the sentence, and if the character is a vowel, it's added to the vowels list.
    After the loop completes, the vowels list will contain only the vowels found in the sentence.

Example:

If you run this code, the output will be:

vowels = ['e', 'o', 'a', 'a', 'e', 'o', 'a']

This shows that the code successfully extracted all the lowercase vowels from the sentence "the rocket came back from mars".