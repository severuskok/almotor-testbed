import pytest

from unitsize import human_size, parse_size


def test_bytes_are_printed_whole():
    assert human_size(0) == "0 B"
    assert human_size(1) == "1 B"
    assert human_size(999) == "999 B"


def test_kilobytes():
    assert human_size(2500) == "2.4 KB"
    assert human_size(10_000) == "9.8 KB"


def test_megabytes_and_up():
    assert human_size(5_000_000) == "4.8 MB"
    assert human_size(3_000_000_000) == "2.8 GB"


def test_precision_is_configurable():
    assert human_size(2500, precision=3) == "2.441 KB"


def test_negative_is_rejected():
    with pytest.raises(ValueError):
        human_size(-1)


def test_parse_round_trip():
    assert parse_size("2.4 KB") == 2458
    assert parse_size("1 MB") == 1048576
    assert parse_size("512") == 512


def test_parse_is_case_insensitive():
    assert parse_size("1 kb") == 1024
    assert parse_size("1Kb") == 1024


def test_parse_rejects_rubbish():
    with pytest.raises(ValueError):
        parse_size("")
    with pytest.raises(ValueError):
        parse_size("lots")
    with pytest.raises(ValueError):
        parse_size("12 XB")
