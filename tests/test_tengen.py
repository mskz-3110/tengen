import tengen as tg

def test_tengen():
  args = ["TENGEN"]
  with open("./tests/templates/done.tngn") as file:
    assert(tg.Template.render(file.read(), args) == "TENGEN is done.")
  with open("./tests/templates/skip.tngn") as file:
    assert(tg.Template.render(file.read(), args) == "TENGEN is skip.")
  with open("./tests/templates/undefined.tngn") as file:
    assert(tg.Template.render(file.read(), args) == "TENGEN is undefined.")
