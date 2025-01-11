import ipaddress

def get_all_addresses(network, cidr):
    """
    Generate a list of all possible host addresses within a given network and CIDR notation.
    Args:
        network (str): The network address in string format (e.g., '192.168.1.0').
        cidr (int): The CIDR notation specifying the subnet mask (e.g., 24).
    Returns:
        list: A list of all possible host addresses within the specified network.
    Raises:
        ValueError: If the network address or CIDR notation is invalid.
    Example:
        >>> get_all_addresses('192.168.1.0', 24)
        ['192.168.1.1', '192.168.1.2', ..., '192.168.1.254']
    Note:
        This function uses the `ipaddress` module to calculate the host addresses.   
    """

    try:
        network_with_cidr = f"{network}/{cidr}"
        net = ipaddress.ip_network(network_with_cidr, strict=False)
        return [str(ip) for ip in net.hosts()]
    except ValueError as e:
        print(f"Invalid network address or CIDR notation: {e}")
        return []

def strip_cidr(cidr):
    """
    Extract the integer value from a CIDR notation string or integer.
    Args:
        cidr (str or int): The CIDR notation string (e.g., '/25') or integer (e.g., 25).
    Returns:
        int: The integer value of the CIDR notation (e.g., 25).
    Raises:
        ValueError: If the CIDR notation is invalid.
    Example:
        >>> strip_cidr('/25')
        25
        >>> strip_cidr(25)
        25
    """
    try:
        if isinstance(cidr, str):
            return int(cidr.lstrip('/'))
        elif isinstance(cidr, int):
            return cidr
        else:
            raise ValueError("CIDR notation must be a string or integer")
    except ValueError as e:
        print(f"Invalid CIDR notation: {e}")
        return None
