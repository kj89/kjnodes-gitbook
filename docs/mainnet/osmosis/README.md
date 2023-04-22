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
peers="bfc50a343de219d5cd744a81dab8f83911c076e5@65.109.90.96:26656,616327f7ca045fb57827683e471ca472a232ef1f@89.33.8.233:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,a8a72dce31fdd36db889b1203d9af5fb7155e4d3@65.108.122.246:26686,807eda3abecff79df294d127cf58d6d5e07393ee@67.209.54.21:26656,b37a3c92c039de2582edd120b16afa3f462ecf3e@23.88.69.22:27166,f024eadf265f72f4240e5e3ea20eac22f6695ccb@159.65.100.92:26656,747d01891a83d6f759d88f9be07159c268b584b0@141.95.65.98:26656,23d67702fc76a2f3b3f3b74876727934843cff94@195.14.6.2:26656,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,a50c8dcd0e83032b5e29d5c5beef6e54ddafb508@35.83.253.164:26656,ef573bd8b519f9572798444f6c229ab0a3204bb8@5.9.94.24:26656,34340a9151d4a97a850d2cd64d8778279faf3f96@194.163.181.100:26656,b6ec9c7284b45eb912b01c192f7ffd8ef7508ec7@51.81.123.33:26656,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,6e9b0cf3ea78a9a540c75a4cfeb0c6a54b73fee4@65.108.127.166:26656,3226b67b2bb9da41b633392a785e87e8f6749939@162.55.245.149:12000,7f36123a395e902deaecf63bdaf5656bbb209623@15.204.52.75:26656,bcef965764a0d6bc15f1476c18133d52d0ff14b6@149.202.72.166:26624,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,f96947493f1edd08058afaeaef8f5830cc70b8f2@15.204.197.10:26656,5bda7b3070d62b4ddbea815e8bea6c6e9548d17d@65.108.140.115:26656,74e8ba742d8312c250f3237c8c8f3f951c01f9df@95.216.4.104:26656,3e874613919a6f8b3fc26071fef563c88f031b3c@116.202.236.59:31656,83a58da0e2ea2abe5a605cdc7194d92a086c2155@161.35.199.182:26656,8a6d1179752c44d6cee9a900bbe88956486dd724@139.180.185.11:26856,65f51ebf46256d829ae5903e9faf31dae35bdf46@65.109.64.245:26656,d011c34ee72767d7a33d94b79ef158eb49c9a7bf@164.92.70.57:31316,ab4ea418db1c65c2517975988e2f35891637ff4a@185.111.159.235:2000"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
