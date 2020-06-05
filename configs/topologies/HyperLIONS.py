# This topology only works for 256 nodes, 16 nodes at each router
# It is also not exactly a fat tree, it is an approximation for the sake of comparison to FLEX-LIONS
# The topology is a 2=layer fat tree topology, with 16 servers at each edge router, in total 16 edge routers and 16 core routers. 
# It is actually more like a CLOS 

from m5.params import *
from m5.objects import *

from BaseTopology import SimpleTopology

class HyperLIONS(SimpleTopology):
    description='HyperLIONS'

    def __init__(self, controllers):
        self.nodes = controllers

    def makeTopology(self, options, network, IntLink, ExtLink, Router):
        nodes = self.nodes
        k =32 
        num_clusters = k/8
        num_tor_routers  = (k/4) *(k/8) * (k/8)
        intra_pod = k/4
        total_num_routers = num_tor_routers
	
        link_latency   = options.link_latency # used by simple and garnet
        router_latency = options.router_latency # only used by garnet

        cntrls_per_router, remainder = divmod(len(nodes), num_tor_routers)

        routers = [Router(router_id=i, latency = router_latency) \
            for i in range(total_num_routers)]
        network.routers = routers

        link_count = 0

        network_nodes   = []
        remainder_nodes = []
        for node_index in xrange(len(nodes)):
            if node_index < (len(nodes) - remainder):
                network_nodes.append(nodes[node_index])
            else:
                remainder_nodes.append(nodes[node_index])

	# Connect each node to the appropriate router
        ext_links = []
        for (i, n) in enumerate(network_nodes):
            cntrl_level, router_id = divmod(i, num_tor_routers)
#	    print "Connect router ", router_id, " to ", n 
            assert(cntrl_level < cntrls_per_router)
            ext_links.append(ExtLink(link_id=link_count, ext_node=n,
                                    int_node=routers[router_id],
                                    latency = link_latency/16)) #link_latency/3
            link_count += 1

        # Connect the remainding nodes to router 0.  These should only be
        # DMA nodes.
        for (i, node) in enumerate(remainder_nodes):
            assert(node.type == 'DMA_Controller')
            assert(i < remainder)
            ext_links.append(ExtLink(link_id=link_count, ext_node=node,
                                    int_node=routers[0],
                                    latency = link_latency))
            link_count += 1

        network.ext_links = ext_links

	# Fat tree topology starts here 
        int_links = []

	# first 32 routers are edge routers, next 32 routers are core routers

        for j in xrange(16):
            for i in xrange(intra_pod):
                for l in xrange(intra_pod):
                    if(i != l):
                        link_count += 1
                        int_links.append(IntLink(link_id=link_count,
                                                src_node=routers[(j*k/4)+i],
                                                dst_node=routers[(j*k/4)+l],
                                                latency=link_latency,
                                                weight=1))
                        

        for j in xrange(4):
            for i in xrange(k):
                for l in xrange(k):
                    if((i != l) and ((i%8) == (l%8))):
                        link_count += 1
                        int_links.append(IntLink(link_id=link_count,
                                                src_node=routers[(j*k)+i],
                                                dst_node=routers[(j*k)+l],
                                                latency=link_latency,
                                                weight=1))

        for j in xrange(128):
            for i in xrange(128):
                if((i != j) and ((i%32) == (j%32))):
                    link_count += 1
                    int_links.append(IntLink(link_id=link_count,
                                            src_node=routers[j],
                                            dst_node=routers[i],
                                            latency=link_latency,
                                            weight=1))
                        
        print("LINK Count******************", link_count)
        network.int_links = int_links



