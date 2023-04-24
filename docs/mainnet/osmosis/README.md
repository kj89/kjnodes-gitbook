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
peers="5696d9806c883beb725fb469d90039d921107b5b@116.202.209.186:26656,980b15331dece2aa8020c1800b9c00ddb273c872@138.201.32.103:30656,e726816f42831689eab9378d5d577f1d06d25716@23.88.22.10:26656,31d2c86f7957e2db91297e54c3b0456ea06c2250@173.67.177.115:26656,807eda3abecff79df294d127cf58d6d5e07393ee@67.209.54.21:26656,af678c610cf37bf5d443efdba7ac1354f104415c@137.184.9.18:32644,2c400fa54e9d7aa5b65a6b16d34a05c5b39aab99@130.61.42.243:26656,3226b67b2bb9da41b633392a785e87e8f6749939@162.55.245.149:12000,ef573bd8b519f9572798444f6c229ab0a3204bb8@5.9.94.24:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.71:26656,95dbddda671081fb433871fa612ff5291242d93d@45.67.221.200:26656,b6ec9c7284b45eb912b01c192f7ffd8ef7508ec7@51.81.123.33:26656,1c398af2208984d4e59bc41132e3eac0508abb0f@95.216.76.251:26656,3d311ac374e6953e97ee07c74a76f399394c3025@173.215.85.171:20000,747d01891a83d6f759d88f9be07159c268b584b0@141.95.65.98:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,07db7d141686559045bfd4f39feff5ecf5f57f15@141.164.55.118:10001,23d67702fc76a2f3b3f3b74876727934843cff94@195.14.6.2:26656,7fc90a9c32c775ff685798c33fc06fe6d5009b26@202.61.229.102:26656,74e8ba742d8312c250f3237c8c8f3f951c01f9df@95.216.4.104:26656,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,65f51ebf46256d829ae5903e9faf31dae35bdf46@65.109.64.245:26656,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,a50c8dcd0e83032b5e29d5c5beef6e54ddafb508@35.83.253.164:26656,9379a49cadb2e71d896c2d4ebd5ca394e50bf983@18.116.211.23:26656,34340a9151d4a97a850d2cd64d8778279faf3f96@194.163.181.100:26656,3e874613919a6f8b3fc26071fef563c88f031b3c@116.202.236.59:31656,6cbb7b7bddf723a28925fae2c19eb7be41ef687c@34.71.161.134:26656,bcef965764a0d6bc15f1476c18133d52d0ff14b6@149.202.72.166:26624"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
