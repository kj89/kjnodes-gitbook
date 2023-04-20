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
peers="e613079d9b1c1c688963215a975cc9b29722f4fb@65.108.238.103:12556,2f4c0337b2522034a614a5cb2c61a891fe753c03@5.9.81.187:29656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,807eda3abecff79df294d127cf58d6d5e07393ee@67.209.54.21:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,6e9b0cf3ea78a9a540c75a4cfeb0c6a54b73fee4@65.108.127.166:26656,6acf893525c9c43dee575dc23fcab3aa1523ea87@74.118.136.232:26656,34340a9151d4a97a850d2cd64d8778279faf3f96@194.163.181.100:26656,4cccbb26639559c39f44758d246c5ed928f7717f@176.9.19.66:26656,77bb5fb9b6964d6e861e91c1d55cf82b67d838b5@35.212.77.47:26656,fc590afe489a1b9ca8ff3f2fb396dbc20b1997a4@204.16.244.254:26656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,75bae7b2af60155b6687ca3e5f92010d35cb0c12@54.164.100.216:26656,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,ef573bd8b519f9572798444f6c229ab0a3204bb8@5.9.94.24:26656,65f51ebf46256d829ae5903e9faf31dae35bdf46@65.109.64.245:26656,7fc90a9c32c775ff685798c33fc06fe6d5009b26@202.61.229.102:26656,c5afa50cac6814f16facafb0c680871ebd62482d@184.105.162.166:26656,747d01891a83d6f759d88f9be07159c268b584b0@141.95.65.98:26656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,b6ec9c7284b45eb912b01c192f7ffd8ef7508ec7@51.81.123.33:26656,3d311ac374e6953e97ee07c74a76f399394c3025@173.215.85.171:20000,024a615ea051461357046c00f67eac6300b03215@65.108.128.240:26656,23d67702fc76a2f3b3f3b74876727934843cff94@195.14.6.2:26656,c0c2c6ff9e456dc31c7f697c81168267dbb49339@34.83.112.45:26656,f3262b9f490720920b0002fadd500af1cef3e6a6@51.222.40.84:26656,cb0ad76ff7ec6488073a710e528d893892b9fe56@54.218.158.147:26656,8a41a35b9685a336380bc0fcd3fd4d4fc07b6101@8.218.7.106:26656,8c5e9342661a728b810d82221152b2a2fce5018a@162.19.84.205:26656,9f2df25f380a7e67a92c3dc5e7c33c08555b30dc@5.9.108.19:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
