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
peers="bae51539de7b7b7ac784b4c7dc0bc6c005b4f593@65.109.115.226:18256,bccdc6cb3a0785bf3ee65d98c38bdd62bb843285@141.95.157.139:18256,6f9e244b6e225241c02b235f700c2b0788da982d@148.113.159.22:18256,8688b59432d98b6ded8bed01c3c29d4892ae6e4f@38.146.3.149:18256,201eb8fc1e84beb4bdce8ae5614c7abb41e32edb@65.109.160.91:18256,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14856,49b72b4c79d589955a5004797b45ee306da6a889@143.42.237.237:26656,d7ea38275af96271fd66194dad3951ef38b8ba7c@193.70.33.64:18256,471518432477e31ea348af246c0b54095d41352c@134.65.195.144:26656,5a111b281852be31838ecf1202e59981e618355e@89.116.31.95:18256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quasarnode/config/config.toml
```
