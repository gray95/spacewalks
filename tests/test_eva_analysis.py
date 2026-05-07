import pytest
from eva_data_analysis import text_to_duration, calculate_crew_size

def test_text_to_duration_float():
    """
    Test that text_to_duration returns expected ground truth values for typical
    durations with a non-zero minute component.
    """
    assert abs(text_to_duration("10:20")) == pytest.approx(10.333333)

def test_text_to_duration():
    """
    Test that text_to_duration returns expected ground truth values for typical
    whole hour durations
    """
    input_value = "10:00"
    assert text_to_duration(input_value) == 10

@pytest.mark.parametrize("input_value, expected_result", [
    ("Barnacle Boy;", 1),
    ("Barnacle Boy; Mermaid Man;", 2)
])
def test_calculate_crew_size(input_value, expected_result):
    """
    Test that calculate_crew_size returns expected number
    """
    assert calculate_crew_size(input_value) == expected_result

def test_calculate_crew_size_edge_case():
    """
    Test calculate_crew_size returns expected values for edge
    case where crew is an empty string
    """
    assert calculate_crew_size("") is None