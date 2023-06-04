# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/ojo.png" alt=""><figcaption></figcaption></figure>

Ojo is a decentralized security-first oracle network built  to support the Cosmos Ecosystem. Ojo will source price data  from a diverse catalog of on and off-chain sources and use  advanced security mechanisms to guarantee the integrity of the data it provides.

**Chain ID**: ojo-devnet | **Latest Version Tag**: v0.1.2 | **Wasm**: OFF

[Website](https://ojo.network) | [Discord](https://discord.gg/fd8Yrex8nC) | [Twitter](https://twitter.com/ojo_network)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/ojo-testnet](https://explorer.kjnodes.com/ojo-testnet)

## Public endpoints

* api: [https://ojo-testnet.api.kjnodes.com](https://ojo-testnet.api.kjnodes.com)
* rpc: [https://ojo-testnet.rpc.kjnodes.com](https://ojo-testnet.rpc.kjnodes.com)
* grpc: ojo-testnet.grpc.kjnodes.com:15090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@ojo-testnet.rpc.kjnodes.com:15056
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@ojo-testnet.rpc.kjnodes.com:15059
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/ojo-testnet/addrbook.json > $HOME/.ojo/config/addrbook.json
```

**live-peers** (11)
```bash
peers="dacdb802de389deb5ccf9100e049209f55f62854@188.40.98.169:29656,b4c7205397045d22fe762c8d2021fa4ce6d7ea1e@162.55.39.159:36656,855fc154f9054ce4055719e09ce6f7f1d0ecd9fb@85.10.198.171:36656,18300f0a5973798c3900fe51ff255bb6bca982f9@65.109.65.248:36656,0ae4649c788cd2e86fc1ee0a45dc245c6716004e@95.214.55.25:35656,4cb932af43e2c64a0277516d96410a05294653de@75.119.148.69:26656,2c40b0aedc41b7c1b20c7c243dd5edd698428c41@138.201.85.176:26696,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,66b140833cba7cadd92d544088d735e219adbf01@65.108.226.183:21656,41d974f9a97209a401546a61ea2638a0f8071d79@178.18.252.10:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
