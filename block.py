"""
Block: object representing a trend.
"""


class Block:
    """
    An annotated subsequence of reals.
    :param list[float] s: The underlying sequence
    :param int start: The start of the subsequence
    :param int length: The length of the subsequence

    >>> from sequence import Sequence
    >>> s = Sequence([0, 1, 1, 2, 3, 5])
    >>> b = Block(s, 0, 1)
    >>> type(b)
    <class 'block.Block'>
    """

    def __init__(self, seq, start, length, total=None):
        self._seq = seq
        self._start = start
        self._length = length
        if total:
            self._total = total
        else:
            self._total = sum(seq[start : start + length])

    def __repr__(self):
        """representation that permits object creation
        >>> from sequence import Sequence
        >>> s = Sequence([0, 1, 1, 2, 3, 5])
        >>> b = Block(s, 0, 1)
        >>> print(repr(b))
        block.Block([0.0, 1.0, 1.0, 2.0, 3.0, 5.0], 0, 1, total=0.0)
        """
        return "{}.{}({}, {}, {}, total={})".format(
            self.__class__.__module__,
            self.__class__.__qualname__,
            self._seq,
            self._start,
            self._length,
            self._total,
        )

    def __str__(self):
        """user-friendly representation
        >>> from sequence import Sequence
        >>> s = Sequence([0, 1, 1, 2, 3, 5])
        >>> b = Block(s, 0, 1)
        >>> print(b)
        trend: [0.0]
            start: 0, length: 1, mean: 0.0
            (seq: [0.0, 1.0, 1.0, 2.0, 3.0, 5.0])
        """
        return "trend: {}\n    start: {}, length: {}, mean: {}\n    (seq: {})".format(
            self.trend(), self._start, self._length, self.arithmetic_mean(), self.seq
        )

    @property
    def seq(self):
        """the underlying sequence, of which the subsequence is a part.
        >>> from sequence import Sequence
        >>> s = Sequence(69)
        >>> b = Block(s, 0, 1)
        >>> len(b.seq)
        69
        """
        return self._seq

    @property
    def start(self):
        """the subsequence start.
        >>> from sequence import Sequence
        >>> s = Sequence(69)
        >>> b = Block(s, 3, 12)
        >>> b.start
        3
        """
        return self._start

    @property
    def length(self):
        """Subsequence length.
        >>> from sequence import Sequence
        >>> s = Sequence(69)
        >>> b = Block(s, 3, 12)
        >>> b.length
        12
        """
        return self._length

    @property
    def total(self):
        """Block total.
        >>> from sequence import Sequence
        >>> s = Sequence([0, 1, 1, 2, 3, 5])
        >>> b = Block(s, 2, 3)
        >>> b.total
        6.0
        """
        return self._total

    def _left_neighbor(self, other):
        """is self the left-hand neighbor of other?
        :param Block other:
        :return: Whether self is a left neighbor of other.
        :rtype: bool

        >>> from sequence import Sequence
        >>> s = Sequence([0, 1, 1, 2, 3, 5])
        >>> a = Block(s, 0, 2)
        >>> b = Block(s, 2, 2)
        >>> c = Block(s, 4, 2)
        >>> a._left_neighbor(b)
        True
        >>> b._left_neighbor(a)
        False
        >>> c._left_neighbor(a)
        True
        """
        return (self.start + self.length) % len(self.seq) == other.start

    def arithmetic_mean(self):
        """Block mean.
        :return: block mean
        :rtype: float
        >>> from sequence import Sequence
        >>> s = Sequence([0, 1, 1, 2, 3, 5])
        >>> b = Block(s, 0, 6)
        >>> b.arithmetic_mean()
        2.0
        """
        return self.total / self.length

    def trend(self):
        """return block subsequence.
        :return: block trend
        :rtype: list[float]
        >>> from sequence import Sequence
        >>> s = Sequence([0, 1, 1, 2, 3, 5])
        >>> b = Block(s, 1, 2)
        >>> print(b.trend())
        [1.0, 1.0]
        >>> b = Block(s, 5, 2)
        >>> print(b.trend())
        [5.0, 0.0]
        """
        start = self.start
        end = (start + self.length) % len(self.seq)
        if end > start:
            trend = self.seq[start:end]
        else:  # wraps around
            trend = self.seq[start:] + self.seq[:end]
        return trend

    def merge(self, other):
        """ merge adjacent blocks
        :param Block other: right-hand neighbor to merge
        :return: block that includes both
        :rtype: Block

        >>> from sequence import Sequence
        >>> s = Sequence([0, 1, 1, 2, 3, 5])
        >>> b = Block(s, 1, 2)
        >>> c = Block(s, 3, 2)
        >>> merger = b.merge(c)
        >>> merger.length == 4
        True
        >>> merger.start == 1
        True
        >>> merger.total == b.total + c.total
        True
        """
        assert self._left_neighbor(other), "blocks {} and {} not adjacent".format(
            self, other
        )
        merger = Block(
            self.seq,
            self.start,
            self.length + other.length,
            total=self.total + other.total,
        )
        return merger
