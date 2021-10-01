from rx import create, of, operators as op

# An observable is created with create. On subscription, the function of items is called, emitting those items.
# The callabcks provided to the subscribe function simply print the received items and completion states.
source = of("Alpha", "Beta", "Gamma", "Delta", "Epsilon")
source.subscribe(
    on_next = lambda i: print("Received {0}".format(i)),
    on_error = lambda e: print("Error Occurred: {0}".format(e)),
    on_completed = lambda: print("Done!"),
)

composed = source.pipe(
    op.map(lambda s: len(s)),
    op.filter(lambda i: i >= 5)
)

composed.subscribe(
    on_next = lambda i: print("Received {0}".format(i)),
    on_error = lambda e: print("Error Occurred: {0}".format(e)),
    on_completed = lambda: print("Done!"),
)

#Need a Scheduler to use the two operators subscribe_on() and observe_on() for Concurrency