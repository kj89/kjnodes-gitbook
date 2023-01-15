# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/mars.png" width="150" alt=""><figcaption></figcaption></figure>

Mars is a credit protocol for the future: non-custodial,  open-source, transparent, algorithmic and community-governed.

**Chain ID**: ares-1 | **Latest Version Tag**: v1.0.0-rc7 | **Wasm**: OFF

[Website](https://marsprotocol.io) | [Discord](https://discord.gg/marsprotocol) | [Twitter](https://twitter.com/mars_protocol)


## Public endpoints

* api: [https://mars-testnet.api.kjnodes.com](https://mars-testnet.api.kjnodes.com)
* rpc: [https://mars-testnet.rpc.kjnodes.com](https://mars-testnet.rpc.kjnodes.com)
* grpc: https://mars-testnet.grpc.kjnodes.com:443

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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:45656,0dd41dec3dcbaeddb2a17813abb7bbb83c85c7b8@65.109.92.48:58656,931d82351a5b96a1e9838008636b98c6e6b530bc@65.108.225.158:18556,4b66ccb20f36e46b980b54f7cd96ee8c4b603a90@65.108.72.233:12656,3f83067376eec1d4f97a585b76266cc5b951d02d@144.76.90.130:33656,fe8d614aa5899a97c11d0601ef50c3e7ce17d57b@65.108.233.109:18556,958433deb6f5c3a5d299705a2371f456a6f377f0@5.189.149.37:26656,3986b72739988aff6fbba4c2792f185d42779f2e@194.163.160.1:18556,00b62bc5966baeefface817ce7c7185d7ffc2ea4@65.108.221.37:26656,7810d82538ad81e2dde14996643f02b5b048eec9@194.163.155.84:44656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
