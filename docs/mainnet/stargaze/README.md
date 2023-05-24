# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/stargaze.png" alt=""><figcaption></figcaption></figure>

Stargaze is a Cosmos zone (layer 1 proof-of-stake blockchain).  It is the base layer node software for the Stargaze NFT Marketplace.

**Chain ID**: stargaze-1 | **Latest Version Tag**: v9.0.0 | **Wasm**: ON

[Website](https://www.stargaze.zone) | [Discord](https://discord.gg/stargaze) | [Twitter](https://twitter.com/stargazezone)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/stargaze](https://explorer.kjnodes.com/stargaze)

## Public endpoints

* api: [https://stargaze.api.kjnodes.com](https://stargaze.api.kjnodes.com)
* rpc: [https://stargaze.rpc.kjnodes.com](https://stargaze.rpc.kjnodes.com)
* grpc: stargaze.grpc.kjnodes.com:15890

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@stargaze.rpc.kjnodes.com:15856
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@stargaze.rpc.kjnodes.com:15859
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/stargaze/addrbook.json > $HOME/.starsd/config/addrbook.json
```

**live-peers** (10)
```bash
peers="b99beb75e753224b2cf6b3dd8db48b47047c56f6@135.181.162.122:26656,bb5a32a9301b06cd4f30c0e45ca023213c95e9f6@213.133.111.71:36656,f5fa74f9a41b3d71f29a95cb1c90717e193a337d@23.111.163.2:26656,56a776a589fbc4d038db956791bcf75204c67872@172.105.112.35:26656,02826a9d7da27fbaf869544a108218859106c7b1@65.108.77.98:26656,0a935dd56157e719e704bc46633faf6ef0d52f11@51.159.109.243:21103,22a5266cb18ea209d3725e561bd9d2d27ee81d50@195.3.223.96:26656,c565abfb2686a51764dca1bacb5280098dda06a5@65.21.236.33:26656,fc668bbf7e34d6926308487348b2655159198f1d@135.181.128.114:13756,1c3e1cafb4d3e9edeb37fc964e98ed1ae8bda6ee@144.76.223.202:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
