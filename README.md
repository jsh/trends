# Trends

## Perfect Lives

What's a perfect life?  How about a life where every day is better
than the last? A life where you're happier every day than all the
days that came before.

Is that likely? No.

For example? Imagine that your happiness is at the mercy of fate.
Each day, the universe reaches into a hat, picks a random number,
and that's how your day goes.

If you live for 70 years -- 25,000 days or so -- then that's 25,000
random number. (No two days are exactly the same, so we'll represent
that as 25,000 random reals.)  How many arrangements of those numbers
have every day get better? One. Out of 25000!.

That's roughly 0.0, followed by a ginormous number of 0's. [footnote 1]

## What's a Trend?

"It's getting better all the time."

Okay, what if you relax your criteria a little? Suppose you declare
a near-perfect life to be one where, despite ups and downs, there's
a general upward trend.

An example will make this clearer. Just focus in on a week.
Again, we'll let fate pull your daily numbers out of a hat.  The
odds that every day will be better than the last are only 1/5040
-- about 0.0002) But what about a week like this one:

	Sunday - 2
	Monday - 1
	Tuesday - 4
	Wednesday - 3
	Thursday - 6
	Friday - 5
	Saturday -7

(Yes, I know, those aren't reals. Just put a decimal point in front
of each integer and you'll feel better.)

Every other day is worse than the day before, but there's also a
clear, upward trend.

Let's declare a "trend" to be a period of time in which things get
better _on average_.  At the end of every day, when you climb into
bed to go to sleep, the average day up until now in your life wasn't
as good as the average days still left to you. How does that improve
your odds?
[Days of Our Lives reference.]

Skipping the math -- you can go through it later -- if you
look over N days, there's a 1/N chance that that you'll ride an
upward trend for the whole time. [footnote 2]

If you live to the Biblical, three-score-and-ten, the odds that your whole life
is one, big, upward trend are about one in 25,000.

That's not so small.  Boulder has about 100,000 people.  If it's 1
in 25,000, about four Boulderites will have perfect lives.

The other 99,996 of us? Not so perfect. Life has setbacks. Maybe
you have to move to a giant city for work. Maybe you get a really bad
divorce. Maybe you get cancer.

Whatever.

That's happiness more like this: 92 47 41 98 70 74 14 88 18 83

Things start out great (92), then you move (47).  Things get a bit
better, but then your wife leaves (14). Thing bounce back up (88),
but suddenly you get cancer (18).

Still, you can decompose this into a set of trends:
92 | 47 41 98 70 74 | 14 88 | 18 83

Every one of these chunks is a trend. In each case, when you had a setback, you got back on the horse and looked to the future.

Any sequence of reals can be uniquely decomposed into a series of
adjacent, maximum-length trends. [footnote 3]

They're random, but they look ordered.
[Joni Mitchell "Clouds" quote.]

How many trends does a random sequence of 25,000 reals have? What's the average?
With random numbers, eleven. Ten setbacks.

If these are your days, each trend's a bit under seven years.

## It Depends on How You Look at It.

"An optimist says 'the glass is half full,' a pessimist says, 'the glass is half empty.' An engineer says, 'The glass is twice as big as it needs to be.'"

"Ah," you're saying, "but wait.  I could look at life as a series of *downwar* trends?  All the math must be the same. There must be about four people in Boulder who can get up every day, look in the mirror, and say the rest of their life is headed downhill."  Every day.

Ugh, right?

That's a whole life's equivalent to a week like this:

	Sunday - 7
	Monday - 5
	Tuesday - 6
	Wednesday - 3
	Thursday - 4
	Friday - 1
	Saturday -2

But even a week that sucks as badly as that can be seen another way.

7 | 5 6 | 3 4 | 1 2

It's just a week with some setbacks and shorter, upward trends.

It's the same, random sequence. You get to decide how to describe
it to yourself.

This is an interesting point.

Even if everyone else looks at you and says, "Well, my life's not
perfect, but at leat it's not *his*," you can still look at your
life as a series of upward trends with some setbacks.

How many?

I've already said that a randomly-generated sequence of a lifetime
of days has an average of about a dozen upward trends.

But let's restrict ourselves to randomly generated sequences
of 25000 reals that form a single, downward trend.

Polyanna that you are, try looking at them as upward trends with
setbacks. What's the average number of setbacks? How long are the
average trends *upwards* in these, unfortunate, random sequences
-- in these sucky lives.

Guesses?

The answer is eighteen setbacks, interspersed by four-year trends
in which what's coming is better than what came before. That sounds
a lot better than one, long, downhill slide.

Again, we're talking about the same sequence. The only difference is attitude.
["There's got to be a pony in here, somewhere." cartoon]

Even if you're at the mercy of fate, even if it uncaringly deals
you a bad hand for your entire life, even if it seems like you have
a right to complain, you have a choice.

You can say, "Woe is me.  Oy. vey iz mir. The best is behind me."  

Or you can say, "Yeah, sometimes my luck's not great, but I have
good stretches of years at a time."

If fate's coin flips had been more typical, you might have had six-
or seven-year stretches instead of only four, but four's not bad.

Same data. Your choice of how to see it.

And that's the null-hypothesis case. One where you have no role in your fate.

## Some Math.

(1) 25000!

By Stirling's approximation, N! ~ sqrt(2*pi*N)*(N/e)^N = C*(N/e)^N
N = 2.5*10^4
C = 2*pi*n ~ 6*N ~ 15*10^4
sqrt(2*pi*N) ~ 4*10^2 
N/e ~ 2.5*10^4/2.7 ~ 10^4
(N/e)^n ~ (10^4)^(2.5*10^4) = 10^(10^5)
So 25000! ~ C*10^(10^5), or C followed by 10^5 zeroes.
1/25000! is "0." followed by 10^5 zeroes before the first non-zero digit.

Yowza.

(2) P(a single, upward trend) = 1/N

Consider a sequence of N random reals.  Exactly one circular permutation has a single trend. The subsets that are circular permutations of one another are mutually exclusive, equivalence classes. Thus, the upward trends are at least 1/N of all permutations.

(3) Not every sequence of reals can be uniquely decomposed into
trends. For example, sequences with ties, like [1.0, 1.0, 1.0, ...,
1.0], can't. On the other hand, the probabilty of a random-number
generating such sequences is zero -- the set of such sequences has Lebesgue measure zero -- so you can pretend they don't exist.  [Dilbert cartoon]

(4) Finding a circular permutation that is a single trend.

Any sequence of random reals can be decomposed uniquely into non-overlapping, adjacent trends. The means of these trends decrease, monotonically, from left to right.

Rotate the leftmost trend to the right end. These two trends will merge into a single trend. It's entirely possible that this new trend will merge with its neighbor, in turn, and so on. If that makes the entire, rotated sequence a single trend, we're done.  If not, take the leftmost remaining trend, rotate it to the right end, and continue until there's only one trend.

The details, like "unique decomposition" and "rotations not on trend boundaries don't lead to single trends"? Left to the reader, but aren't hard.

The Python scripts here decompose sequences into trends and rotate them to create a single trend, so you can answer the questions you have yourself.


## References
Andrzej Ehrenfeucht, Jeffrey Haemer, and David Haussler Quasi-Monotonic Sequences: Theory, Algorithms and Applications. SIAM. J. on Algebraic and Discrete Methods 1987;8(3):410-429
