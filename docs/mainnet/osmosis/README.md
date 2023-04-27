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

**live-peers** (29)
```bash
peers="4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,23d67702fc76a2f3b3f3b74876727934843cff94@195.14.6.2:26656,ab4ea418db1c65c2517975988e2f35891637ff4a@185.111.159.235:2000,807eda3abecff79df294d127cf58d6d5e07393ee@67.209.54.21:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,9203fbde463bd66bb451da3de390c7d3515c2bf2@65.108.46.248:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.71:26656,253bc0e57f48cb4f70493e6109b756208e20e8fe@135.181.171.121:26656,3e874613919a6f8b3fc26071fef563c88f031b3c@116.202.236.59:31656,a5ce326c6a5b78ef57d5121825e041a3cba94146@142.132.202.98:26656,3e3f8f3a9ed941600550d090900aee639abb7906@93.159.134.158:56656,914865f0b02d76c48c5369457cf5aa4173d06ed8@54.169.236.90:26656,d0c050f33b7aa1032a3763da0e7eb8df0ac72a2c@162.55.92.114:12000,af678c610cf37bf5d443efdba7ac1354f104415c@137.184.9.18:32644,170e681516b039be361df87eb626ee81c08f07a4@157.245.115.42:26656,2c400fa54e9d7aa5b65a6b16d34a05c5b39aab99@130.61.42.243:26656,b6ec9c7284b45eb912b01c192f7ffd8ef7508ec7@51.81.123.33:26656,ef573bd8b519f9572798444f6c229ab0a3204bb8@5.9.94.24:26656,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,13d17adf418ceab5528096dcacf130830fee2b86@35.215.50.201:26656,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,65f51ebf46256d829ae5903e9faf31dae35bdf46@65.109.64.245:26656,b69e57cd6f796ac5d6efb1a834163365c37cbfa8@78.46.69.29:26656,d4e6a9d74abbf4676c8fd2d58d27fc24b59056b9@143.198.22.206:26656,3d311ac374e6953e97ee07c74a76f399394c3025@173.215.85.171:20000,c5afa50cac6814f16facafb0c680871ebd62482d@184.105.162.166:26656,bfcbd83f2ecfc2e839b246a001e355079e66f0fd@24.199.110.108:30799,1990bfb9135023ca697bbb8a8d0defb6e4669478@211.219.19.74:26656,7b9c493b17a55beaa61d635edc167f58c77be141@23.88.44.37:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
