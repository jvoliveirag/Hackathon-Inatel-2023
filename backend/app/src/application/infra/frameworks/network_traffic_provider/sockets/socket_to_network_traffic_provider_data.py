"""
Module containing the "NetworkTrafficProviderData" DataStructure.
TODO: FIX THIS MODULE AND THIS PACKAGE
"""

from typing import Any, Dict, List

from domain.use_cases.network_traffic.interfaces import NetworkTrafficProviderData


from dataclasses import dataclass

@dataclass
class ProtocolTrafficDataModel:
    protocol: str
    download: str
    upload: str


@dataclass
class HostTrafficDataModel:
    host: str
    download: str
    upload: str


class SocketToNetworkTrafficProviderDataBuilder:
    """
    Class to build the network traffic provider data structure
    based on the socket data.
    """

    def build(self, socket_data: Dict[str, Any]) -> NetworkTrafficProviderData:
        """
        Public Method to build the network traffic provider data structure
        based on the socket data.
        """
        protocol_traffic = socket_data.get("protocol_traffic", [])
        protocol_traffic_data_model = self._build_protocol_traffic_data_model(protocol_traffic)

        host_traffic = socket_data.get("host_traffic", [])
        host_traffic_data_model = self._build_host_traffic_data_model(host_traffic)

        network_traffic_provider_data_model = self._build_network_traffic_data_model(
            socket_data,
            protocol_traffic_data_model,
            host_traffic_data_model
        )

        return network_traffic_provider_data_model

    def _build_protocol_traffic_data_model(self, protocol_traffic_data: List[Dict[str, str]]) -> List[ProtocolTrafficDataModel]:
        """
        Private Method to build the protocol traffic data structure.
        """
        traffic_data_list: List[ProtocolTrafficDataModel] = []

        for traffic_data in protocol_traffic_data:
            protocol = traffic_data.get("protocol", "")
            download = traffic_data.get("download", "")
            upload = traffic_data.get("upload", "")

            protocol_traffic_data_model = ProtocolTrafficDataModel(
                protocol=protocol,
                download=download,
                upload=upload
            )

            traffic_data_list.append(protocol_traffic_data_model)

        return traffic_data_list
    
    def _build_host_traffic_data_model(self, host_traffic_data: List[Dict[str, str]]) -> List[HostTrafficDataModel]:
        """
        Private Method to build the host traffic data structure.
        """
        traffic_data_list: List[HostTrafficDataModel] = []

        for traffic_data in host_traffic_data:
            host = traffic_data.get("host", "")
            download = traffic_data.get("download", "")
            upload = traffic_data.get("upload", "")

            host_traffic_data_model = HostTrafficDataModel(
                host=host,
                download=download,
                upload=upload
            )

            traffic_data_list.append(host_traffic_data_model)

        return traffic_data_list
    
    def _build_network_traffic_data_model(
        self,
        network_traffic_data: Dict[str, str],
        protocol_traffic: List[ProtocolTrafficDataModel],
        host_traffic: List[HostTrafficDataModel]
    ) -> Any:
        """
        Private Method to build the network traffic data structure.
        """
        pid = network_traffic_data.get("pid", "")
        name = network_traffic_data.get("name", "")
        create_time = network_traffic_data.get("create_time", "")
        last_time_update = network_traffic_data.get("last_time_update", "")
        upload = network_traffic_data.get("upload", "")
        download = network_traffic_data.get("download", "")
        upload_speed = network_traffic_data.get("upload_speed", "")
        download_speed = network_traffic_data.get("download_speed", "")

        network_traffic_provider_data = NetworkTrafficProviderData(
            pid=pid,
            name=name,
            create_time=create_time,
            last_time_update=last_time_update,
            upload=upload,
            download=download,
            upload_speed=upload_speed,
            download_speed=download_speed,
            protocol_traffic=protocol_traffic,
            host_traffic=host_traffic
        )

        return network_traffic_provider_data
