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

**live-peers** (10)
```bash
peers="02f12e71d5150b49c39123e4e979999b1a08e99d@5.9.79.121:62656,b4c7205397045d22fe762c8d2021fa4ce6d7ea1e@162.55.39.159:36656,1761db35a0402af7d6008705a49dad5c9059ae63@195.231.38.226:28656,7afbf90f6ea9639c783ed38a2628a402bf3d912b@109.205.180.81:56656,66b140833cba7cadd92d544088d735e219adbf01@65.108.226.183:21656,dd100ed6f1046f8db6d1d7ad04ed6253f935e9b2@176.118.198.128:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15056,030c769628e3e56928f8fd143ce9bd9ce53dba34@31.220.85.212:46656,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,eddfe8bf3c478fdd0281808371f9d9d1a3d63308@157.90.208.222:60956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
