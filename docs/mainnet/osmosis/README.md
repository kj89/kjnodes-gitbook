# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/osmosis.png" width="150" alt=""><figcaption></figcaption></figure>

Osmosis is a DEX protocol, which means it uses smart contracts  to determine the price of digital assets, to produce liquidity  via a peer-to-peer (P2P) methodology, and to exact trades between users

**Chain ID**: osmosis-1 | **Latest Version Tag**: v15.0.0 | **Wasm**: ON

[Website](https://osmosis.zone) | [Discord](https://discord.gg/osmosis) | [Twitter](https://twitter.com/osmosiszone)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/osmosis](https://explorer.kjnodes.com/osmosis)

## Public endpoints

* api: [https://osmosis.api.kjnodes.com](https://osmosis.api.kjnodes.com)
* rpc: [https://osmosis.rpc.kjnodes.com](https://osmosis.rpc.kjnodes.com)
* grpc: osmosis.grpc.kjnodes.com:29090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@osmosis.rpc.kjnodes.com:29656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@osmosis.rpc.kjnodes.com:29659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/osmosis/addrbook.json > $HOME/.osmosisd/config/addrbook.json
```

**live-peers** (30)
```bash
peers="c5358545d951ae666c695903036c1e93578951eb@135.181.176.113:26656,7fc90a9c32c775ff685798c33fc06fe6d5009b26@202.61.229.102:26656,406f64a8d601e34d7311fd61ec87b0c7028bd230@138.201.23.39:46656,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,1c398af2208984d4e59bc41132e3eac0508abb0f@95.216.76.251:26656,07db7d141686559045bfd4f39feff5ecf5f57f15@141.164.55.118:10001,34340a9151d4a97a850d2cd64d8778279faf3f96@194.163.181.100:26656,e1f6d26b4686fab5a8a90c720231e36b26b173cf@65.109.55.186:50656,ec929701754be057fb38c824fc127e26add9c900@138.201.121.185:26666,23d67702fc76a2f3b3f3b74876727934843cff94@195.14.6.2:26656,747d01891a83d6f759d88f9be07159c268b584b0@141.95.65.98:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,95dbddda671081fb433871fa612ff5291242d93d@45.67.221.200:26656,0bb96aa57bc785dd71b65690f1efc9e8f1803548@164.90.144.186:32323,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,3226b67b2bb9da41b633392a785e87e8f6749939@162.55.245.149:12000,ebc272824924ea1a27ea3183dd0b9ba713494f83@178.211.139.77:26716,807eda3abecff79df294d127cf58d6d5e07393ee@67.209.54.21:26656,170e681516b039be361df87eb626ee81c08f07a4@157.245.115.42:26656,9379a49cadb2e71d896c2d4ebd5ca394e50bf983@18.116.211.23:26656,ef30bc7dbac63eb868e66bad497368f2cd0924e1@141.98.217.102:26656,3d311ac374e6953e97ee07c74a76f399394c3025@173.215.85.171:20000,677ef9606ea18a13b5dbfad19493d99d7ea068f5@149.56.24.130:26656,b6ec9c7284b45eb912b01c192f7ffd8ef7508ec7@51.81.123.33:26656,af678c610cf37bf5d443efdba7ac1354f104415c@137.184.9.18:32644,74e8ba742d8312c250f3237c8c8f3f951c01f9df@95.216.4.104:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,d557fd150f11883e93c23d8fcab19ef343db8096@35.215.38.241:26656,c7fb97358712f447ca0689e814fe8c965a71b314@65.21.133.114:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
