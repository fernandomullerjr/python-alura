Here’s a review of your updated code for PEP 8 compliance, along with some minor improvements:

### 1. **Comments**
   - Ensure that comments are useful and written in English, following PEP 8 guidelines.
   
   **Change:**
   ```python
   # Remember to import the 'random' module
   ```

### 2. **Parentheses in `if` and `while` Statements**
   - Extra parentheses are not required in `while` and `if` statements. PEP 8 suggests avoiding unnecessary parentheses in conditions.

   **Change to:**
   ```python
   while not enforcou and not acertou:
   if chute in palavra_secreta:
   if acertou:
   if __name__ == "__main__":
   ```

### 3. **Use Context Manager for File Handling**
   - It's a good practice to use a `with` statement for file handling, which ensures the file is properly closed after its block of code is executed.

   **Change to:**
   ```python
   def carrega_palavra_secreta():
       with open("palavras.txt", "r") as arquivo:
           palavras = [linha.strip() for linha in arquivo]
   
       numero = random.randrange(0, len(palavras))
       return palavras[numero].upper()
   ```

### 4. **Function and Variable Naming**
   - You are already following PEP 8 conventions by using snake_case for function and variable names, which is great!

### 5. **Inline Improvements**
   - You are using an `index` variable in your `for` loop, but Python provides a more readable and efficient way to handle indexing using `enumerate()`.

   **Change:**
   ```python
   if chute in palavra_secreta:
       for index, letra in enumerate(palavra_secreta):
           if chute == letra:
               letras_acertadas[index] = letra
   ```

### 6. **Line Length**
   - Ensure that lines are no longer than 79 characters, though your code is currently within this limit. Always keep this in mind for readability.

### 7. **Consistent Spacing Around Operators**
   - PEP 8 suggests having spaces around operators for better readability, and your code follows this.

### Revised Code:
Here’s the revised version of your code with PEP 8 improvements:

```python
import random

def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = input("Qual letra? ").strip().upper()

        if chute in palavra_secreta:
            for index, letra in enumerate(palavra_secreta):
                if chute == letra:
                    letras_acertadas[index] = letra
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")

    print("Fim do jogo")


def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def carrega_palavra_secreta():
    with open("palavras.txt", "r") as arquivo:
        palavras = [linha.strip() for linha in arquivo]

    numero = random.randrange(0, len(palavras))
    return palavras[numero].upper()


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


if __name__ == "__main__":
    jogar()
```

### Summary of Changes:
1. Removed unnecessary parentheses in `if` and `while` statements.
2. Used a context manager (`with` statement) for file handling.
3. Replaced `index` handling with `enumerate()` in the loop for better readability and efficiency.
4. Improved the comment at the top of the script.

These changes will make your code more compliant with PEP 8 and improve its readability. Let me know if you have any questions!