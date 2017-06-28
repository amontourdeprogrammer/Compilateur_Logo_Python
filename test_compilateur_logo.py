import pytest
from compilateur_logo import compile_logo, deal_with_brackets, deal_with_functions

def test_compile_one_logo_command():
    assert compile_logo([["ar","50"]]) == "ar(50);"
def test_compile_several_logo_commands():
    assert compile_logo([["ar","50"], ["td","90"]]) == "ar(50);\ntd(90);"
def test_isolate_commands_in_brackets():
	assert deal_with_brackets(["repete", "12", "[trait", "td", "30", "td", "50]"]) == ['trait', 'td', '30', 'td', '50']
def test_transform_logo_commands_in_processing():
	assert deal_with_functions(['trait', 'td', '30', 'td', '50']) == "trait();\ntd(30);\ntd(50);"
def test_compile_repete():
    assert compile_logo([["repete", "12", "[trait", "td", "30]"]]) == "for (int i = 0; i < 12; i = i+1){\ntrait();\ntd(30);\n}"
def test_compile_repete_with_other_commands():
	assert compile_logo([["ar","50"], ["td","90"],["repete", "12", "[trait", "td", "30]"], ["ar","50"], ["td","90"]])== "ar(50);\ntd(90);\nfor (int i = 0; i < 12; i = i+1){\ntrait();\ntd(30);\n}\nar(50);\ntd(90);"

#def test_compile_if():
    #assert compile_logo([["si", "1", "<", "2" "[td", "30]"]]) == "if(1<2){\ntd(30);\n}"

#def test_compile_if_else():
    #assert compile_logo([["si", "1", "<", "2", "[td", "30]","[av","60]"]]) == "if(1<2){\ntd(30);\n}else{\nav(60);\n}"





