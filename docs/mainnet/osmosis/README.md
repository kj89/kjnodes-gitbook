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
peers="7f36123a395e902deaecf63bdaf5656bbb209623@15.204.52.75:26656,406f64a8d601e34d7311fd61ec87b0c7028bd230@138.201.23.39:46656,5696d9806c883beb725fb469d90039d921107b5b@116.202.209.186:26656,d4e6a9d74abbf4676c8fd2d58d27fc24b59056b9@143.198.22.206:26656,6b1dd134b30aeaeb2f21f33bd2cd0370a2275501@138.68.6.165:26656,a50c8dcd0e83032b5e29d5c5beef6e54ddafb508@35.83.253.164:26656,cb0ad76ff7ec6488073a710e528d893892b9fe56@54.218.158.147:26656,024a615ea051461357046c00f67eac6300b03215@65.108.128.240:26656,535b442ab48c404f217cb4e78500be068a35e4e9@51.89.219.185:26656,747d01891a83d6f759d88f9be07159c268b584b0@141.95.65.98:26656,34340a9151d4a97a850d2cd64d8778279faf3f96@194.163.181.100:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,c61bf85fd330bb702b1f13f58dd3cf83c5363bf2@149.56.26.22:26656,b6ec9c7284b45eb912b01c192f7ffd8ef7508ec7@51.81.123.33:26656,3226b67b2bb9da41b633392a785e87e8f6749939@162.55.245.149:12000,8c5e9342661a728b810d82221152b2a2fce5018a@162.19.84.205:26656,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,3d311ac374e6953e97ee07c74a76f399394c3025@173.215.85.171:20000,f96947493f1edd08058afaeaef8f5830cc70b8f2@15.204.197.10:26656,807eda3abecff79df294d127cf58d6d5e07393ee@67.209.54.21:26656,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,2048e1bc1f020fa210fb475e7a0ec0948919609f@185.217.125.64:26656,31d2c86f7957e2db91297e54c3b0456ea06c2250@173.67.177.115:26656,65f51ebf46256d829ae5903e9faf31dae35bdf46@65.109.64.245:26656,ef573bd8b519f9572798444f6c229ab0a3204bb8@5.9.94.24:26656,2904827f3ffa642bf7122d65cef27e1ab40a7346@35.74.104.174:16656,42f42a4b3527b927d5002d45abd37f66ecdd4861@51.178.74.75:16656,23d67702fc76a2f3b3f3b74876727934843cff94@195.14.6.2:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,7fc90a9c32c775ff685798c33fc06fe6d5009b26@202.61.229.102:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
