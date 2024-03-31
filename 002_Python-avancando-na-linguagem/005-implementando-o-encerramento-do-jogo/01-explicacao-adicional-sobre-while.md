




- Fonte:
<https://initialcommit.com/blog/python-while-loop-multiple-conditions>


## Python While Loop Multiple Conditions

To combine two conditional expressions into one while loop, you'll need to use logical operators. This tells Python how you want all of your conditional expressions to be evaluated as a whole.


### Logical AND Operator

The first logical operator is and. Here's how you would use it to combine multiple conditional expressions:

~~~~python
while ( CONDITIONAL EXPRESSION A ) and ( CONDITIONAL EXPRESSION B ):
	EXECUTE STATEMENTS
~~~~

Here, the while loop has two conditional expressions, A and B, that it needs to evaluate. The and operator says to evaluate them separately and then consider their results as a whole. If (and only if) both A and B are true, then the loop body will execute. If even one of them is false, then the entire while statement evaluates to false and the loop terminates.

Let's take a look at a code example.

>>> a = 5
>>> b = 10
>>> count = 0
>>> while count < a and count < b:
...     print(f"count: {count}, a: {a}, b: {b}")
...     count += 1
...
count: 0, a: 5, b: 10
count: 1, a: 5, b: 10
count: 2, a: 5, b: 10
count: 3, a: 5, b: 10
count: 4, a: 5, b: 10

You define two new variables, a and b, which are equal to 5 and 10, respectively. Again, you've defined a counter and set it to zero. The while statement now contains two conditional expressions. The first checks to see if count is less than a, and the second checks to see if count is less than b. The logical operator and combines these two conditional expressions so that the loop body will only execute if both are true.

The loop runs for five iterations, incrementing count by 1 each time. In the last iteration, where the loop terminates, the value of count is now 5, which is the same value as a. This means the first conditional expression is now false (5 is not less than 5), so the while loop terminates.

Note that the second condition count < b is still true, even when count is 5. What if you wanted the loop to keep running as long as count is less than one of the variables?



### Logical OR Operator

Logical or is the second operator you can use to combine multiple conditional expressions:

~~~~python
while ( CONDITIONAL EXPRESSION A ) or ( CONDITIONAL EXPRESSION B ):
	EXECUTE STATEMENTS
~~~~

There are still two conditional expressions, A and B, that need to be evaluated. Like logical AND, the or operator says to evaluate them separately and then consider their results as a whole. Now, however, the loop body will execute if at least one of the conditional expressions is true. The loop will only terminate if both expressions are false.
The programming guide I wish I had when I started learning to code... 🚀👨‍💻📚

Image of the cover of the Coding Essentials Guidebook for Developers

Check out our Coding Essentials Guidebook for Developers

Let's take a look at the previous example. The only change is that the while loop now says or instead:

>>> a = 5
>>> b = 10
>>> count = 0
>>> while count < a or count < b:
...     print(f"count: {count}, a: {a}, b: {b}")
...     count += 1
...
count: 0, a: 5, b: 10
count: 1, a: 5, b: 10
count: 2, a: 5, b: 10
count: 3, a: 5, b: 10
count: 4, a: 5, b: 10
count: 5, a: 5, b: 10
count: 6, a: 5, b: 10
count: 7, a: 5, b: 10
count: 8, a: 5, b: 10
count: 9, a: 5, b: 10

Now, the loop doesn't stop after the count variable reaches the same value as a. That's because the second condition, count < b, still holds true. Since at least one condition is true, the loop body continues to execute until count reaches a value of 10. Then, the second condition evaluates to false as well, and the loop terminates.





# ###################################################################################################################################################################
# ###################################################################################################################################################################
# RESUMO

- O uso do "and" e do "or" no laço while funciona assim:
o "and" executa o laço e para quando apenas 1 das condições já atenderem(passarem para *true* ou *false*, dependendo do caso).
já o laço com "or", ele segue executando enquanto alguma das condições não for atendida, o laço só encerra quando as 2 condições forem atendidas.