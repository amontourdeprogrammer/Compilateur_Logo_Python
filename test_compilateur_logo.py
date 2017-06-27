import pytest
from compilateur_logo import compile_logo

def test_compile_one_logo_command():
    assert compile_logo([["ar","50"]]) == "ar(50);"

def test_compile_several_logo_commands():
    assert compile_logo([["ar","50"], ["td","90"]]) == "ar(50);\ntd(90);"

def test_compile_repete():
    assert compile_logo([["repete", "12", "[trait", "td", "30]"]]) == "for(var i, i > 12; i++){\ntrait();\ntd(30);\n}"

def test_compile_if():
    assert compile_logo([["si", "1", "<", "2" "[td", "30]"]]) == "if(1<2){\ntd(30);\n}"

def test_compile_if_else():
    assert compile_logo([["si", "1", "<", "2", "[td", "30]","[av","60]"]]) == "if(1<2){\ntd(30);\n}else{\nav(60);\n}"






