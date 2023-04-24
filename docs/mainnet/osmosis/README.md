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
peers="4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,170e681516b039be361df87eb626ee81c08f07a4@157.245.115.42:26656,f024eadf265f72f4240e5e3ea20eac22f6695ccb@159.65.100.92:26656,32e9d4a7413dd5393c8be004bee68dea683be839@65.21.227.95:2004,c7fb97358712f447ca0689e814fe8c965a71b314@65.21.133.114:26656,807eda3abecff79df294d127cf58d6d5e07393ee@67.209.54.21:26656,9379a49cadb2e71d896c2d4ebd5ca394e50bf983@18.116.211.23:26656,a50c8dcd0e83032b5e29d5c5beef6e54ddafb508@35.83.253.164:26656,3d311ac374e6953e97ee07c74a76f399394c3025@173.215.85.171:20000,af678c610cf37bf5d443efdba7ac1354f104415c@137.184.9.18:32644,65f51ebf46256d829ae5903e9faf31dae35bdf46@65.109.64.245:26656,34340a9151d4a97a850d2cd64d8778279faf3f96@194.163.181.100:26656,6cbb199c891bf1ed925c64fd1ec0882afdc2e2dc@162.19.81.54:34656,7f36123a395e902deaecf63bdaf5656bbb209623@15.204.52.75:26656,ef573bd8b519f9572798444f6c229ab0a3204bb8@5.9.94.24:26656,23d67702fc76a2f3b3f3b74876727934843cff94@195.14.6.2:26656,1c398af2208984d4e59bc41132e3eac0508abb0f@95.216.76.251:26656,74e8ba742d8312c250f3237c8c8f3f951c01f9df@95.216.4.104:26656,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,3226b67b2bb9da41b633392a785e87e8f6749939@162.55.245.149:12000,406f64a8d601e34d7311fd61ec87b0c7028bd230@138.201.23.39:46656,a5d0842d58c0fdd4ed10a39fd9c897cd168906d2@65.21.195.98:26706,bfcbd83f2ecfc2e839b246a001e355079e66f0fd@24.199.110.108:30799,31d2c86f7957e2db91297e54c3b0456ea06c2250@173.67.177.115:26656,b6ec9c7284b45eb912b01c192f7ffd8ef7508ec7@51.81.123.33:26656,c5358545d951ae666c695903036c1e93578951eb@135.181.176.113:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,071ae914b06e14148a6286a0fa087c797336f043@34.105.246.121:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,c5afa50cac6814f16facafb0c680871ebd62482d@184.105.162.166:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
