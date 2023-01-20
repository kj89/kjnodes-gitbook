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
peers="0d03b322852add71896c6bbf0010e68410b45ac3@37.187.144.187:32656,3fb4e5c415a6dc43923d790e65ee0457fdc2e87b@65.109.204.235:26656,4aae6c505e4a20415b0d3680e75a526d48c6a370@65.108.238.217:11254,0dd41dec3dcbaeddb2a17813abb7bbb83c85c7b8@65.109.92.48:58656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:45656,ff73c93fea305c14bfe11d773db91e52e5850a80@85.239.235.147:26656,84f1325b17d2d0b7ed78c2f746c2bb515af37d48@65.109.204.197:26656,92c3c938d39362d743c3d621619642fc81d5eb0e@91.230.110.200:45656,c9dd1a617d5d37f08d59f6c695dbafe94279ba62@109.123.254.120:20656,4d0a74f60c0f264e66de823dfbadf0d5ea28b93c@148.251.47.69:33656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
