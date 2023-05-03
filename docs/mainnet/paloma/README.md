# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/paloma.png" alt=""><figcaption></figcaption></figure>

Paloma is a fast, permissionless, Cosmos-SDK blockchain that  moves messages securely, between any other blockchains.

**Chain ID**: messenger | **Latest Version Tag**: v0.11.6 | **Wasm**: ON

[Website](https://www.palomachain.com) | [Discord](https://discord.gg/tKVFpfdSw4) | [Twitter](https://twitter.com/paloma_chain)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/paloma](https://explorer.kjnodes.com/paloma)

## Public endpoints

* api: [https://paloma.api.kjnodes.com](https://paloma.api.kjnodes.com)
* rpc: [https://paloma.rpc.kjnodes.com](https://paloma.rpc.kjnodes.com)
* grpc: paloma.grpc.kjnodes.com:11090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@paloma.rpc.kjnodes.com:11056
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@paloma.rpc.kjnodes.com:11059
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/paloma/addrbook.json > $HOME/.paloma/config/addrbook.json
```

**live-peers** (16)
```bash
peers="08c242d4505c5db223647069fdc0acb6e90079aa@65.109.106.214:26656,8ed8cddfac504d986a2c6545def0e57b2c6aa5db@65.109.106.172:38656,1a0232b9426aa1c7a78c92a2136b69d050bb6942@65.108.224.126:26656,471a09da6fafb67bff3aa1f01e00fd1830e53262@136.243.94.138:26656,8af8dfa817359036f55f6793b0ed4bcce8884027@85.14.245.70:26656,b244dfc19293103040d4bdad359534d0990a9070@45.140.185.181:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:10656,41a47bae18f81c1f626e4b238221b77e274424d7@45.33.65.223:26656,b92c94f00b46500a5ff8920acd438c0873c2f9da@50.116.13.101:26656,2c6772b11c1f9eff2a923eb2bf808543cdd501c5@79.143.179.196:26656,87b4221770495e66e772a53bbea92a15aff288c2@144.126.158.0:26656,ab6875bd52d6493f39612eb5dff57ced1e3a5ad6@95.217.229.18:10656,f4c43099e04b721c54a454dad85f61da49be90bc@65.108.199.222:28656,7eae755c119f538e0dc99f3c37289de628bc9526@209.182.239.169:26656,d73f7f6de427369a60245725047f49b1fd0e0a2f@65.108.199.26:31656,4a0b3275453e3a12fca3214268ac865689c90a8e@135.181.76.35:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.paloma/config/config.toml
```
