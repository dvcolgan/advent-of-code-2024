from src.day5.util import OrderingRule, UpdatePages, partition


def is_update_valid(rules: list[OrderingRule], update: UpdatePages) -> bool:
    # For every individual page in the update
    for page in update:
        # Gather all rules that involve me as the first rule
        first_rules = [rule for rule in rules if rule[0] == page]

        # Gather all rules that involve me as the second rule
        second_rules = [rule for rule in rules if rule[1] == page]

        before, after = partition(update, page)

        # For all first rule appearances, ensure that the other rule page does not come before me
        for other_page in before:
            if not all([other_page != rule[1] for rule in first_rules]):
                return False

        # For all second rule appearances, ensure that the other rule page does not come after me
        for other_page in after:
            if not all([other_page != rule[0] for rule in second_rules]):
                return False

    return True
