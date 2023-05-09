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
peers="9a60cf2bb51eed575d58170fcc55901fb99b40a0@194.163.148.202:50656,9d9d7a060cdf621b275c5127e736ad25f381eb6b@95.214.52.138:25676,340f0623e9338a5c93baf2d8a8825718a86d3e8b@195.3.223.196:26656,a9bcb95ee047c4a909c675dc36c556eafe1248e1@195.201.174.109:46656,67e95aeec46d7c5840f9685ca2b4cd725841b814@16.163.74.176:26636,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15056,41d974f9a97209a401546a61ea2638a0f8071d79@178.18.252.10:26656,0a54815282d06cd10ce30b5ba3f9721c6ca1b600@135.181.33.42:50656,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,f35a6ea4693d24d3727a8e866acab2a9faa2ddbc@91.223.3.144:26256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
