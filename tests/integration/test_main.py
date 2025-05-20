import rawjs2dict


def test_init_variable():
    script = """var x = 1;"""

    script_dict = rawjs2dict.transform(script)

    assert script_dict == {"x": 1}


def test_init_and_update_variable():
    script = """var x = 1; x = 2;"""

    script_dict = rawjs2dict.transform(script)

    assert script_dict == {"x": [1, 2]}


def test_variable_inside_function():
    script = """function f() { var x = 1; x = 2; }"""

    script_dict = rawjs2dict.transform(script)

    assert script_dict == {"f": {"x": [1, 2]}}


def test_variable_inside_nested_function():
    script = """function f() { function g() { var x = [1, 2]; } }"""

    script_dict = rawjs2dict.transform(script)

    assert script_dict == {"f": {"g": {"x": [1, 2]}}}


def test_variable_inside_class():
    script = """class C { constructor() { var x = 1; x = 2; } }"""

    script_dict = rawjs2dict.transform(script)

    assert script_dict == {"C": {"constructor": {"x": [1, 2]}}}


def test_json_parse_variable():
    script = """var x = JSON.parse('{"a": 1}');"""

    script_dict = rawjs2dict.transform(script)

    assert script_dict == {"x": {"a": 1}}


def test_json_object_variable():
    script = """var x = {a: 1};"""

    script_dict = rawjs2dict.transform(script)

    assert script_dict == {"x": {"a": 1}}


def test_labelled_statement():
    script = """label: var x = 1;"""

    script_dict = rawjs2dict.transform(script)

    assert script_dict == {"label": {"x": 1}}


def test_try_catch():
    script = """try { var x = 1; } catch (e) { var y = 2; }"""

    script_dict = rawjs2dict.transform(script)

    assert script_dict == {"try": {"x": 1}, "catch": {"y": 2}}


def test_if_statement():
    script = """if (true) { var x = 1; } else if (false) { var y = 2; } else { var z = 3; }"""

    script_dict = rawjs2dict.transform(script)

    assert script_dict == {"x": 1, "y": 2, "z": 3}


def test_negative_literal():
    script = """
    return {
        location: {
            latitude: 43.3391455,
            longitude: -1.7807761
        }
    };
    """

    script_dict = rawjs2dict.transform(script)

    assert script_dict == {"return": {"location": {"latitude": 43.3391455, "longitude": -1.7807761}}}
