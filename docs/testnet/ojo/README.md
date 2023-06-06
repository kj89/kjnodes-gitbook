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
peers="1786d7d18b39d5824cae23e8085c87883ed661e6@65.109.147.57:36656,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15056,b33500a3aaeb7fa116bdbddbe9c91c3158f38f8d@128.199.18.172:26656,b4c7205397045d22fe762c8d2021fa4ce6d7ea1e@162.55.39.159:36656,41d974f9a97209a401546a61ea2638a0f8071d79@178.18.252.10:26656,f12af93f4f59534a022192408c31fdd1d2f1bb0c@38.242.131.92:26656,23e9ab332e123b1458bcaac58302c84805eabfcb@130.185.119.243:26656,c2f1a2474219cdd314e271429b415732261ebaa3@148.251.19.197:26666,23da6727d574bd04ac40cc8c9cbe301ba8dbdc34@185.198.27.139:32656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
