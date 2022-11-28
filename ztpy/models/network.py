import json
from dataclasses import dataclass, field


@dataclass
class ConfigProperty:
    property_id: str = field(init=False)
    nwid: str = field(init=False)
    name: str = field(init=False)
    objtype: str = field(init=False)
    private: bool = field(init=False)
    creation_time: int = field(init=False)
    revision: int = field(init=False)
    last_modified: int = field(init=False)
    multicast_limit: int = field(init=False)
    routes: list = field(init=False)
    rules: list = field(init=False)
    tags: list = field(init=False)
    mtu: int = field(init=False)
    dns: dict = field(init=False)
    capabilities: list = field(init=False)
    total_member_count: int = field(init=False)
    active_member_count: int = field(init=False)
    auth_tokens: list = field(init=False)
    authorized_member_count: int = field(init=False)
    v4_assign_mode: dict = field(init=False)
    v6_assign_mode:dict = field(init=False)


@dataclass
class PermissionProperty:
    t: str = field(init=False)
    r: str = field(init=False)
    m: str = field(init=False)
    d: str = field(init=False)
    a: str = field(init=False)


class NetworkPermissionsPropertiesManager:

    def __dict_to_permission_property(self, perm_property: dict):
        pp = PermissionProperty()
        pp.t = perm_property.get("t", "")
        pp.r = perm_property.get("r", "")
        pp.m = perm_property.get("m", "")
        pp.d = perm_property.get("d", "")
        pp.a = perm_property.get("a", "")
        return pp

    def __list_to_config_properties(self, properties: list):
        permission_properties = []
        for element in properties:
            p = self.__dict_to_permission_property(element)
            permission_properties.append(p) 
        return permission_properties

    def GetProperties(self, data) -> list[PermissionProperty]:
        
        if not data:
            return []
        if type(data) == dict:
            pp = self.__dict_to_permission_property(data)
            return [pp]
        elif type(data) == list:
            return self.__list_to_config_properties(data)
        else:
            return []

        
class NetworkConfigPropertiesManager:

    def __dict_to_config_property(self, conf_property: dict):
        cp = ConfigProperty()
        cp.property_id = conf_property.get("id", "")
        cp.nwid = conf_property.get("nwid", "")
        cp.name = conf_property.get("name", "")
        cp.objtype = conf_property.get("objtype","")
        cp.private = conf_property.get("private", "")
        cp.creation_time = conf_property.get("creationTime", "")
        cp.revision = conf_property.get("revision", -1)
        cp.last_modified = conf_property.get("lastModified", -1)
        cp.multicast_limit = conf_property.get("multicastLimit", -1)
        cp.routes = conf_property.get("routes", [])
        cp.rules = conf_property.get("rules", [])
        cp.tags = conf_property.get("tags", [])
        cp.mtu = conf_property.get("mtu", -1)
        cp.dns = conf_property.get("dns", {})
        cp.capabilities = conf_property.get("capabilities", [])
        cp.total_member_count = conf_property.get("totalMemberCount", -1)
        cp.active_member_count = conf_property.get("activeMemberCount", -1)
        cp.auth_tokens = conf_property.get("authTokens", [])
        cp.authorized_member_count = conf_property.get("authorizedMemberCount", -1)
        cp.v4_assign_mode = conf_property.get("v4AssignedMode", {})
        cp.v6_assign_mode = conf_property.get("v6AssignMode", {})
        return cp

    def __list_to_config_properties(self, properties: list):     
        configuration_properties: list = []
        for element in properties:
            p = self.__dict_to_config_property(element)
            configuration_properties.append(p) 
        return configuration_properties

    def GetProperties(self, data) -> list[ConfigProperty]:

        if not data:
            return []

        if type(data) == dict:
            cp = self.__dict_to_config_property(data)
            return [cp]
        elif type(data) == list:
            return self.__list_to_config_properties(data)
        else:
            return []


@dataclass
class Config:
    properties: list[ConfigProperty] = field(init=False)

    def add_config(self, data):
        if type(data) == dict:
            cp = ConfigProperty()
            cp.property_id = data.get("id")

            pass
        elif type(data) == list:
            pass

"""  
@dataclass
class Permissions:
    properties: list[Permission]
    description : str = field(init=False)
@dataclass
class GlobalPermission:
    pass
"""

@dataclass
class Network:
    network_id: str = field(init=False)
    network_type: str = field(init=False)
    clock: int = field(init=False)
    ui: int = field(init=False)
    rules_source: int = field(init=False)
    description: int = field(init=False)
    permissions: list[PermissionProperty] = field(init=False)
    online_member_count: int = field(init=False)
    capabilities_by_name: dict = field(init=False)
    tags_by_name: dict = field(init=False)
    circuit_test_every: int = field(init=False)
    config: list[ConfigProperty] = field(init=False)
    description: str = field(init=False)


class Networks:
    def __init__(self) -> None:
        self.__networks: list[Network] = [] 

    def add_network(self, network: Network):
        self.__networks.append(network)

    def get_networks(self) -> list[Network]:
        return self.__networks