from metaqnn.grammar.state_enumerator import State



def generate_layer():
    _layer = State(

    ).to_tensorflow_layer()

    print(_layer)


if __name__ == '__main__':
    generate_layer()