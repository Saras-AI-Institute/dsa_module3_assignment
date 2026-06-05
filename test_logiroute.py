import pytest
from dispatch_engine import Package, binary_search_package, schedule_maximum_deliveries
from router_engine import DeliveryNetworkGraph

def test_task1_binary_search_exact_and_insertion():
    rack = [Package(10, 1.2), Package(20, 3.4), Package(30, 5.6), Package(40, 2.1)]
    
    # Test exact match
    assert binary_search_package(rack, 30) == 2
    assert binary_search_package(rack, 10) == 0
    
    # Test missing item insertion point placement
    assert binary_search_package(rack, 25) == 2 # Should belong right before 30
    assert binary_search_package(rack, 5) == 0  # Should belong at the start
    assert binary_search_package(rack, 50) == 4 # Should belong at the very end

def test_task2_drone_scheduling():
    # Overlapping slots scenario
    slots = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11)]
    
    # The optimal choice picks: (1, 4), (5, 7), (8, 11) -> Total 3 slots
    assert schedule_maximum_deliveries(slots) == 3

def test_task3_route_optimization():
    network = DeliveryNetworkGraph()
    network.add_road("Hub_A", "Hub_B", 4.0)
    network.add_road("Hub_A", "Hub_C", 2.0)
    network.add_road("Hub_B", "Hub_C", 1.0)
    network.add_road("Hub_B", "Hub_D", 5.0)
    network.add_road("Hub_C", "Hub_D", 8.0)
    network.add_road("Hub_C", "Hub_E", 10.0)
    network.add_road("Hub_D", "Hub_E", 2.0)
    
    # Path: A -> C -> B -> D -> E (Distance: 2 + 1 + 5 + 2 = 10)
    shortest_dist = network.find_shortest_delivery_route("Hub_A", "Hub_E")
    assert shortest_dist == 10.0
