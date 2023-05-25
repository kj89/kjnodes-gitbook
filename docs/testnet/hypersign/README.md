# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/hypersign.png" alt=""><figcaption></figcaption></figure>

Hypersign is a decentralized identity layer for the internet, giving  users control of their personal data and identity whilst digital  enabling trust for businesses.

**Chain ID**: jagrat | **Latest Version Tag**: v0.1.7 | **Wasm**: OFF

[Website](https://hypersign.id) | [Discord](https://discord.gg/DmuUjMrHVw) | [Twitter](https://twitter.com/hypersignchain)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/hypersign-testnet](https://explorer.kjnodes.com/hypersign-testnet)

## Public endpoints

* api: [https://hypersign-testnet.api.kjnodes.com](https://hypersign-testnet.api.kjnodes.com)
* rpc: [https://hypersign-testnet.rpc.kjnodes.com](https://hypersign-testnet.rpc.kjnodes.com)
* grpc: hypersign-testnet.grpc.kjnodes.com:13190

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@hypersign-testnet.rpc.kjnodes.com:13156
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@hypersign-testnet.rpc.kjnodes.com:13159
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/hypersign-testnet/addrbook.json > $HOME/.hid-node/config/addrbook.json
```

**live-peers** (10)
```bash
peers="c127e8b0608e62709b690037a6b0da635c6f5447@89.58.45.204:56656,1e3f0aeb6f2a2017b122af2461a75c9695790954@65.108.233.109:10956,bd2ae9f1c42183104719f7c44be078bb7d282a61@65.109.92.241:11056,0c6758a3f4554bbc67da73993bbb697764c5c534@38.242.142.227:26656,1380864bb38481fef4b2358026a5ed53fc027679@95.214.52.206:26656,ec5127072c252f7246fb66f7e7762423a23ff6bd@154.12.228.93:31656,23eff008c88dcc60ef9a71f2fb469c472679c35e@136.243.88.91:5040,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13156,d7c9b9a3c3a6c5f4ccdfb37a8358755b277271c1@3.110.226.164:26656,610843eda2f0388cb8e75917e8c1f63350bd3bd1@154.26.131.130:16656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.hid-node/config/config.toml
```
