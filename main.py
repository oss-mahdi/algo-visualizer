from algorithms.graph.graphs import Graph
from algorithms.sorting.sorts import Sort


def test_graph_algorithms():
    """Test all graph algorithms comprehensively."""
    print("=" * 60)
    print("GRAPH ALGORITHMS TESTING")
    print("=" * 60)
    
    # Test 1: Unweighted Undirected Graph
    print("\n1. UNWEIGHTED UNDIRECTED GRAPH")
    print("-" * 40)
    
    g1 = Graph(directed=False, weighted=False)
    g1.add_edge(0, 1)
    g1.add_edge(0, 2)
    g1.add_edge(1, 2)
    g1.add_edge(1, 3)
    g1.add_edge(2, 3)
    g1.add_edge(3, 4)
    
    print(f"Graph:\n{g1}")
    print(f"BFS from 0: {g1.bfs(0)}")
    print(f"DFS from 0: {g1.dfs(0)}")
    print(f"Connected: {g1.is_connected()}")
    print(f"Has cycle: {g1.has_cycle()}")
    
    path, dist = g1.shortest_path(0, 4)
    print(f"Shortest path 0->4: {path} (steps: {dist})")
    
    # Test 2: Weighted Undirected Graph
    print("\n2. WEIGHTED UNDIRECTED GRAPH")
    print("-" * 40)
    
    g2 = Graph(directed=False, weighted=True)
    g2.add_edge(0, 1, 4)
    g2.add_edge(0, 2, 2)
    g2.add_edge(1, 2, 1)
    g2.add_edge(1, 3, 5)
    g2.add_edge(2, 3, 8)
    g2.add_edge(2, 4, 10)
    g2.add_edge(3, 4, 2)
    
    print(f"Graph:\n{g2}")
    
    distances, _ = g2.dijkstra(0)
    print(f"Dijkstra distances from 0: {dict(distances)}")
    
    mst_prim = g2.prim(0)
    print(f"Prim's MST: {mst_prim}")
    
    mst_kruskal = g2.kruskal()
    print(f"Kruskal's MST: {mst_kruskal}")
    
    # Test 3: Directed Acyclic Graph (DAG)
    print("\n3. DIRECTED ACYCLIC GRAPH (DAG)")
    print("-" * 40)
    
    g3 = Graph(directed=True, weighted=False)
    g3.add_edge(0, 1)
    g3.add_edge(0, 2)
    g3.add_edge(1, 3)
    g3.add_edge(2, 3)
    g3.add_edge(3, 4)
    g3.add_edge(2, 4)
    
    print(f"Graph:\n{g3}")
    
    try:
        topo = g3.topological_sort()
        print(f"Topological sort: {topo}")
    except ValueError as e:
        print(f"Topo sort error: {e}")
    
    print(f"Has cycle: {g3.has_cycle()}")
    
    # Test 4: Directed Graph with Cycle
    print("\n4. DIRECTED GRAPH WITH CYCLE")
    print("-" * 40)
    
    g4 = Graph(directed=True, weighted=False)
    g4.add_edge(0, 1)
    g4.add_edge(1, 2)
    g4.add_edge(2, 0)  # Creates cycle
    
    print(f"Graph:\n{g4}")
    print(f"Has cycle: {g4.has_cycle()}")
    
    try:
        topo = g4.topological_sort()
        print(f"Topological sort: {topo}")
    except ValueError as e:
        print(f"Topo sort error: {e}")
    
    # Test 5: Weighted Directed Graph
    print("\n5. WEIGHTED DIRECTED GRAPH")
    print("-" * 40)
    
    g5 = Graph(directed=True, weighted=True)
    g5.add_edge(0, 1, 5)
    g5.add_edge(0, 2, 3)
    g5.add_edge(1, 2, 2)
    g5.add_edge(1, 3, 6)
    g5.add_edge(2, 3, 7)
    g5.add_edge(2, 4, 4)
    g5.add_edge(3, 4, 2)
    
    print(f"Graph:\n{g5}")
    
    try:
        distances, _ = g5.bellman_ford(0)
        print(f"Bellman-Ford distances: {dict(distances)}")
    except ValueError as e:
        print(f"Bellman-Ford error: {e}")
    
    path, dist = g5.shortest_path(0, 4)
    print(f"Shortest path 0->4: {path} (cost: {dist})")
    
    print("\n" + "=" * 60)
    print("ALL GRAPH TESTS COMPLETED!")
    print("=" * 60)


if __name__ == "__main__":
    # Test sorting algorithms
    print("SORTING ALGORITHMS TESTING")
    print("=" * 40)
    
    lst = [3, 4, 2, 6, 1, 7, 9, 0, 8, 5]
    print(f"Original list: {lst}")
    
    sorter = Sort(lst)
    sorter.bubble_sort()
    sorter.selection_sort()
    sorter.insertion_sort()
    sorter.merge_sort_recursive()
    sorter.quick_sort()
    sorter.shell_sort()
    sorter.heap_sort()
    
    # Test graph algorithms
    test_graph_algorithms()
