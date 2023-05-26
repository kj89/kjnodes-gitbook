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
peers="1acc83715399737cff74767e00807d1d402eb1e2@144.91.65.175:26656,83f1e2bfb86a2cf13870cff8f306cd0bc684e40e@194.163.158.209:26656,56615e02aa90e35a20a1fc4c46e78bb00956f07b@192.118.76.199:26681,ec5127072c252f7246fb66f7e7762423a23ff6bd@154.12.228.93:31656,b09953bd16cdb17576c4fc356e39773a8e500133@149.202.73.104:11456,d7c9b9a3c3a6c5f4ccdfb37a8358755b277271c1@3.110.226.164:26656,e8e764fa9ecc5727038099205798520c547d7019@51.178.65.184:25656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13156,55b3cf307182091e60b774712733231a8cc7f448@89.163.132.156:31656,bd2ae9f1c42183104719f7c44be078bb7d282a61@65.109.92.241:11056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.hid-node/config/config.toml
```
