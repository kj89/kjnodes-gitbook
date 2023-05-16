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
peers="0621bb73d18724cae4eb411e6b96765f95a3345e@178.63.8.245:61356,f8a62360e6084b6a9ba3f731a1fb708ef3c9c5cf@143.198.136.136:28656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15056,d6318facf0de085644dcf8ba57bcc1725b6ec515@89.58.59.75:36656,23830179727e6e38933e95000cb84ece4112f78c@185.155.97.74:18656,67e95aeec46d7c5840f9685ca2b4cd725841b814@16.163.74.176:26636,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,2774da513310abecb7c3c7ec4cb15548f53e7d6b@109.123.248.58:26656,a1a6edee9e7928c97d8f99805757c09a1248b942@194.195.87.28:34656,46984fe69d730d18bfc561830b729fb7689aea2b@95.216.14.46:22656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
