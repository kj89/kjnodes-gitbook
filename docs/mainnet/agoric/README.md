# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/agoric.png" width="150" alt=""><figcaption></figcaption></figure>

Agoric is an interoperable Proof-of-Stake chain in the Cosmos ecosystem.  Agoric JavaScript smart contract platform enables 15M+ developers across the  globe to rapidly build and deploy dapps on-chain.

**Chain ID**: agoric-3 | **Latest Version Tag**: pismoC | **Wasm**: OFF

[Website](https://agoric.com) | [Discord](https://discord.com/invite/qDW8DRes4s) | [Twitter](https://twitter.com/agoric)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/agoric/agoricvaloper1ku5sm2twlsywdrp4wz3kfwgyrtqtp0lpr3nvk8)

## Restake

[Restake with kjnodes](https://restake.app/agoric/agoricvaloper1ku5sm2twlsywdrp4wz3kfwgyrtqtp0lpr3nvk8) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/agoric](https://explorer.kjnodes.com/agoric)

## Public endpoints

* api: [https://agoric.api.kjnodes.com](https://agoric.api.kjnodes.com)
* rpc: [https://agoric.rpc.kjnodes.com](https://agoric.rpc.kjnodes.com)
* grpc: [https://agoric.grpc.kjnodes.com](https://agoric.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@agoric.rpc.kjnodes.com:27656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@agoric.rpc.kjnodes.com:27659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/agoric/addrbook.json > $HOME/.agoric/config/addrbook.json
```

**live-peers** (15)
```bash
peers="b2406ba97421a9030bed25560c99b25965b6c336@135.181.2.54:26656,b10682f3c25882b5ef94da284a4a195efad69d0d@95.216.94.106:26656,1cbe5f5c77610bb6568332e026a3b516edeb0121@65.21.234.47:21156,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.135:27106,2aedd7163a8ee725507e461b13fb90c091ee1c42@128.0.51.32:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:27656,9d2bf3feb8a0a95ccce16a94f926d1c5ddad5190@65.108.121.110:12656,4cfac01c912d33f74cb7b66e8b7005aaae47fc2a@146.190.59.8:26060,e70955351f601ea5be9a9bf41032949a777f31b3@207.244.255.229:10003,6ba72731d54ded6d012fa7b02ae46e0c214b1e07@5.75.230.116:26656,1c9a5b1d34b9e6f184b2dcb18ed068cf0c282e50@51.79.98.163:26656,384e9743b277373ba5c06015ef554487c6067bdf@54.74.222.43:30303,d03a9974f14ae380fdb7caf46ec71ce5278f0356@34.72.231.9:26656,ca4c3b9d0cf78d934a3b972c328db2e4a9a66c42@64.32.40.114:26656,00dc1964683a005274c39d3f347e83a5651dd923@65.21.127.159:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.agoric/config/config.toml
```
