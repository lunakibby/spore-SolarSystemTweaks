import random

# Replace '300' with however many spawns you want, Progenitor is 19, Sparse is 42, Cramped is 2000, Cramped-EX is 8000
def generate_values(n=300):
    results = []
    for _ in range(n):
        value1 = random.uniform(-100, 100)
        value2 = random.uniform(-100, 100)
        value3 = random.randint(0, 3)
        
        results.append(f"\t{value1:.4f}\n\t{value2:.4f}\n\t{value3}")
    return "\n".join(results)

# Replace '300' with however many spawns you want, Progenitor is 19, Sparse is 42, Cramped is 2000, Cramped-EX is 8000
output = generate_values(300)

with open("generated_values.txt", "w") as f:
    f.write(output)

print("File 'generated_values.txt' created with 300 instances.")
