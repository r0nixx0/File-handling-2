import pytest

from assignment import (
    save_scores,
    average_score,
    filter_passed,
    replace_word,
    remove_line,
)


@pytest.mark.parametrize("names, scores, expected", [
    [["Bat", "Saraa", "Anu"], [78, 91, 65], "Bat,78\nSaraa,91\nAnu,65\n"],
    [["Dorj"], [100], "Dorj,100\n"],
    [["Tuya", "Bold"], [0, 59], "Tuya,0\nBold,59\n"],
    [[], [], ""],
])
def test1_save_scores(tmp_path, names, scores, expected):
    path = tmp_path / "scores.txt"
    save_scores(names, scores, path)
    assert path.read_text() == expected


def test1_overwrites(tmp_path):
    path = tmp_path / "scores.txt"
    save_scores(["Bat", "Saraa"], [78, 91], path)
    save_scores(["Anu"], [65], path)
    assert path.read_text() == "Anu,65\n"


@pytest.mark.parametrize("content, expected", [
    ["Bat,78\nSaraa,91\nAnu,65\n", 78.0],
    ["Bat,70\nSaraa,81\n", 75.5],
    ["Bat,1\nSaraa,2\nAnu,2\n", 1.7],
    ["Dorj,100\n", 100.0],
    ["Bat,70\n\nSaraa,81\n\n", 75.5],
])
def test2_average_score(tmp_path, content, expected):
    path = tmp_path / "scores.txt"
    path.write_text(content)
    assert average_score(path) == expected


def test2_empty_file(tmp_path):
    path = tmp_path / "scores.txt"
    path.write_text("")
    assert average_score(path) == 0


@pytest.mark.parametrize("content, pass_mark, expected_content, expected_count", [
    ["Bat,78\nSaraa,91\nAnu,45\nDorj,50\n", 50, "Bat,78\nSaraa,91\nDorj,50\n", 3],
    ["Bat,78\nSaraa,91\nAnu,45\nDorj,50\n", 80, "Saraa,91\n", 1],
    ["Bat,10\nSaraa,20\n", 50, "", 0],
    ["", 50, "", 0],
])
def test3_filter_passed(tmp_path, content, pass_mark, expected_content, expected_count):
    source = tmp_path / "all.txt"
    destination = tmp_path / "passed.txt"
    source.write_text(content)
    result = filter_passed(source, destination, pass_mark)
    assert destination.read_text() == expected_content
    assert result == expected_count


def test3_source_unchanged(tmp_path):
    source = tmp_path / "all.txt"
    destination = tmp_path / "passed.txt"
    source.write_text("Bat,78\nAnu,45\n")
    filter_passed(source, destination, 50)
    assert source.read_text() == "Bat,78\nAnu,45\n"
    assert destination.read_text() == "Bat,78\n"


@pytest.mark.parametrize("content, old_word, new_word, expected_content, expected_count", [
    ["I like cats.\nCats are cute.\ncats sleep a lot.\n", "cats", "dogs",
     "I like dogs.\nCats are cute.\ndogs sleep a lot.\n", 2],
    ["red red red\n", "red", "blue", "blue blue blue\n", 3],
    ["Hello Bat\nBye Bat\n", "Bat", "Saraa", "Hello Saraa\nBye Saraa\n", 2],
    ["one two\nthree\n", "two", "2", "one 2\nthree\n", 1],
])
def test4_replace_word(tmp_path, content, old_word, new_word, expected_content, expected_count):
    path = tmp_path / "story.txt"
    path.write_text(content)
    result = replace_word(path, old_word, new_word)
    assert path.read_text() == expected_content
    assert result == expected_count


def test4_no_match_keeps_file(tmp_path):
    path = tmp_path / "story.txt"
    path.write_text("I like cats.\nCats are cute.\n")
    assert replace_word(path, "horse", "pony") == 0
    assert path.read_text() == "I like cats.\nCats are cute.\n"


@pytest.mark.parametrize("line_number, expected_content", [
    [1, "Tue\nWed\nThu\n"],
    [2, "Mon\nWed\nThu\n"],
    [4, "Mon\nTue\nWed\n"],
])
def test5_remove_line(tmp_path, line_number, expected_content):
    path = tmp_path / "days.txt"
    path.write_text("Mon\nTue\nWed\nThu\n")
    assert remove_line(path, line_number) == True
    assert path.read_text() == expected_content


@pytest.mark.parametrize("content, line_number", [
    ["Mon\nTue\nWed\nThu\n", 0],
    ["Mon\nTue\nWed\nThu\n", 5],
    ["Mon\nTue\nWed\nThu\n", -1],
    ["", 1],
])
def test5_invalid_line_number(tmp_path, content, line_number):
    path = tmp_path / "days.txt"
    path.write_text(content)
    assert remove_line(path, line_number) == False
    assert path.read_text() == content
