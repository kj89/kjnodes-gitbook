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

**live-peers** (11)
```bash
peers="d11f867df7e498de0835e2d1b5bc34334c7337d1@65.109.31.114:2490,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.84:26656,89757803f40da51678451735445ad40d5b15e059@169.155.169.149:26656,a40e1d5f63fad9e14edb9c95458b27f3c1de858c@116.203.236.246:26618,5a111b281852be31838ecf1202e59981e618355e@89.116.31.95:18256,471518432477e31ea348af246c0b54095d41352c@134.65.195.144:26656,6f9e244b6e225241c02b235f700c2b0788da982d@148.113.159.22:18256,bccdc6cb3a0785bf3ee65d98c38bdd62bb843285@141.95.157.139:18256,1369d544be2680e031b57f30a8d18cbe8b17a8ef@54.38.73.121:26656,fd0bd2366d5941580042cfc6444b9aea12363764@5.78.95.218:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quasarnode/config/config.toml
```
