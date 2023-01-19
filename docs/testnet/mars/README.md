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
peers="8cd58bdfadefa1302c30b919b4d8ce9acd53fb0d@65.108.9.230:33656,db6231aafffcd7dff070d76771a9b77dd3ac6521@85.173.113.198:27656,70b4e6ad0c9c3a125acdec4ca47ac148c7e6f552@3.7.14.82:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:45656,59fdbead04db40a8bfcee1b42bc2351e1dc78d2e@207.180.243.64:36656,0690069f3aedf4fc156f3ce4a3b24252b13e36b3@213.239.216.252:41656,79b82583f2d8a0ed187fa2edf1f06c0c712d4989@185.48.24.106:28656,ed98dcc0088888d0eb3fbccc207ace26626b92dd@89.117.59.229:26656,1a026f66b85594cf1d842c6f00f665f6d8baddf2@65.108.126.35:33656,3fb4e5c415a6dc43923d790e65ee0457fdc2e87b@65.109.204.235:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
