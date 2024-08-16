person = {
    'first':'Asabeneh',
    'last':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':
        {
        'street':'Space street',
        'zipcode':'02210'
        }
}
info = [i for i in person['skills'] if i == "JavaScript"]
print(info)