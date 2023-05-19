"""
TODO IMPLEMENT
"""

from typing import Any, Dict, List

from ....dtos import NetworkTrafficDTO
from ....dtos.host_traffic import HostTrafficDTO
from ....dtos.protocol_traffic import ProtocolTrafficDTO


JSON_TYPE = Dict[str, Any]


class NetworkTrafficDTOBuilder:
    """
    TODO IMPLEMENT
    """

    @staticmethod
    def build(network_traffic_data: JSON_TYPE) -> NetworkTrafficDTO:
        """
        TODO IMPLEMENT
        """
        host_traffic_data: List[JSON_TYPE] = network_traffic_data.get("host_traffic")  # type: ignore
        host_traffic = NetworkTrafficDTOBuilder._build_host_traffic(host_traffic_data)

        protocol_traffic_data: List[JSON_TYPE] = network_traffic_data.get("protocol_traffic")  # type: ignore
        protocol_traffic = NetworkTrafficDTOBuilder._build_protocol_traffic(protocol_traffic_data)

        network_traffic = NetworkTrafficDTOBuilder._build_network_traffic(network_traffic_data, host_traffic, protocol_traffic)
        return network_traffic

    @staticmethod
    def _build_host_traffic(host_traffic_data: List[JSON_TYPE]) -> List[HostTrafficDTO]:
        """
        TODO IMPLEMENT
        """
        hosts: List[HostTrafficDTO] = []

        for host_traffic in host_traffic_data:
            host = host_traffic.pop("host", "")
            download = host_traffic.pop("download", "")
            upload = host_traffic.pop("upload", "")

            host_traffic_dto = HostTrafficDTO(
                host=host,
                download=download,
                upload=upload,
            )

            hosts.append(host_traffic_dto)

        return hosts

    @staticmethod
    def _build_protocol_traffic(protocol_traffic_data: List[JSON_TYPE]) -> List[ProtocolTrafficDTO]:
        """
        TODO IMPLEMENT
        """
        protocols: List[ProtocolTrafficDTO] = []

        for protocol_traffic in protocol_traffic_data:
            protocol = protocol_traffic.pop("protocol", "")
            download = protocol_traffic.pop("download", "")
            upload = protocol_traffic.pop("upload", "")

            protocol_traffic_dto = ProtocolTrafficDTO(
                protocol=protocol,
                download=download,
                upload=upload,
            )

            protocols.append(protocol_traffic_dto)

        return protocols

    @staticmethod
    def _build_network_traffic(
        network_traffic_data: JSON_TYPE,
        host_traffic: List[HostTrafficDTO],
        protocol_traffic: List[ProtocolTrafficDTO],
    ) -> NetworkTrafficDTO:
        """
        TODO IMPLEMENT
        """
        pid = network_traffic_data.get("pid", "")
        name = network_traffic_data.get("name", "")
        create_time = network_traffic_data.get("create_time", "")
        last_time_update = network_traffic_data.get("last_time_update", "")
        upload = network_traffic_data.get("upload", "")
        download = network_traffic_data.get("download", "")
        upload_speed = network_traffic_data.get("upload_speed", "")
        download_speed = network_traffic_data.get("download_speed", "")

        network_traffic = NetworkTrafficDTO(
            pid=pid,
            name=name,
            create_time=create_time,
            last_time_update=last_time_update,
            upload=upload,
            download=download,
            upload_speed=upload_speed,
            download_speed=download_speed,
            host_traffic=host_traffic,
            protocol_traffic=protocol_traffic,
        )

        return network_traffic
