def direct_flights(graph, city_names):
    total_cost = 0
    for i in range(len(city_names) - 1):
        start_city, end_city = city_names[i], city_names[i+1]
        start_vertex = None
        end_vertex = None

        # Find vertices for the given city names
        for vertex in graph._adjacency_list:
            if vertex.value == start_city:
                start_vertex = vertex
            elif vertex.value == end_city:
                end_vertex = vertex

        if not start_vertex or not end_vertex:
            return False, 0  # One of the cities is not in the graph

        # Check for a direct flight between the two cities
        has_direct_flight = False
        for edge in graph.get_neighbors(start_vertex):
            if edge.vertex == end_vertex:
                total_cost += edge.weight
                has_direct_flight = True
                break

        if not has_direct_flight:
            return False, 0  # No direct flight found

    return True, total_cost
