
# ✨🧙 The Ancient Scroll of Fibonacci ✨
# Inscribed by Kiro the Grey Hat
# A spell to summon the sacred sequence of numbers

def cast_fibonacci_spell(n):
    """
    🔮 A mystical spell that conjures the first `n` numbers
    of the legendary Fibonacci sequence.
    Each number is the sum of the two spirits before it.
    """
    print("=" * 45)
    print("  ✨ Kiro's Fibonacci Conjuration Spell ✨")
    print("=" * 45)

    if n <= 0:
        print("⚠️  The spell requires at least one number!")
        return []

    sequence = []
    a, b = 0, 1

    print(f"\n🧙 Summoning {n} numbers from the ancient sequence...\n")

    for i in range(n):
        sequence.append(a)
        print(f"  📜 Step {i + 1:>2}: {a}")
        a, b = b, a + b

    print("\n" + "=" * 45)
    print(f"  🔮 The Sacred Sequence: {sequence}")
    print("=" * 45)
    print("\n✨ The spell is complete! The Fibonacci magic flows! ✨\n")

    return sequence

# 🪄 Cast the spell for the first 10 Fibonacci numbers!
result = cast_fibonacci_spell(10)
