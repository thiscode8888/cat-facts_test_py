from faker import Faker

fake = Faker()

class FactsHelper():

    def valid_body(self):
        body = {
            'status': {
                'verified': True,
                'sentCount': 1
            },
            '_id': '58e008780aac31001185ed05',
            'user': {
                'name': {
                    'first': 'Kasimir',
                    'last': 'Schulz'
                },
                '_id': '58e007480aac31001185ecef',
                'photo': 'https://lh6.googleusercontent.com/-BS_rskGd3kA/AAAAAAAAAAI/AAAAAAAAADg/yAxrX9QabMg/photo.jpg?sz=200'
            },
            'text': 'Owning a cat can reduce the risk of stroke and heart attack by a third.',
            '__v': 0,
            'source': 'user',
            'updatedAt': '2020-08-23T20:20:01.611Z',
            'type': 'cat',
            'createdAt': '2018-03-29T20:20:03.844Z',
            'deleted': False, 
            'used': False
        }
        return str(body)