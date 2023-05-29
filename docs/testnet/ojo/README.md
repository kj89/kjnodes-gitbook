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
peers="43c5a820220dfe96810a7582825acb6caeaaf33e@194.61.28.173:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15056,18300f0a5973798c3900fe51ff255bb6bca982f9@65.109.65.248:36656,7afbf90f6ea9639c783ed38a2628a402bf3d912b@109.205.180.81:56656,a1a6edee9e7928c97d8f99805757c09a1248b942@194.195.87.28:34656,9fa6a54e5b9207ea53ddd123f7b417e864b5769d@65.108.49.114:26656,ed12aee3273baaaf01e357574c1692f12776446d@65.109.117.165:50656,d6318facf0de085644dcf8ba57bcc1725b6ec515@89.58.59.75:36656,7831b3b3d625757c749d17569c6730f6589d35fe@65.109.48.181:29656,ba99038e9de54698765e47316c1d778aeb390a46@95.217.57.232:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
