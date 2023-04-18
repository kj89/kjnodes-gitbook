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
peers="569aac51b04607a18696c63035586816dec85511@157.90.213.235:26656,b37a3c92c039de2582edd120b16afa3f462ecf3e@23.88.69.22:27166,5696d9806c883beb725fb469d90039d921107b5b@116.202.209.186:26656,d0d4b88110767c503baa8a618cfd7e284482f8dc@37.120.245.11:26656,50491afd6cb3910f94ccbf7190ac32f693e76d5b@185.216.179.86:26656,ef573bd8b519f9572798444f6c229ab0a3204bb8@5.9.94.24:26656,f860ee99ef34f10155065a97e95da07f712f1d6b@116.202.169.6:26666,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,807eda3abecff79df294d127cf58d6d5e07393ee@67.209.54.21:26656,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,913e9db0332df1152e5afe032ab81bdb65e3f91c@110.11.23.44:26656,3226b67b2bb9da41b633392a785e87e8f6749939@162.55.245.149:12000,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,7fc90a9c32c775ff685798c33fc06fe6d5009b26@202.61.229.102:26656,3d311ac374e6953e97ee07c74a76f399394c3025@173.215.85.171:20000,a50c8dcd0e83032b5e29d5c5beef6e54ddafb508@35.83.253.164:26656,65f51ebf46256d829ae5903e9faf31dae35bdf46@65.109.64.245:26656,170e681516b039be361df87eb626ee81c08f07a4@157.245.115.42:26656,d4e6a9d74abbf4676c8fd2d58d27fc24b59056b9@143.198.22.206:26656,4cccbb26639559c39f44758d246c5ed928f7717f@176.9.19.66:26656,e17c0a849eb239acd9f08ba396dec0db149b6ffc@185.255.131.77:26656,88fa3de90d06422b409ce6beb2367b94b2a1759e@51.79.17.73:26656,34340a9151d4a97a850d2cd64d8778279faf3f96@194.163.181.100:26656,6acf893525c9c43dee575dc23fcab3aa1523ea87@74.118.136.232:26656,2cb8dd6195c65458e3c18505bb70ce2ff624f85c@89.58.61.223:2000,75bae7b2af60155b6687ca3e5f92010d35cb0c12@54.164.100.216:26656,3e874613919a6f8b3fc26071fef563c88f031b3c@116.202.236.59:31656,ebc272824924ea1a27ea3183dd0b9ba713494f83@178.211.139.77:26716,f96947493f1edd08058afaeaef8f5830cc70b8f2@15.204.197.10:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
