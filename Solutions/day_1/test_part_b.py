import pytest

from solution import PassesThroughClicks

dial = range(100)    
start = 50       

# Data for test_twisted_through_click
@pytest.mark.parametrize("input, output", [
    (60, 1),
    (160, 2),
    (-40, 0),
    (-160, 2),
])

def test_twisted_through_click(input, output):
    passes_through_clicks = PassesThroughClicks(start, dial)
    expected_clicks = passes_through_clicks._twisted_through_click(input)
    assert expected_clicks == output

# Data for PassesThroughClicks
@pytest.mark.parametrize("input, output", [
    (["R30"], 0),
    (["L30"],0),
    (["R60"], 1),
    (["L50"], 1),
    (["R100", "R100"], 2),
    (["L100", "R100"], 2),
    (["R100", "L100"], 2),
    (["L100", "L100"], 2),
    (["R1000"], 10),
    # (
    #     [
    #         "L68",
    #         "L30",
    #         "R48",
    #         "L5",
    #         "R60",
    #         "L55",
    #         "L1",
    #         "L99",
    #         "R14",
    #         "L82",
    #     ], 
    #     6
    # ),
])    

def test_passes_through_clicks(input, output):
    passes_through_clicks = PassesThroughClicks(start, dial)
    expected_clicks = passes_through_clicks.run(input)
    assert expected_clicks == output