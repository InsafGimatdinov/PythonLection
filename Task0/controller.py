# Должен работать с model
import model_quad as model               # controller является связующим звеном
import view

def bottom_click():
    value_a = view.get_value()
    value_b = view.get_value()
    model.init(value_a, value_b)
    result = model.do_it()
    view.view_data(result, "quad")