# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cosmoshub.png" alt=""><figcaption></figcaption></figure>

The Cosmos Hub is the blockchain protocol underlying an  increasingly large number of blockchains built on the  Cosmos Network, allowing them to communicate with each other.

**Chain ID**: cosmoshub-4 | **Latest Version Tag**: v10.0.0 | **Wasm**: OFF

[Website](https://hub.cosmos.network) | [Discord](https://discord.gg/cosmosnetwork) | [Twitter](https://twitter.com/cosmoshub)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/cosmoshub](https://explorer.kjnodes.com/cosmoshub)

## Public endpoints

* api: [https://cosmoshub.api.kjnodes.com](https://cosmoshub.api.kjnodes.com)
* rpc: [https://cosmoshub.rpc.kjnodes.com](https://cosmoshub.rpc.kjnodes.com)
* grpc: cosmoshub.grpc.kjnodes.com:13490

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@cosmoshub.rpc.kjnodes.com:13456
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@cosmoshub.rpc.kjnodes.com:13459
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/cosmoshub/addrbook.json > $HOME/.gaia/config/addrbook.json
```

**live-peers** (10)
```bash
peers="a3f378a0fd7174496f8238d6b6d73e87e94d4106@34.86.248.3:26656,36515aac2a928e227e7dc793a548b35b54bec974@45.63.82.80:26656,cf52e109b7015d5c21f50ab4331fb7062160ab6c@35.206.171.231:26656,ca5011c44fd74d95e7fca487c69e301df195750c@65.108.122.246:26726,72829b78b38408b03793ed389b9f16596b82c306@146.59.81.92:26656,81062b9a8807a1229543b84bae2898c50a1b1dfc@52.211.169.132:26656,322efd4fdc72a189a2fc8b2b597927831df2bbed@128.0.51.9:26656,3da88430414ec9084c8983fe4d462cce655ff1f3@51.222.245.114:26656,8698cb819c9a4503fe2c71055f1380d08edc5adf@204.16.244.116:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13456"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gaia/config/config.toml
```
