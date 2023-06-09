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

**live-peers** (11)
```bash
peers="52eee2c34150d621312087e49f118969472ba55f@149.102.137.192:26656,1e3f0aeb6f2a2017b122af2461a75c9695790954@65.108.233.109:10956,d7c9b9a3c3a6c5f4ccdfb37a8358755b277271c1@3.110.226.164:26656,15d2f1bc2bfaa143388465ea115c59e5ce6e77dc@65.109.39.223:26656,d92268c246e02a54103f7098b901b876c88f006e@5.161.130.108:26656,1de2abae74a4c5fd7d96d9869ef02187f81498f0@134.209.238.66:26656,5e4fc955b23ab00f6a07cb6d56e89aafac0c85ff@167.86.85.122:26656,17befe8d02039c5b0f4489d22fcfe768cb35a035@209.145.53.163:10656,934324c3b4318d8438954d19a82673a3d218951b@142.132.209.236:10956,b09953bd16cdb17576c4fc356e39773a8e500133@149.202.73.104:11456,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.hid-node/config/config.toml
```
