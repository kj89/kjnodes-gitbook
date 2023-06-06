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
peers="0465032114df76df206c9983968f2d229b3a50d6@88.198.32.17:39656,66b140833cba7cadd92d544088d735e219adbf01@65.108.226.183:21656,c28eda270c571c7cc70bdd0374ae1732f861d8ec@135.181.217.182:37656,dd100ed6f1046f8db6d1d7ad04ed6253f935e9b2@176.118.198.128:26656,f35a6ea4693d24d3727a8e866acab2a9faa2ddbc@91.223.3.144:26256,41d974f9a97209a401546a61ea2638a0f8071d79@178.18.252.10:26656,6e5726d52ed6c854cc0625b32981dd93c01b54d7@135.181.183.62:17656,340f0623e9338a5c93baf2d8a8825718a86d3e8b@195.3.223.196:26656,dacdb802de389deb5ccf9100e049209f55f62854@188.40.98.169:29656,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
