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
peers="23eff008c88dcc60ef9a71f2fb469c472679c35e@136.243.88.91:5040,55b3cf307182091e60b774712733231a8cc7f448@89.163.132.156:31656,bbbd2b6da27d29648b4a429885601d8a024633f8@46.166.172.249:31656,e8e764fa9ecc5727038099205798520c547d7019@51.178.65.184:25656,1e3f0aeb6f2a2017b122af2461a75c9695790954@65.108.233.109:10956,5b6356defbfc7227035698d6af7d686d3981a0eb@5.161.99.136:26656,934324c3b4318d8438954d19a82673a3d218951b@142.132.209.236:10956,d7c9b9a3c3a6c5f4ccdfb37a8358755b277271c1@3.110.226.164:26656,5e4fc955b23ab00f6a07cb6d56e89aafac0c85ff@167.86.85.122:26656,efcb16ec33d8e6233d1068fff679c6fd64bf5802@65.108.225.158:10956,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.hid-node/config/config.toml
```
