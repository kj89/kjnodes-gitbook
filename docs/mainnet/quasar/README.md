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
peers="97e4468ac589eac505a800411c635b14511a61bb@134.65.195.240:26656,d7ea38275af96271fd66194dad3951ef38b8ba7c@193.70.33.64:18256,66e0a7d2c2fc75a91627085d0ac5681a35dfd408@37.252.184.234:26656,58a4943a150cc77ab77ded222c44b23548ee702a@146.59.81.23:26667,6cceba286b498d4a1931f85e35ea0fa433373057@169.155.170.222:26656,6f9e244b6e225241c02b235f700c2b0788da982d@148.113.159.22:18256,471518432477e31ea348af246c0b54095d41352c@134.65.195.144:26656,89757803f40da51678451735445ad40d5b15e059@169.155.169.149:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.193.11:26656,0f7eca0da978e4304bb81fa1b9d9a1c87c57f45d@38.146.3.147:18256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quasarnode/config/config.toml
```
