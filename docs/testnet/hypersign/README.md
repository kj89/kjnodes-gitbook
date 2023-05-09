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
peers="1380864bb38481fef4b2358026a5ed53fc027679@95.214.52.206:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13156,9876d1b1e5b5968c1c729559325dd909f93c1d34@65.108.238.61:56656,bbbd2b6da27d29648b4a429885601d8a024633f8@46.166.172.249:31656,1e3f0aeb6f2a2017b122af2461a75c9695790954@65.108.233.109:10956,54f5df8d6516ead7099191776d9ee2048e0ec947@95.214.53.46:26656,c1b6d86f46eab9d0aa2e4399cddb9cf05d13621a@65.108.206.118:60556,934324c3b4318d8438954d19a82673a3d218951b@142.132.209.236:10956,610843eda2f0388cb8e75917e8c1f63350bd3bd1@154.26.131.130:16656,fd06a873c4172105925ed89e632ff3f369740eed@18.188.21.237:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.hid-node/config/config.toml
```
