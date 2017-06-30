import pytest
from compil_logo_with_class import Commande_Logo

braketless_logo_command = ["av","50"]
several_braketless_logo_command = ["av","50", "td","90", "origine"]
braketmedium_logo_command = ["repete", "12", "[origine", "td", "30", "td", "50]"]
braketfull_logo_command = ["repete", "12", "[repete", "4", "[av", "20]", "td", "30]"]
complex_braketfull_logo_command = ["repete", "12", "[origine","repete", "4", "[av", "20]","repete", "6", "[av", "20]", "td", "30]"]

# Create Command object with seperated brackets

def test_compile_one_logo_command():
    a = Commande_Logo(braketless_logo_command)
    assert a.logo_command == ["av", "50"]


def test_prepare_several_braketless_logo_command():
    a = Commande_Logo(several_braketless_logo_command)
    assert a.logo_command == ["av","50", "td","90", "origine"]


def test_prepare_braketmedium_logo_command():
    a = Commande_Logo(braketmedium_logo_command)
    assert a.logo_command == ["repete", "12", "[", "origine", "td", "30", "td", "50", "]"]


def test_prepare_braketfull_logo_command():
    a = Commande_Logo(braketfull_logo_command)
    assert a.logo_command == ["repete", "12", "[","repete", "4", "[", "av", "20", "]", "td", "30", "]"]

# Find deepest brackets

def test_find_braketless_deepest_braket():
    a = Commande_Logo(braketless_logo_command)
    b = a.find_deepest_brackets()
    assert [a.deepest_bracket, a.context, b] == [False, ["av", "50"], False]


def test_find_several_braketless_deepest_braket():
    a = Commande_Logo(several_braketless_logo_command)
    b = a.find_deepest_brackets()
    assert [a.deepest_bracket, a.context, b] == [False, ["av","50", "td","90", "origine"], False]


def test_find_several_braketmedium_deepest_braket():
    a = Commande_Logo(braketmedium_logo_command)
    b = a.find_deepest_brackets()
    assert [a.deepest_bracket, a.context, b] == [["origine", "td", "30", "td", "50"],["repete", "12","CONTENT"], True]


def test_find_several_braketfull_deepest_braket():
    a = Commande_Logo(braketfull_logo_command)
    b = a.find_deepest_brackets()
    assert [a.deepest_bracket, a.context, b] == [["av", "20"],["repete", "12", "[", "repete", "4", "CONTENT", "td", "30","]"], True]

# Deal with expressions

def test_deal_with_braketless_expressions():
    a = Commande_Logo(braketless_logo_command)
    assert a.deal_with_braketless_expressions(a.context) == "av(50);"

def test_deal_with_several_braketless_expressions():
    a = Commande_Logo(several_braketless_logo_command)
    assert a.deal_with_braketless_expressions(a.context) == "av(50);\ntd(90);\norigine();"

# Deal with complex bracket

def test_deal_with_complex_braketless_expressions():
    a = Commande_Logo(braketless_logo_command)
    assert a.deal_with_complex_expression() == "av(50);"

def test_deal_with_complex_several_braketless_expressions():
    a = Commande_Logo(several_braketless_logo_command)
    assert a.deal_with_complex_expression() == "av(50);\ntd(90);\norigine();"

def test_deal_with_complex_braketmedium_expressions():
    a = Commande_Logo(braketmedium_logo_command)
    assert a.deal_with_complex_expression() == "for (int i = 0; i < 12; i = i+1){\norigine();\ntd(30);\ntd(50);\n}"


def test_deal_with_complex_braketfull_expressions():
    a = Commande_Logo(braketfull_logo_command)
    assert a.deal_with_complex_expression() == "for (int i = 0; i < 12; i = i+1){\nfor (int i = 0; i < 4; i = i+1){\nav(20);\n}\ntd(30);\n}"

def _test_deal_with_very_complex_braketfull_expressions():
    a = Commande_Logo(complex_braketfull_logo_command)
    assert a.deal_with_complex_expression() == "tg(79);\nfor (int i = 0; i < 12; i = i+1){\norigine();\nfor (int i = 0; i < 4; i = i+1){\nav(20);\n}\ntd(30);\n}\nfor (int i = 0; i < 6; i = i+1){\nav(20);\n}"

