# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cosmoshub.png" alt=""><figcaption></figcaption></figure>

The Cosmos Hub is the blockchain protocol underlying an  increasingly large number of blockchains built on the  Cosmos Network, allowing them to communicate with each other.

**Chain ID**: cosmoshub-4 | **Latest Version Tag**: v9.0.0 | **Wasm**: OFF

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

**live-peers** (8)
```bash
peers="aa61bc0e8a42eda6ac1276c4279941714a4a38f4@88.99.70.38:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13456,6feb3dd7c139294fc4c5c721efb5ca452f7ed177@88.198.198.158:14956,8918eaded204a6f948a0f4a158568c57b2ef1895@47.90.133.13:26656,1733aef88702bd8326bea0e1dc403d3dbb6f5d8a@158.247.202.33:26656,7abab0475a506ed3b9ab2ad40948bfe53b797e13@128.199.128.15:26090,b6b9bc1a0c18d12be759111bb3a0d9a8958120c7@57.128.20.184:26656,3da88430414ec9084c8983fe4d462cce655ff1f3@51.222.245.114:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gaia/config/config.toml
```
