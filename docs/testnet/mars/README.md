# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/mars.png" width="150" alt=""><figcaption></figcaption></figure>

Mars is a credit protocol for the future: non-custodial,  open-source, transparent, algorithmic and community-governed.

**Chain ID**: ares-1 | **Latest Version Tag**: v1.0.0-rc7 | **Wasm**: ON

[Website](https://marsprotocol.io) | [Discord](https://discord.gg/marsprotocol) | [Twitter](https://twitter.com/mars_protocol)


## Chain explorer
[https://explorer.kjnodes.com/mars-testnet](https://explorer.kjnodes.com/mars-testnet)

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
peers="3f83067376eec1d4f97a585b76266cc5b951d02d@144.76.90.130:33656,d46fb5f5e70d5417962bd237d4ec8eb50c89e042@176.9.22.117:23656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:45656,66a77479d79a16e7cb0ba4702708e4554b40b5ea@176.9.146.72:43656,fe98e1374e7fa23356f6b6fb758021c4b3153861@138.201.196.18:26656,e5577ecbf793ce92ce5993c4841a340a4c9db64b@65.108.204.119:46656,1fb28068ba58e0386c5204ab6a378c1dec9d2acf@65.109.88.254:36656,e8f573d581516235258229f4a86de34f98c0e1ad@173.212.223.170:28656,84b3986e9b539f3f690efe5e4df7dfd4c7530289@5.78.40.234:26656,bb2151bd2ffa6f5c93b6cad3d55aaee675a03ef4@161.97.79.100:56656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
