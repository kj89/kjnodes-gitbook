# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quasar.png" alt=""><figcaption></figcaption></figure>

Quasar (pronounced QWAY-ZAR) is a decentralized  appchain enabling interchain digital asset management.

**Chain ID**: quasar-1 | **Latest Version Tag**: v0.1.1 | **Wasm**: ON

[Website](https://www.quasar.fi) | [Discord](https://discord.gg/quasarfi) | [Twitter](https://twitter.com/QuasarFi)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/quasar](https://explorer.kjnodes.com/quasar)

## Public endpoints

* api: [https://quasar.api.kjnodes.com](https://quasar.api.kjnodes.com)
* rpc: [https://quasar.rpc.kjnodes.com](https://quasar.rpc.kjnodes.com)
* grpc: quasar.grpc.kjnodes.com:14890

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@quasar.rpc.kjnodes.com:14856
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@quasar.rpc.kjnodes.com:14859
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/quasar/addrbook.json > $HOME/.quasarnode/config/addrbook.json
```

**live-peers** (10)
```bash
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14856,89757803f40da51678451735445ad40d5b15e059@169.155.169.149:26656,b76a4b43471c31cd5f251036d8e70e47dadba1e2@158.247.206.39:10000,471518432477e31ea348af246c0b54095d41352c@134.65.195.144:26656,0f7eca0da978e4304bb81fa1b9d9a1c87c57f45d@38.146.3.147:18256,8688b59432d98b6ded8bed01c3c29d4892ae6e4f@38.146.3.149:18256,6f95ddfd08c07249c4efafb781eb30ca5739b223@65.109.93.44:18256,5a111b281852be31838ecf1202e59981e618355e@89.116.31.95:18256,6f9e244b6e225241c02b235f700c2b0788da982d@148.113.159.22:18256,367d65ece0aafd9b46e15b9dd58fe319d7d29550@143.198.172.109:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quasarnode/config/config.toml
```
