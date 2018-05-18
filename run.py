# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)

print "Breadth Search : "
path, expansion = search.breadth_first_graph_search(ab)
path = [x for x in reversed(path.path())]
print "Ruta : %s --> %d Expansiones" %(path, expansion)

print "\nDepth Search : "
path, expansion = search.depth_first_graph_search(ab)
path = [x for x in reversed(path.path())]
print "Ruta : %s --> %d Expansiones" %(path, expansion)

print "\nBranch and Bound : "
path, expansion = search.branch_and_bound_graph_search(ab)
print path.path()
path = [x for x in reversed(path.path())]
print "Ruta : %s --> %d Expansiones" %(path, expansion)

print "\nSubestimated Branch and Bound : "
path, expansion = search.subestimated_branch_and_bound_graph_search(ab)
path = [x for x in reversed(path.path())]
print "Ruta : %s --> %d Expansiones" %(path, expansion)

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
