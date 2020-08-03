print('\t burger beef \tsalat \tbun \tonion \ttomato \tcalories')
burger_cal = 140
beef_cal = 120
salat_cal = 80
bun_cal = 20
onion_cal = 40
tomato_cal = 20
count = 1
for burger in [0, 1]:
    for beef in [0, 1]:
        for salat in [0, 1]:
            for bun in [0, 1]:
                for onion in [0, 1]:
                    for tomato in [0, 1]:
                        total_cal = (beef * beef_cal)+ (burger * burger_cal) + (salat * salat_cal)\
                        + (bun * bun_cal) + (onion * onion_cal) + (tomato * tomato_cal)
                        print('#', count, '\t', burger,
                              '\t', beef, '\t', salat,
                              '\t',bun, '\t', onion, '\t', tomato, '\t' ,total_cal)
                        count += 1
