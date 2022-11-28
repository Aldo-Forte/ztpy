import json
from dataclasses import dataclass, field


class MemberConfigProperty:
    node_id: str = field(init=False)
    address: str = field(init=False)
    nwid: str = field(init=False)
    objtype: str = field(init=False)
    authorized: bool = field(init=False)
    auth_history: list = field(init=False)
    capabilities: list = field(init=False)
    tags: list = field(init=False)
    creation_time: int = field(init=False)
    identity: str = field(init=False)
    ip_assignments: list = field(init=False)
    last_authorized_time: int = field(init=False)
    last_deauthorized_time: int = field(init=False)
    no_auto_assign_ips: bool = field(init=False)
    physical_addr: str = field(init=False)
    revision: int = field(init=False)


class Member:
    member_id: str = field(init=False)
    member_type: str = field(init=False)
    clock: int = field(init=False)
    network_id: str = field(init=False)
    node_id: str = field(init=False)
    controller_id: str = field(init=False)
    hidden: bool = field(init=False)
    name: str = field(init=False)
    description: str = field(init=False)
    online: bool = field(init=False)
    last_online: int = field(init=False)
    last_offline: int = field(init=False)
    physical_address: str = field(init=False)
    physical_location: str = field(init=False)
    client_version: str = field(init=False)
    protocol_version: int = field(init=False)
    supports_circuit_testing: bool = field(init=False)
    supports_rules_engine: bool = field(init=False)
    offline_notify_delay: int = field(init=False)
    config: MemberConfigProperty = field(init=False)



