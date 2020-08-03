print('\tdog \tmustard ketchup mayon \tbun')
count = 1
for dog in [0, 1]:
    for mustard in [0, 1]:
        for ketchup in [0, 1]:
            for mayonnaise in [0, 1]:
                for bun in [0, 1]:
                    print('#', count, '\t',
                          dog, '\t', mustard, '\t',
                          ketchup, '\t', mayonnaise,
                          '\t', bun)
                    count += 1
