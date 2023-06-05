# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/osmosis.png" alt=""><figcaption></figcaption></figure>

Osmosis is a DEX protocol, which means it uses smart contracts  to determine the price of digital assets, to produce liquidity  via a peer-to-peer (P2P) methodology, and to exact trades between users

**Chain ID**: osmosis-1 | **Latest Version Tag**: v15.0.0 | **Wasm**: ON

[Website](https://osmosis.zone) | [Discord](https://discord.gg/osmosis) | [Twitter](https://twitter.com/osmosiszone)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/osmosis](https://explorer.kjnodes.com/osmosis)

## Public endpoints

* api: [https://osmosis.api.kjnodes.com](https://osmosis.api.kjnodes.com)
* rpc: [https://osmosis.rpc.kjnodes.com](https://osmosis.rpc.kjnodes.com)
* grpc: osmosis.grpc.kjnodes.com:12990

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@osmosis.rpc.kjnodes.com:12956
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@osmosis.rpc.kjnodes.com:12959
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/osmosis/addrbook.json > $HOME/.osmosisd/config/addrbook.json
```

**live-peers** (10)
```bash
peers="c124ce0b508e8b9ed1c5b6957f362225659b5343@169.155.169.186:26656,9f2df25f380a7e67a92c3dc5e7c33c08555b30dc@5.9.108.19:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,406f64a8d601e34d7311fd61ec87b0c7028bd230@138.201.23.39:46656,d4e6a9d74abbf4676c8fd2d58d27fc24b59056b9@143.198.22.206:26656,a8a72dce31fdd36db889b1203d9af5fb7155e4d3@65.108.122.246:26686,980b15331dece2aa8020c1800b9c00ddb273c872@138.201.32.103:30656,2f4c0337b2522034a614a5cb2c61a891fe753c03@5.9.81.187:29656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:12956,ab4ea418db1c65c2517975988e2f35891637ff4a@185.111.159.235:2000"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
