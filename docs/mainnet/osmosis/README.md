# Services

[installation](./installation/ "mention") [upgrade](./upgrade/ "mention") [snapshot](./snapshot/ "mention") [state-sync](./state-sync/ "mention") [useful-commands](./useful-commands/ "mention")

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
peers="65f51ebf46256d829ae5903e9faf31dae35bdf46@65.109.64.245:26656,b6ec9c7284b45eb912b01c192f7ffd8ef7508ec7@51.81.123.33:26656,6e9b0cf3ea78a9a540c75a4cfeb0c6a54b73fee4@65.108.127.166:26656,31d2c86f7957e2db91297e54c3b0456ea06c2250@173.67.177.115:26656,e0f3b604f1df9bf6590c4cc09fee1e28f46b0b39@65.109.28.226:15656,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,af678c610cf37bf5d443efdba7ac1354f104415c@137.184.9.18:32644,5696d9806c883beb725fb469d90039d921107b5b@116.202.209.186:26656,7fc90a9c32c775ff685798c33fc06fe6d5009b26@202.61.229.102:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,23d67702fc76a2f3b3f3b74876727934843cff94@195.14.6.2:26656,c5afa50cac6814f16facafb0c680871ebd62482d@184.105.162.166:26656,1990bfb9135023ca697bbb8a8d0defb6e4669478@211.219.19.74:26656,94e69330d6f4cfe221cdd2ce49ee141e53e5f200@23.106.120.6:26656,54b56ff565527b20f21af5a8e8744a7b2ef35c0a@54.150.227.110:26656,ef573bd8b519f9572798444f6c229ab0a3204bb8@5.9.94.24:26656,34340a9151d4a97a850d2cd64d8778279faf3f96@194.163.181.100:26656,677ef9606ea18a13b5dbfad19493d99d7ea068f5@149.56.24.130:26656,3d311ac374e6953e97ee07c74a76f399394c3025@173.215.85.171:20000,12910da249bcee4cdafbef938b10b51c94c0057e@5.9.142.165:26656,c61bf85fd330bb702b1f13f58dd3cf83c5363bf2@149.56.26.22:26656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@23.88.21.234:26656,a427a6c73e65ad4aa5acdee633afabeb8f473603@65.109.116.204:10156,f666123ff189fdc2cf26186e2910b9b3fedf08bf@135.181.223.115:2000,807eda3abecff79df294d127cf58d6d5e07393ee@67.209.54.21:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,a50c8dcd0e83032b5e29d5c5beef6e54ddafb508@35.83.253.164:26656,f9bfc7f25f63bd7e392fbe5465126b311465cbce@65.108.78.186:26656,9203fbde463bd66bb451da3de390c7d3515c2bf2@65.108.46.248:26656,74e8ba742d8312c250f3237c8c8f3f951c01f9df@95.216.4.104:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
