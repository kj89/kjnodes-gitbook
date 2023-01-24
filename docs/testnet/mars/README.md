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
peers="bd40811e571c11d45ae302e9ab5c47d63c55ad2f@65.108.73.124:25656,8987b47ff9e681299e26e609373bf096cce413e0@185.190.140.105:20656,b36f90fb7763876c5a5999fa3e993f6ef8063969@144.91.66.143:28656,fe8d614aa5899a97c11d0601ef50c3e7ce17d57b@65.108.233.109:18556,1a026f66b85594cf1d842c6f00f665f6d8baddf2@65.108.126.35:33656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:45656,3986b72739988aff6fbba4c2792f185d42779f2e@194.163.160.1:18556,66a77479d79a16e7cb0ba4702708e4554b40b5ea@176.9.146.72:43656,1fb28068ba58e0386c5204ab6a378c1dec9d2acf@65.109.88.254:36656,b3ce16f4a93365cd665801faaa1e43efe1994975@65.109.106.91:25656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
