import random
import time

loot_pool = [
    ("Common Sword", 50),
    ("Rare Shield", 30),
    ("Epic Bow", 15),
    ("Legendary Dragon Blade", 5)
]

def forge_loot():
    roll = random.randint(1, 100)
    cumulative = 0

    for item, chance in loot_pool:
        cumulative += chance
        if roll <= cumulative:
            return item

def main():
    print("🔥 Entering the Luck Forge...")
    time.sleep(1)

    for i in range(3):
        print("Forging loot...")
        time.sleep(1)
        print("✨ You forged:", forge_loot())
        print()

if __name__ == "__main__":
    main()