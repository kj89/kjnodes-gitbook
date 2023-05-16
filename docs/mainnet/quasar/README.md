# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quasar.png" alt=""><figcaption></figcaption></figure>

Quasar (pronounced QWAY-ZAR) is a decentralized  appchain enabling interchain digital asset management.

**Chain ID**: quasar-1 | **Latest Version Tag**: v0.1.0 | **Wasm**: ON

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
peers="a286b35c9e9626cc7b780120ebe4afa883c059ce@144.76.40.53:18256,d7ea38275af96271fd66194dad3951ef38b8ba7c@193.70.33.64:18256,6f9e244b6e225241c02b235f700c2b0788da982d@148.113.159.22:18256,0f7eca0da978e4304bb81fa1b9d9a1c87c57f45d@38.146.3.147:18256,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14856,89757803f40da51678451735445ad40d5b15e059@169.155.169.149:26656,a40e1d5f63fad9e14edb9c95458b27f3c1de858c@116.203.236.246:26618,58a4943a150cc77ab77ded222c44b23548ee702a@146.59.81.23:26667,8688b59432d98b6ded8bed01c3c29d4892ae6e4f@38.146.3.149:18256,fd0bd2366d5941580042cfc6444b9aea12363764@5.78.95.218:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quasarnode/config/config.toml
```
