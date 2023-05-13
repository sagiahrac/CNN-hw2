r"""
Use this module to write your answers to the questions in the notebook.

Note: Inside the answer strings you can use Markdown format and also LaTeX
math (delimited with $$).
"""

# ==============
# Part 2 answers


def part2_overfit_hp():
    wstd, lr, reg = 0, 0, 0
    # TODO: Tweak the hyperparameters until you overfit the small dataset.
    # ====== YOUR CODE: ======
    wstd, lr, reg = 0.01, 0.1, 0.01
    # ========================
    return dict(wstd=wstd, lr=lr, reg=reg)


def part2_optim_hp(opt_name):
    wstd, lr, reg, = 0, 0, 0

    # TODO: Tweak the hyperparameters to get the best results you can.
    # You may want to use different hyperparameters for each optimizer.
    # ====== YOUR CODE: ======
    if opt_name == 'vanilla':
        wstd, lr, reg = 0.01, 0.1, 0.0001
    if opt_name == 'momentum':
        wstd, lr, reg = 0.1, 0.1, 0.001
    if opt_name == 'rmsprop':
        wstd, lr, reg = 0.1, 0.001, 0.00001
    # ========================
    return dict(wstd=wstd, lr=lr, reg=reg)


def part2_dropout_hp():
    wstd, lr, = 0, 0
    # TODO: Tweak the hyperparameters to get the model to overfit without
    # dropout.
    # ====== YOUR CODE: ======
    wstd, lr = 0.1, 0.0001
    # ========================
    print(dict(wstd=wstd, lr=lr))
    return dict(wstd=wstd, lr=lr)


part2_q1 = r"""
**-1-**

*Yes* and *No*.

When using dropout, we would expect to see improved generalization performance and reduced overfitting.

**The expected**:
- Dropout indeed constrained overfitting over the training data.
It is possible to see that the training curve is much more representative to unseen data when using dropout.
- Loss variance decrease as dropout increase.

**The unexpected**:
- I'd expect the testing curve with dropout to be more stable than without.
In addition, I believe the saturation point of testing accuracy is usually higher when using dropout, as it is harder to overfit, and we can use better our model expressiveness.
I believe the cause is that we didn't achieve saturation, due to small dataset or short training.
When using dropout, only parts of the weights are getting backpropagated, so sometimes we need more iterations to 
experience large number of weights update to each activation, even though we scaled them appropriately (which only fixes the gradient size).


**-2-**

Training a CNN model with dropout is similar to training an ensemble of expressive (subsets) of CNN
models, a different one each batch. 

With high dropout (0.8), each subset is much smaller, which explains the low training accuracy.
The graphs describe a situation of underfitting, as both training and testsing curves are roughly sharing the same accuracy.

With low dropout (0.4), each subset is bigger, so trainig error increase faster as more activations are getting updated each time.

As we said earlier, the loss variance of of each iteration is smaller as dropout increase, due to the stability reasons mentioned above.

Dropout 0.4 achieves better train and test accuracy than 0.8.
"""

part2_q2 = r"""
**Yes, it is possible.** The relationship between loss and accuracy is not straightforward.
The reason for this is that the cross-entropy loss function is a measure of how well the model's predicted probabilities match the true labels.
If the model's true label predicted probabilities are $\epsilon$ less than the max probability, then a small change can increase accuracy without significantly affecting the loss.
It is possible that each step some predictions got corrected by a small margin above the previous max probability, but instances we failed to predict contibuted a heavier portion to the loss.




"""
# ==============

# ==============
# Part 3 answers

part3_q1 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part3_q2 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part3_q3 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""


part3_q4 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""
