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

**live-peers** (30)
```bash
peers="6e9b0cf3ea78a9a540c75a4cfeb0c6a54b73fee4@65.108.127.166:26656,31d2c86f7957e2db91297e54c3b0456ea06c2250@173.67.177.115:26656,f3262b9f490720920b0002fadd500af1cef3e6a6@51.222.40.84:26656,6b1dd134b30aeaeb2f21f33bd2cd0370a2275501@138.68.6.165:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,807eda3abecff79df294d127cf58d6d5e07393ee@67.209.54.21:26656,4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,253bc0e57f48cb4f70493e6109b756208e20e8fe@135.181.171.121:26656,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,f666123ff189fdc2cf26186e2910b9b3fedf08bf@135.181.223.115:2000,d0c050f33b7aa1032a3763da0e7eb8df0ac72a2c@162.55.92.114:12000,7fc90a9c32c775ff685798c33fc06fe6d5009b26@202.61.229.102:26656,afdedf1dff1e0d1e06036dd28dfe1633ec4204b9@3.217.47.126:26656,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,13d17adf418ceab5528096dcacf130830fee2b86@35.215.50.201:26656,b6ec9c7284b45eb912b01c192f7ffd8ef7508ec7@51.81.123.33:26656,ef573bd8b519f9572798444f6c229ab0a3204bb8@5.9.94.24:26656,74e8ba742d8312c250f3237c8c8f3f951c01f9df@95.216.4.104:26656,e4485f292ae0ed3c3998873cb25fa6eda4af4ea4@207.148.88.210:26656,65f51ebf46256d829ae5903e9faf31dae35bdf46@65.109.64.245:26656,a8a72dce31fdd36db889b1203d9af5fb7155e4d3@65.108.122.246:26686,2ff9bc1740a721a9baeda01abee181997bb65568@142.132.140.20:26656,e0f3b604f1df9bf6590c4cc09fee1e28f46b0b39@65.109.28.226:15656,ebc272824924ea1a27ea3183dd0b9ba713494f83@178.211.139.77:26716,913e9db0332df1152e5afe032ab81bdb65e3f91c@110.11.23.44:26656,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,a5ce326c6a5b78ef57d5121825e041a3cba94146@142.132.202.98:26656,26865e31c6aa6de9cbf887c1111d36205baa7665@164.90.158.138:26656,b69e57cd6f796ac5d6efb1a834163365c37cbfa8@78.46.69.29:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
