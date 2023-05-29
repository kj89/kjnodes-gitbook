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
peers="318994f72a78af443880526466fa11e89ea5e055@85.190.254.14:26656,d92268c246e02a54103f7098b901b876c88f006e@5.161.130.108:26656,9876d1b1e5b5968c1c729559325dd909f93c1d34@65.108.238.61:56656,d72875380d7b0b68f071623996bd5a86b7491287@116.202.227.117:31656,54f5df8d6516ead7099191776d9ee2048e0ec947@95.214.53.46:26656,1e3f0aeb6f2a2017b122af2461a75c9695790954@65.108.233.109:10956,bd2ae9f1c42183104719f7c44be078bb7d282a61@65.109.92.241:11056,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13156,55b3cf307182091e60b774712733231a8cc7f448@89.163.132.156:31656,7d85caec437cc8c0a504d6ab3b18fd07c173b2fb@94.130.219.37:26001"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.hid-node/config/config.toml
```
