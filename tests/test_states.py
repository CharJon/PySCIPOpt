from pyscipopt import Model


def test_model():
    model = Model()
    assert model is not None
    model.readProblem("data/mips/capfac-n5m4r2-243.lp")
    model.optimize()
    state = model.getState()
