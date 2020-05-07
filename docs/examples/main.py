from onany import dispatch, listener


@listener("event.name")
def on_event_name(*args, **kwargs):
    print("I've been called with {} and {}".format(
        args,
        kwargs
    ))

dispatch(
    "event.name",
    "first_param",
    "second_param",
    "third_param",
    first="param",
    second="param",
    third="param")