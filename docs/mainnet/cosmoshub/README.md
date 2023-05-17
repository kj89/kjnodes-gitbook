# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cosmoshub.png" alt=""><figcaption></figcaption></figure>

The Cosmos Hub is the blockchain protocol underlying an  increasingly large number of blockchains built on the  Cosmos Network, allowing them to communicate with each other.

**Chain ID**: cosmoshub-4 | **Latest Version Tag**: v9.1.0 | **Wasm**: OFF

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

**live-peers** (9)
```bash
peers="d53ecee926a66a4a6b1858004f5f22f77faca036@3.69.52.20:26656,53b3651680ec3482d736808cbb3035940107f8ab@82.100.58.119:26656,d9dbd30f7e9ae99dc05645f48f4637c2f4a14645@34.107.9.71:26656,4ebf074e8b4a24438bd0bd503b62b4728dfb8eae@35.212.101.35:26656,e0ab6c5cc86959853f499236b8297344802ac5f4@5.161.139.201:26656,5d45bc48f6c0199c047e685fafb4309f53593f37@5.161.119.242:49656,c1e437f73b8889b78ea34981e7c349157ad80284@107.135.15.66:26656,f05ddce65f1e75babe01d05fef1bce5d8ffe0972@54.177.181.170:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13456"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gaia/config/config.toml
```
