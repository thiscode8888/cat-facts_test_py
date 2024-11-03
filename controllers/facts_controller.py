from controllers.base_controller import BaseController

class FactsController(BaseController):

    endpoint = 'facts'

    def get_facts(self):
        return self.request.get(f'{self.base_url}/{self.endpoint}')

    def find_by_id(self, fact_id):
        return self.request.get(f'{self.base_url}/{self.endpoint}/{fact_id}')
