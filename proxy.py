from coc.server.endpoint import CoCServerEndpoint
from coc.server.factory import CoCServerFactory
from coc.client.endpoint import CoCClientEndpoint

from twisted.internet import reactor

if __name__ == "__main__":

    client_endpoint = CoCClientEndpoint(reactor, "gamea.clashofclans.com", 9339)

    server_endpoint = CoCServerEndpoint(reactor, 9339)
    server_endpoint.listen(CoCServerFactory(client_endpoint))

    print("listening on {}:{} ...".format(server_endpoint.interface, server_endpoint.port))

    reactor.run()
