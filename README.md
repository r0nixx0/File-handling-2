# Python File Handling 2
 
Python File handling
https://drive.google.com/file/d/1sIv9rb6PizW9sfts9eVu0BkLYWLjysiT/view

**Rules**

- Always `close()` a file after you finish with it.
- Pick the right mode. `"w"` **erases** the file first. `"a"` **adds** to the end.
  `"r"` only reads.
- `filename` is given to you as a parameter — never type a file name inside
  your function.
- Every line you write must end with `"\n"`.


## Exercise 1

**Problem:**

`names` is a list of student names and `scores` is a list of their scores, in
the same order. Write each student to the file on its own line as
`name,score`. The function returns nothing.

If the file already exists, the old content must be **replaced**, not added to.

**Example:**

    Example Input:
        names    = ["Bat", "Saraa", "Anu"]
        scores   = [78, 91, 65]
        filename = "scores.txt"

    File Output (scores.txt):
        Bat,78
        Saraa,91
        Anu,65

Note the format carefully: name, comma, score — **no spaces**.

*Hint:* `write()` only accepts strings. `str(78)` turns the number 78 into
the string `"78"`.

---

## Exercise 2

**Problem:**

Every line of the file looks like `name,score`. Return the **average** score,
rounded to 1 decimal place with `round(value, 1)`.

- Skip any blank lines completely.
- If the file has no students, return `0`.

**Example:**

    Example File Content (scores.txt):
        Bat,78
        Saraa,91
        Anu,65

    Program Output:
        78.0

    Example File Content (scores.txt):
        Bat,70
        Saraa,81

    Program Output:
        75.5

    Example File Content (empty file):

    Program Output:
        0

*Hint:* `"Saraa,91".split(",")` gives `["Saraa", "91"]`. Use `int()` on the
second part to get the number.

---

## Exercise 3

**Problem:**

Read the file `source`, where every line looks like `name,score`. Write a
**new** file `destination` containing only the students whose score is
`pass_mark` **or more**, in the same `name,score` format.
Return how many students passed.

The `source` file must not be changed.

**Example:**

    Example File Content (all.txt):
        Bat,78
        Saraa,91
        Anu,45
        Dorj,50

    Example Input:
        pass_mark = 50

    File Output (passed.txt):
        Bat,78
        Saraa,91
        Dorj,50

    Program Output:
        3

Dorj has exactly 50 — that is a pass.

*Hint:* read everything from `source` and `close()` it **before** you open
`destination`. Two files, two `open()` calls, two `close()` calls.

---

## Exercise 4

**Problem:**

Replace every `old_word` in the file with `new_word`, and save the file.
Return how many times the word was replaced.

Capital letters matter: `"cats"` does **not** match `"Cats"`.

**Example:**

    Example File Content (story.txt):
        I like cats.
        Cats are cute.
        cats sleep a lot.

    Example Input:
        old_word = "cats"
        new_word = "dogs"

    File Content afterwards (story.txt):
        I like dogs.
        Cats are cute.
        dogs sleep a lot.

    Program Output:
        2

*Hint:* read the whole file with `read()`, `close()` it, then open it again
in `"w"` mode to write the new text. If you open it with `"w"` first, the file
is **erased** before you can read it!

`"red red".count("red")` gives `2`, and `"red red".replace("red", "blue")`
gives `"blue blue"`.

---

## Exercise 5

**Problem:**

Remove line number `line_number` (starting at 1) from the file, and save the
file. Return `True` if the line was removed.

If the file has no line with that number, do **not** change the file, and
return `False`.

**Example:**

    Example File Content (days.txt):
        Mon
        Tue
        Wed
        Thu

    Example Input:
        line_number = 2

    File Content afterwards (days.txt):
        Mon
        Wed
        Thu

    Program Output:
        True

    Example Input:
        line_number = 5

    File Content afterwards (days.txt):
        Mon
        Tue
        Wed
        Thu

    Program Output:
        False

*Hint:* `readlines()` gives you a list — line 1 is `lines[0]`. Check the line
number **before** you open the file in `"w"` mode, then write back every line
except the one you are removing.

---
