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
peers="b09953bd16cdb17576c4fc356e39773a8e500133@149.202.73.104:11456,28fa150b5a843c9bdf2889f31f4ff8ac75c17be9@185.196.20.153:26656,9876d1b1e5b5968c1c729559325dd909f93c1d34@65.108.238.61:56656,bbbd2b6da27d29648b4a429885601d8a024633f8@46.166.172.249:31656,1acc83715399737cff74767e00807d1d402eb1e2@144.91.65.175:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13156,17befe8d02039c5b0f4489d22fcfe768cb35a035@209.145.53.163:10656,1380864bb38481fef4b2358026a5ed53fc027679@95.214.52.206:26656,56615e02aa90e35a20a1fc4c46e78bb00956f07b@192.118.76.199:26681,5a09c55dbbb32b870645f56993e87403dfd17467@162.55.194.205:31656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.hid-node/config/config.toml
```
