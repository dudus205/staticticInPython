from faker import Faker
import pandas as pd
import numpy as np

fake = Faker(['it_IT'])


def workers(iterations):
    groups = [fake.color_name(), fake.color_name(), fake.color_name(), fake.color_name(), fake.color_name()]
    full_time = round(iterations / 2)
    half_time = round(iterations / 3)
    part_time = round(iterations - full_time - half_time)
    workers_dictionary = []

    for i in range(iterations):
        if full_time > 0:
            work_type = "Full time"
            full_time = full_time - 1
        elif half_time > 0:
            work_type = "Half time"
            half_time = half_time - 1
        elif part_time > 0:
            work_type = "Part time"
            part_time = part_time - 1

        workers_dictionary.append([fake.random_int() * fake.random_int(1, 5),
                                   fake.name(),
                                   groups[fake.random_int(0, 4)],
                                   fake.date(),  # date default is -30 years
                                   work_type
                                   ])

    workers_df = pd.DataFrame(workers_dictionary)
    return workers_df


def steps(iterations):
    steps = {}
    for i in range(iterations):
        # steps[id(fake.random_int())] = {np.random.gamma(2, 2, 1)[0],
        steps[i] = {id(fake.random_int()): [np.random.gamma(2, 2, 1)[0],
                                            np.random.normal(2, 2, 1)[0],
                                            np.random.exponential(2, 1)[0]
                                            ]}
    return steps


def itemList(worker, part):
    items = []
    for i in part:
        print(part[i][int(str(part[i].keys())[11:24])][0]) #show row
        print(part[i][int(str(part[i].keys())[11:24])][1]) #show row
        print(part[i][int(str(part[i].keys())[11:24])][2]) #show row


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    company = workers(5000)
    print(company)

    parts = steps(100)
    print(parts)

    itemList(company, parts)
