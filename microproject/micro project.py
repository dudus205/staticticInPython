def clean_up_data(data):
    for item in range(len(data)):
        data[item] = data[item].replace("-", "").replace("PL", "").replace(" ", "")

    return list(dict.fromkeys(data))


def validate_nip(data):
    output = []
    for item in range(len(data)):
        control = int(data[item][0]) * 6
        control = control + int(data[item][1]) * 5
        control = control + int(data[item][2]) * 7
        control = control + int(data[item][3]) * 2
        control = control + int(data[item][4]) * 3
        control = control + int(data[item][5]) * 4
        control = control + int(data[item][6]) * 5
        control = control + int(data[item][7]) * 6
        control = control + int(data[item][8]) * 7
        control = control % 11
        if control == int(data[item][9]):
            output.append(data[item])

    return output


if __name__ == '__main__':
    data = [
        '6312609607',
        '828 131 62 12',
        '7392954381',
        '4980117337',
        '7431641598',
        '7393029517',
        '744-15-16-966',
        '5711503502',
        '7540335340',
        '5422698451',
        '5541007223',
        '984-00-78-782',
        '7393208668',
        '6422105641',
        'PL6331813071',
        '5422449707',
        '5260300292',
        '583-101-48-98',
        '7792081703',
        'PL 6391747857',
        '9691227069',
        '7491899923',
        '0000000000',
        '754 033 53 40'
    ]

    data = clean_up_data(data)
    data = validate_nip(data)
    print(data)
