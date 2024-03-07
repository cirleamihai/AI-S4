import random

def create_cumulative_probabilities(probabilities):
    cumulative_probabilities = []
    cumulative_probability = 0

    for probability in probabilities:
        cumulative_probability += probability
        cumulative_probabilities.append(cumulative_probability)

    return cumulative_probabilities

def low_level_spinner(probability_distribution: dict, seeded: bool = False):
    outcomes = list(probability_distribution.keys())
    probabilities = list(probability_distribution.values())
    cumulative_probabilities = create_cumulative_probabilities(probabilities)
    simulated_outcomes = {outcome: 0 for outcome in outcomes}

    if seeded:
        random.seed(42)

    for i in range(1000):
        random_number = random.random()
        for j, cumulative_probability in enumerate(cumulative_probabilities):
            if random_number <= cumulative_probability:
                outcome = outcomes[j]
                simulated_outcomes[outcome] += 1
                break

    simulated_probabilities = {outcome: f"{count / 10} %" for outcome, count in simulated_outcomes.items()}
    print(simulated_probabilities)
    print(simulated_outcomes)
    print()

def high_level_spinner(probability_distribution: dict, seeded: bool = False):
    if seeded:
        random.seed(42)
    outcomes = list(probability_distribution.keys())
    probabilities = list(probability_distribution.values())

    result = random.choices(outcomes, weights=probabilities, k=1000)
    simulated_outcomes = {outcome: result.count(outcome) for outcome in outcomes}
    simulated_probabilities = {outcome: f"{(count / 10)} %" for outcome, count in simulated_outcomes.items()}

    print(simulated_probabilities)
    print(simulated_outcomes)
    print()

distribution = {
    "blue": 0.2,
    "red": 0.3,
    "green": 0.15,
    "yellow": 0.35
}

def switch_to_probability(distribution_in_degrees: dict):
    total = sum(distribution_in_degrees.values())
    return {key: value / total for key, value in distribution_in_degrees.items()}

distrib_in_degrees = {
    "blue": 45,
    "red": 85,
    "yellow": 70,
    "green": 160
}

# print(switch_to_probability(distrib_in_degrees))

low_level_spinner(distribution)
high_level_spinner(distribution)




