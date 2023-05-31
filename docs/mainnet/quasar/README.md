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
peers="a40e1d5f63fad9e14edb9c95458b27f3c1de858c@116.203.236.246:26618,d7ea38275af96271fd66194dad3951ef38b8ba7c@193.70.33.64:18256,bbf8c1562c20726a436f1c1476ad49e560ca179b@51.89.190.33:26656,471518432477e31ea348af246c0b54095d41352c@134.65.195.144:26656,6f9e244b6e225241c02b235f700c2b0788da982d@148.113.159.22:18256,0f7eca0da978e4304bb81fa1b9d9a1c87c57f45d@38.146.3.147:18256,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14856,a286b35c9e9626cc7b780120ebe4afa883c059ce@144.76.40.53:18256,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.193.11:26656,4e1c2471efb89239fb04a4b75f9f87177fd91d00@164.152.162.218:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quasarnode/config/config.toml
```
