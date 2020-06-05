# This topology only works for 256 nodes, 16 nodes at each router
# It is also not exactly a fat tree, it is an approximation for the sake of comparison to FLEX-LIONS
# The topology is a 2=layer fat tree topology, with 16 servers at each edge router, in total 16 edge routers and 16 core routers. 
# It is actually more like a CLOS 

from m5.params import *
from m5.objects import *

from BaseTopology import SimpleTopology

class FatTree_sc20(SimpleTopology):
    description='FatTree_sc20'

    def __init__(self, controllers):
        self.nodes = controllers

    def makeTopology(self, options, network, IntLink, ExtLink, Router):
        nodes = self.nodes
        num_pods = 32 
        num_edge_routers  = 512
        num_aggr_routers  = 512
        num_core_routers  = num_aggr_routers/2 
        total_num_routers = num_edge_routers + num_aggr_routers + num_core_routers
	
        edge_per_pod = num_edge_routers / num_pods
        link_latency   = options.link_latency # used by simple and garnet
        router_latency = options.router_latency # only used by garnet

        cntrls_per_router, remainder = divmod(len(nodes), num_edge_routers)

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
            cntrl_level, router_id = divmod(i, num_edge_routers)
	    # print "Connect router ", router_id, " to ", n 
            assert(cntrl_level < cntrls_per_router)
            ext_links.append(ExtLink(link_id=link_count, ext_node=n,
                                    int_node=routers[router_id],
                                    latency = link_latency/16))

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
        link2 = link_count
	# first 32 routers are edge routers, next 32 routers are core routers
        for k in xrange(num_pods):
            for i in xrange(edge_per_pod):
                for j in xrange(num_aggr_routers/num_pods):
                    link_count += 2
            	    # print("Connect router ",(k*edge_per_pod)+i, " to ", (k*edge_per_pod)+num_edge_routers+j) 
                    int_links.append(IntLink(link_id=link_count,
                                         src_node=routers[(k*edge_per_pod)+i],
                                         dst_node=routers[(k*edge_per_pod)+num_edge_routers+j],
                                         latency=link_latency,
                                         weight=1))
                    int_links.append(IntLink(link_id=link_count,
                                         src_node=routers[(k*edge_per_pod)+num_edge_routers+j],
                                         dst_node=routers[(k*edge_per_pod)+i],
                                         latency=link_latency,
                                         weight=1))

        # network.int_links = int_links
        # for j in xrange((num_core_routers/2)):
        for i in xrange(num_aggr_routers):
            # for j in xrange(16):
            for j in xrange(16):    
                # if (i % 2 ==0):
                link_count += 2
                # print("Connect router ",num_edge_routers+i, " to ",num_aggr_routers+num_edge_routers+(16*(i%16))+j)
                int_links.append(IntLink(link_id=link_count,
                                        src_node=routers[num_edge_routers+i],
                                        dst_node=routers[num_aggr_routers+num_edge_routers+(16*(i%16))+j],
                                        latency=link_latency,
                                        weight=1))
                int_links.append(IntLink(link_id=link_count,
                                        src_node=routers[num_aggr_routers+num_edge_routers+(16*(i%16))+j],
                                        dst_node=routers[num_edge_routers+i],
                                        latency=link_latency,
                                        weight=1))
            #     else:
            #         # print("******************")
            #         link_count += 2
		    # # print ("Connect router ",num_edge_routers+i, " to ", num_aggr_routers + num_edge_routers+num_core_routers/2+j)
            #         int_links.append(IntLink(link_id=link_count,
            #                              src_node=routers[num_edge_routers+i],
            #                              dst_node=routers[num_aggr_routers + num_edge_routers+num_core_routers/2+j],
            #                              latency=link_latency,
            #                              weight=1))
            #         int_links.append(IntLink(link_id=link_count,
            #                              src_node=routers[num_aggr_routers + num_edge_routers+num_core_routers/2+j],
            #                              dst_node=routers[num_edge_routers+i],
            #                              latency=link_latency,
            #                              weight=1))
	    
        network.int_links = int_links
        print("LINK Count******************", link_count)
        # print(link_count - link2)



