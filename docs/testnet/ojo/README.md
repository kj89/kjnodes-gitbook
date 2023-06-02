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
peers="fe8c46222c3a013115797176623597aafc16e33a@173.212.203.238:46656,bfdeba21ca39394ab264fff9c16188b6ecdace6d@144.91.82.61:26656,66b140833cba7cadd92d544088d735e219adbf01@65.108.226.183:21656,e3d56e1538e41115bccdcb0b83a734407d59d2b9@185.219.142.216:50656,fee808fc235e2f345caaaee1d65f818d710f6433@213.137.237.201:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15056,23da6727d574bd04ac40cc8c9cbe301ba8dbdc34@185.198.27.139:32656,d6b0791afd2d41c47bce8c152174b40c230988ba@138.201.225.104:47756,7d59fd87e149226d58d28846a17711ec8b89888c@65.109.122.105:60956,41d974f9a97209a401546a61ea2638a0f8071d79@178.18.252.10:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
