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

**live-peers** (11)
```bash
peers="d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.84:26656,66e0a7d2c2fc75a91627085d0ac5681a35dfd408@37.252.184.234:26656,d7ea38275af96271fd66194dad3951ef38b8ba7c@193.70.33.64:18256,1369d544be2680e031b57f30a8d18cbe8b17a8ef@54.38.73.121:26656,f2e7f8af9e5f72bcde83a8bc0ca05aded6d51a5e@103.180.28.199:26656,5a111b281852be31838ecf1202e59981e618355e@89.116.31.95:18256,367d65ece0aafd9b46e15b9dd58fe319d7d29550@143.198.172.109:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.193.11:26656,97e4468ac589eac505a800411c635b14511a61bb@134.65.195.240:26656,471518432477e31ea348af246c0b54095d41352c@134.65.195.144:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quasarnode/config/config.toml
```
