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
peers="c43c0b1197f60cde53cb94b18d05a8d64d71a72a@162.55.245.219:50656,46be755bb7f34a6f4722713e40c9786266654396@38.242.237.125:26656,7afbf90f6ea9639c783ed38a2628a402bf3d912b@109.205.180.81:56656,9fa6a54e5b9207ea53ddd123f7b417e864b5769d@65.108.49.114:26656,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,f8a62360e6084b6a9ba3f731a1fb708ef3c9c5cf@143.198.136.136:28656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15056,97a388be825fc69fca40a8a3de75aa5794602abb@95.217.225.212:36656,a1a6edee9e7928c97d8f99805757c09a1248b942@194.195.87.28:34656,41d974f9a97209a401546a61ea2638a0f8071d79@178.18.252.10:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
