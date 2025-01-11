from pymdbapi.ipam.ipfunctions import get_all_addresses, strip_cidr
from pymdbapi.route_helper import RouteHelper
from flask import request
import ipaddress

class Ipam:
    def __init__(self):
        self.routehelper = RouteHelper()

    def add_network(self) -> tuple:
        new_network_data = request.json
        network_address = new_network_data['network_address']
        cidr = strip_cidr(new_network_data['cidr_mask'])
        
        # Check if the network already exists
        filters = {'network_address': network_address, 'cidr_mask': f'/{cidr}'}
        existing_networks_response, status_code = self.routehelper.get_data('networks', filters=filters)
        existing_networks = existing_networks_response.get_json().get('networks', [])
        if status_code == 200 and existing_networks:
            return {"error": "Network already exists"}, 400

        response, status_code = self.routehelper.upsert_data('networks', new_data=new_network_data)
        if status_code == 201:
            data = response.get_json()
            network_id = data['inserted_id']
            network_response, status_code = self.routehelper.get_data_by_id('networks', network_id)
            network = network_response.get_json()
            network = network[0]
            print(f"Network: {network}", flush=True)
            network_address = network['network_address']
            cidr = strip_cidr(network['cidr_mask'])
            network = ipaddress.IPv4Network(f"{network_address}/{cidr}", strict=False)
            netmask = str(network.netmask)
            addresses = get_all_addresses(network_address, cidr)
            if self.create_addresses(addresses, network_id, netmask):
                return data, 200
            else:
                return {"error": "Failed to create IP addresses", "data": data}, 500
        else:
            return response, status_code

    def create_addresses(self, addresses: list, network_id: str, netmask: str) -> bool:
        fail = 0
        for address in addresses:
            data = { 'ip_address': address, 'subnet': netmask, 'network': { 'id': network_id } }
            response, status_code = self.routehelper.upsert_data('ipaddresses', new_data = data)
            if status_code != 201:
                fail = fail + 1
        return fail == 0


    def scan_network(self, network_id: str) -> tuple:
        network = self.routehelper.get_data_by_id('networks', network_id)
        network_address = network['network_address']
        cidr = network['cidr_mask']
        addresses = get_all_addresses(network_address, int(cidr))
        active_addresses = []
        for address in addresses:
            host_info = self.get_host_info(address)
            if host_info:
                active_addresses.append(host_info)
        return active_addresses, 200

    def get_host_info(self, ip_address: str) -> dict:
        try:
            arp_request = ARP(pdst=ip_address)
            broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
            arp_request_broadcast = broadcast / arp_request
            answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]

            for sent, received in answered_list:
                return {
                    'ip_address': ip_address,
                    'mac_address': received.hwsrc,
                    'host_info': received.summary()
                }
        except Exception as e:
            return {
                'ip_address': ip_address,
                'error': str(e)
            }
        return None
