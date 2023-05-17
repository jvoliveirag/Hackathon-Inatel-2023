""""""

from typing import List

from src.domain.dtos import NetworkTrafficDTO
from src.domain.dtos.host_traffic import HostTrafficDTO
from src.domain.dtos.protocol_traffic import ProtocolTrafficDTO
from src.domain.use_cases.network_traffic.interfaces import NetworkTrafficDataProvider


class NetworkTrafficProviderStub(NetworkTrafficDataProvider):

    def get_data(self) -> List[NetworkTrafficDTO]:
        """
        TODO: FIX THIS
        """
        name = "snapd"
        pid = "634"
        create_time = "16/05/2023, 08:18:24"
        last_time_update = "16/05/2023, 20:04:40"
        upload = "0.00B"
        download = "4.19MB"
        upload_speed = "0.00B"
        download_speed = "78.00B/s"
        host_traffic = HostTrafficDTO(
            host="10.0.16.31",
            download="133.08KB",
            upload="0.00B"
        )
        protocol_traffic = ProtocolTrafficDTO(
            protocol="others",
            download="133.08KB",
            upload="0.00B"
        )

        dtos: List[NetworkTrafficDTO] = []
        for _ in range(3):
            dto = NetworkTrafficDTO(
                name=name,
                pid=pid,
                create_time=create_time,
                last_time_update=last_time_update,
                upload=upload,
                download=download,
                upload_speed=upload_speed,
                download_speed=download_speed,
                host_traffic=[host_traffic],
                protocol_traffic=[protocol_traffic]
            )

            dtos.append(dto)

        return dtos
