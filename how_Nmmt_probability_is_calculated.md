# How is the probability of being "nmmted" calculated?

I am glad you asked! This article (can I call it an article?) will explain how the below formula was created and why it works.

```math
P(\text{nmmt}) = \prod_{i=0}^{4 - S} \left(\frac{D-i}{A-i}\right) \left(1 - \frac{D+S-5}{A+S-5}\right)^{N+S-6}
```

## Getting Started...

### Vocabulary

- **Nmmt**: A "nmmt" is when a player places the sixth card in a stack and takes the other five.
- **Alice**: The player of interest. In this article, we want to find the probability that Alice will be nmmted.

### Variables Used

- $ N = \text{number of players} $

- $ D = \text{card value played} - \text{card value on stack} -1 $ \
    "D" stands for "desired" cards. D equals 1 less than the value of the card Alice played minus the value of the top card of the stack she played in. Think of this as the range of cards within which others can play to help nmmt Alice.

- $ A = \text{number of cards others could play} $ \
    "A" stands for "available" cards. This is the total amount of cards that Alice's opponents could play.

- $ S = \text{number of cards in the stack} $

### Other Important Math Terms

- As we all know, $ \text{Probability} = \frac{\text{desired outcomes}}{\text{possible outcomes}} $

- The AND operator for probability is written with a "$\cap$" symbol. \
    $ P(A) \cap P(B) = P(A) * P(B) $

- The OR operator for probability is written with a "$\cup$" symbol. \
    $ P(A) \cup P(B) = P(A) + P(B) - P(A) * P(B) $

- If $N$ is the number of players, then $N-1$ is the number of opponents.

- If $S$ is the number of cards in the stack, then $5-S$ is the number of cards needed to make Alice's card 6th and nmmt her.

## Caculations

### Approach

Our goal is to calculate the probability that Alice will be nmmted. This can never happen, of course, if there are not enough players to cause the stack of interest to reach 6 cards. Thus, we establish an important rule: If the sum of the cards in the stack and the number of players is less than 6, Alice can never be nmmted.

```math
\text{If } N+S<6, \text{ then } P(\text{nmmt})=0
```

But what about otherwise? For Alice to get nmmted, she must play the 6th card in the stack, not the 5th or 7th card or anything else. To make Alice play 6th, enough players must place cards in the stack before her so that she is 6th. However, we also have to count on the fact that there won't be *too* many players placing before her. Thus, this probability is split into two pieces:

1. Enough players must place before Alice
2. No one else will place before her once this state is reached

### Calculating Step 1

What is the probability that Player X will place a card before Alice? It is the number of cards that fit before Alice's divided by the number of cards Player X could potentially play:

```math
P(X) = \frac{D}{A}
```

Now, what is the probability that the next player, Player Y, will place before Alice? It is the same as before, but this time Player Y has 1 less potential cards to choose from than before. The range within Player Y must play is also 1 less.

```math
P(Y) = \frac{D-1}{A-1}
```

And Player Z? The pattern continues, and this time Player Z has 2 less cards to pick from than Player X.

```math
P(Z) = \frac{D-2}{A-2}
```

To nmmt Alice, we need exactly $5-S$ players to place before her. If $5-S=3$, for example, then the probability of Alice nmmting is

```math
P(\text{nmmt}) =
P(X) \,\cap\, P(Y) \,\cap\, P(Z) = 
\frac{D}{A} * \frac{D-1}{A-1} * \frac{D-2}{A-2}
```

The number of terms is always equal to $5-S$.

```math
P(\text{nmmt}) = \prod_{i=0}^{4-S} \left(\frac{D-i}{A-i}\right)
```

The value of $i$ starts at $0$ and increments up to
$(5-S)-1 \text{, or } 4-S$.