from ztpy.requests.request_manager import RequestManager
from ztpy.models.network import Network, Networks, NetworkConfigPropertiesManager, NetworkPermissionsPropertiesManager

class NetworkApi:

    def dict_to_network(self, data) -> Network:
        network = Network()
        network.network_id = data.get("id", "")
        network.network_type = data.get("type", "")
        network.clock = data.get("clock", "")
        network.ui = data.get("ui", None)
        network.rules_source = data.get("rulesSource", "")
        network.desccription = data.get("description", "")
        permissions = data.get("permissions", None)
        properties_manager = NetworkPermissionsPropertiesManager()
        network.permissions = properties_manager.GetProperties(permissions)
        network.online_member_count = data.get("onlineMemberCount", -1)
        network.capabilities_by_name = data.get("capatibiliesByName", None)
        network.tags_by_name = data.get("tagsByName", None)
        network.circuit_test_every = data.get("circuitTestEvery", -1)
        config = data.get("config", None)
        configs_manager = NetworkConfigPropertiesManager()
        network.config = configs_manager.GetProperties(config)
        return network

    def get_networks(self) -> list[Network]:
        result = []
        resource = "network"
        request_response = RequestManager.do_get_request(resource)  
        
        for net in request_response:
            network = self.dict_to_network(net)
            result.append(network)
        
        return result

    def get_network(self, network_id: str):
        resource = f"network/{network_id}"
        result = RequestManager.do_get_request(resource)
        return self.dict_to_network(result)

    def post_network(self, nretwork_id: str):
        
        pass


class MemberApi:

    def create(self, network_id):
        pass

    def read(self, network_id, member_id):
        resource = f"network/{network_id}/member/{member_id}"
        request_response = RequestManager.do_get_request(resource)
        return request_response

    def inventory(self, network_id):
        resource = f"network/{network_id}/member"
        request_response = RequestManager.do_get_request(resource)
        return request_response

    def update(self, network_id, member_id):
        pass

    def delete(self, network_id, member_id):
        pass




