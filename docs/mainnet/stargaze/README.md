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
peers="fc668bbf7e34d6926308487348b2655159198f1d@135.181.128.114:13756,82d89abe4024c54b68b8d07887cbb7f3d0710f71@130.61.146.203:26656,6c7a904400f646e43eaf1ea76976de037392efa1@23.88.69.22:26566,1c3e1cafb4d3e9edeb37fc964e98ed1ae8bda6ee@144.76.223.202:26656,06805bbbb45dbbcdadb963fda7f5b3733f331ebe@185.119.118.109:3000,0a935dd56157e719e704bc46633faf6ef0d52f11@51.159.109.243:21103,9c948410d4a8483ada2dc4184fbc8f7121ed0c1a@51.89.7.185:26629,62378c0bfc79666d6f7fb17be2af6a4889e775e8@65.108.46.248:36656,c565abfb2686a51764dca1bacb5280098dda06a5@65.21.236.33:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
