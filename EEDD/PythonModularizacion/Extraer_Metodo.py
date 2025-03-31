def process_ages(ages):
    total = 0
    average = bucle(ages, total)
    print(f"Total: {total}, Average: {average}")

def bucle(ages, total):
    for age in ages:
        if age > 0:
            total += age
    average = total / len(ages)
    return average
