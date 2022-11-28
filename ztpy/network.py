from ztpy.request_manager import RequestManager

class Network:

    def get_networks():
        resource = "/api/network"
        result = RequestManager.do_get_request(resource)
        return result

    def get_network(network_id: str):
        resource = f"/api/network/{network_id}"

        pass

    def post_network(nretwork_id: str):
        pass