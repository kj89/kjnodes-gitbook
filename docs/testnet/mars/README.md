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
peers="b36f90fb7763876c5a5999fa3e993f6ef8063969@144.91.66.143:28656,e5577ecbf793ce92ce5993c4841a340a4c9db64b@65.108.204.119:46656,c36d220f73090c242dc5e309695d2c379ee09462@188.166.218.88:20656,75fd0645d505069d293e0fe15170d46e3b8ad5df@173.212.247.6:26656,bb2151bd2ffa6f5c93b6cad3d55aaee675a03ef4@161.97.79.100:56656,79b82583f2d8a0ed187fa2edf1f06c0c712d4989@185.48.24.106:28656,ee4e7bb1590f16d48576b15198cf1ba99cf42f3e@95.216.198.241:26656,140249a417f4fc3e0c94726bbb4a58d2beaf3ebc@65.108.75.107:29656,0f5368092336830876cd9cc2219a6663c4e56b07@95.216.7.169:36656,eb163c2d89d2bfcc1a76a03961c16ea64ad5b58b@157.245.57.33:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
