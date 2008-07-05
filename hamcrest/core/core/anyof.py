from shortcut_combination import ShortcutCombination


class AnyOf(ShortcutCombination):
    """Calculates the logical disjunction of multiple matchers.
    
    Evaluation is shortcut, so subsequent matchers are not called if an earlier
    matcher returns True.
    """
    
    def __init__(self, *matchers):
        super(AnyOf, self).__init__(*matchers)
    
    def matches(self, item):
        return self._matches(item, True)
    
    def describe_to(self, description):
        self._describe_to(description, 'or')


"""Evaluates to true if ANY of the passed in matchers evaluate to true."""
any_of = AnyOf  # Can use directly without a function.
