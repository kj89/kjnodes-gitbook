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
peers="d6b0791afd2d41c47bce8c152174b40c230988ba@138.201.225.104:47756,855fc154f9054ce4055719e09ce6f7f1d0ecd9fb@85.10.198.171:36656,a3b980ccdcf7146fc4a412fb10ad170682263832@62.171.162.229:50656,1879aa588b4d6431bf40543f3a44129dcf60a043@144.91.77.68:50656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15056,8036aed2d37890ddf245e7288b4fc724a301d728@65.109.117.23:50656,9bcec17faba1b8f6583d37103f20bd9b968ac857@38.146.3.230:21656,41d974f9a97209a401546a61ea2638a0f8071d79@178.18.252.10:26656,84074bf78b0a18d2020c3549457f389d7c69ace5@65.108.98.125:60756,20d9bb13b09c054c30f1b48fbd276aa255af5a34@65.108.238.147:37656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
