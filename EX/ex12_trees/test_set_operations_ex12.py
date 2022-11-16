"""."""

import pytest

from operators.leaf import Leaf
from operators.add import Add
from operators.div import Div
from operators.mul import Mul
from operators.sub import Sub


@pytest.mark.timeout(1.0)
def test_set_leaf_apply_yields_set_when_given_a_set():
    """."""
    assert Leaf({6}).apply() == {6}


@pytest.mark.timeout(1.0)
def test_set_add_adds_when_given_leaves_with_sets():
    """."""
    assert Add(Leaf({5}), Leaf({6})).apply() == {5, 6}
    assert Add(Leaf({7}), Leaf({3})).apply() == {7, 3}
    assert Add(Leaf({5}), Leaf({6})).apply() == {5, 6}
    assert Add(Leaf({5}), Leaf(6)).apply() == {5, 6}
    assert Add(Leaf(5), Leaf({6})).apply() == {5, 6}
    assert Add(Leaf({5, 6}), Leaf({6})).apply() == {5, 6}
    assert Add(Leaf({5, 6}), Leaf(6)).apply() == {5, 6}
    assert Sub(Sub(Leaf({5}), Leaf({7})), Sub(Leaf(5), Leaf(6))).apply() == {5}
    assert Div(Leaf({5, 6}), Leaf({6})).apply() == {5}


@pytest.mark.timeout(1.0)
def test_set_multiply_multiplies_when_given_leaves_with_sets__second_single_element():
    """."""
    assert Mul(Leaf({5, 6}), Leaf({3})).apply() == {frozenset({5, 3}), frozenset({6, 3})}


@pytest.mark.timeout(1.0)
def test_set_multiply_multiplies_when_given_leaves_with_sets__second_multiple_elements():
    """."""
    assert Mul(Leaf({5, 6}), Leaf({3, 4})).apply() == {frozenset({5, 3}), frozenset({6, 3}), frozenset({5, 4}),
                                                       frozenset({6, 4})}
