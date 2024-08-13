person = {
    'first':'Asabeneh',
    'last':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':[
        {'street':'Space street',
        'zipcode':'02210'
        }]
}

for result in person["skills"]:
    print(result["street"])