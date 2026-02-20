# Rex C Reviewer — Persistent Memory

## Learner Profile
- CS50 student, early-to-mid stage
- Works in both C (CS50 lectures) and Python (LeetCode)
- Responds well to direct, technical feedback with concrete examples
- Language: Turkish rules file present — may prefer Turkish explanations; respond in user's language per session

## Score History
| Session | File | Safety | Code Quality | Notes |
|---------|------|--------|--------------|-------|
| 2026-02-20 | Two Sum / two_sum.py | N/A (Python) | 5/10 | First Python review. Return value bug, print-instead-of-return, no edge case handling. Algorithm logic itself is correct (hash map O(n)). |
| 2026-02-20 | Lecture-1 / main.c | 4/10 | 5/10 | First C review. Uninitialized variable + no scanf validation = false win on bad input (confirmed at runtime). No srand seeding. Magic number 100. `int main()` missing void. |

## Recurring Patterns

### Python
- **Return value confusion**: Used `print()` inside function + bare `return` (returns None). Does not return the result to the caller. First occurrence: two_sum.py session 1.
- **Missing no-solution handling**: No guard when no valid pair exists (bare `return` at end of loop is silent).
- **`range(len(nums))` anti-pattern**: Should prefer `enumerate()` in Python.
- **Global test variables**: Defined `nums` and `target` at module scope — acceptable for quick scripts but not LeetCode submission style.

### C
- **Uninitialized variable used after scanf failure**: `int number, guess` declared without initializer; when `scanf("%d", &guess)` fails on non-numeric input, `guess` holds garbage — in this game it happened to equal the target and triggered a false win. First occurrence: Lecture-1/main.c session 2026-02-20.
- **rand() without srand()**: Always produces the same sequence (number = 8 on arm64 macOS). Student has not learned about seeding with `time(NULL)` yet.
- **No scanf return value check**: scanf can fail silently; student does not yet check the return value of I/O functions.
- **`int main()` without void**: Should be `int main(void)` per C standard. clang -Wpedantic flags this.
- **Out-of-range input not rejected**: Guesses of 0 or 101 are accepted silently.
- **Magic number 100**: Should be a named constant `#define MAX_NUMBER 100`.

## Topics to Reinforce
- Python: function return values vs side effects (print)
- Python: enumerate() over range(len())
- Python: type hints — use `list[int]` not bare `list`
- General: always handle the "no answer" case explicitly
- C: always initialize all variables at declaration
- C: always check scanf return value before using the variable it writes
- C: srand(time(NULL)) must precede rand() for non-deterministic output
- C: `int main(void)` not `int main()`

## Improvements Noted
- (none yet — only session 2 for C)
