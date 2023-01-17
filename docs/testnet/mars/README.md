# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/mars.png" width="150" alt=""><figcaption></figcaption></figure>

Mars is a credit protocol for the future: non-custodial,  open-source, transparent, algorithmic and community-governed.

**Chain ID**: ares-1 | **Latest Version Tag**: v1.0.0-rc7 | **Wasm**: ON

[Website](https://marsprotocol.io) | [Discord](https://discord.gg/marsprotocol) | [Twitter](https://twitter.com/mars_protocol)


## Public endpoints

* api: [https://mars-testnet.api.kjnodes.com](https://mars-testnet.api.kjnodes.com)
* rpc: [https://mars-testnet.rpc.kjnodes.com](https://mars-testnet.rpc.kjnodes.com)
* grpc: [https://mars-testnet.grpc.kjnodes.com](https://mars-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@mars-testnet.rpc.kjnodes.com:45656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@mars-testnet.rpc.kjnodes.com:45659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/mars-testnet/addrbook.json > $HOME/.mars/config/addrbook.json
```

**live-peers** (10)
```bash
peers="b36f90fb7763876c5a5999fa3e993f6ef8063969@144.91.66.143:28656,4e58d31ab802dfc20beb398cf86efede5c7faf08@65.108.231.238:36656,e5577ecbf793ce92ce5993c4841a340a4c9db64b@65.108.204.119:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:45656,e6f449525b92a02a8ec882869bc27364a3e2a705@37.187.143.4:45656,8e25b81c1eef854e46f85101d3607c8774323098@104.131.0.19:20656,140249a417f4fc3e0c94726bbb4a58d2beaf3ebc@65.108.75.107:29656,aea09eb8f366e388ca74e3f3ffe6909d5c89d1b9@95.214.55.155:22656,92c3c938d39362d743c3d621619642fc81d5eb0e@91.230.110.200:45656,b3ce16f4a93365cd665801faaa1e43efe1994975@65.109.106.91:25656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
