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
peers="f9bfc7f25f63bd7e392fbe5465126b311465cbce@65.108.78.186:26656,f9a920a61ee994b12b77178dd5f1fc1ed39b7cd2@142.132.255.49:26656,95dbddda671081fb433871fa612ff5291242d93d@45.67.221.200:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,e153cc49052d67280dfdd6d660f3d98622905850@209.133.193.74:26656,d4e6a9d74abbf4676c8fd2d58d27fc24b59056b9@143.198.22.206:26656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,c5afa50cac6814f16facafb0c680871ebd62482d@184.105.162.166:26656,807eda3abecff79df294d127cf58d6d5e07393ee@67.209.54.21:26656,75bae7b2af60155b6687ca3e5f92010d35cb0c12@54.164.100.216:26656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,406f64a8d601e34d7311fd61ec87b0c7028bd230@138.201.23.39:46656,a50c8dcd0e83032b5e29d5c5beef6e54ddafb508@35.83.253.164:26656,4cccbb26639559c39f44758d246c5ed928f7717f@176.9.19.66:26656,c0c2c6ff9e456dc31c7f697c81168267dbb49339@34.83.112.45:26656,3226b67b2bb9da41b633392a785e87e8f6749939@162.55.245.149:12000,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,7fc90a9c32c775ff685798c33fc06fe6d5009b26@202.61.229.102:26656,a8a72dce31fdd36db889b1203d9af5fb7155e4d3@65.108.122.246:26686,ef573bd8b519f9572798444f6c229ab0a3204bb8@5.9.94.24:26656,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,3d311ac374e6953e97ee07c74a76f399394c3025@173.215.85.171:20000,747d01891a83d6f759d88f9be07159c268b584b0@141.95.65.98:26656,65f51ebf46256d829ae5903e9faf31dae35bdf46@65.109.64.245:26656,5696d9806c883beb725fb469d90039d921107b5b@116.202.209.186:26656,729219c108c059824ea9a17c09d11adc99226db4@66.172.36.139:36656,f3262b9f490720920b0002fadd500af1cef3e6a6@51.222.40.84:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,59fcef11ce153980b8e7431e8285f2bb8de1d121@195.14.6.2:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
