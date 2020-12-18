# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def defVariable():
    x = [[5, 2, 3], [10, 8, 9]]
    students = [
        {'first_name': 'Michael', 'last_name': 'Jordan'},
        {'first_name': 'John', 'last_name': 'Rosales'}
    ]
    sports_directory = {
        'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
        'soccer': ['Messi', 'Ronaldo', 'Rooney']
    }
    z = [{'x': 10, 'y': 20}]
    return x, students, sports_directory, z


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x,students,sports_directory,z=defVariable()
    x[1][0]=15
    print(x)
    students[0]['last_name']='Briant'
    print(students)
    sports_directory['soccer'][0] = 'Andrés'
    print(sports_directory)
    z[0]['y']=30
    print(z)

