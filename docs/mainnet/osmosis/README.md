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
peers="9363737697cfab7113b44f8596783c4a137b1564@65.108.111.200:26656,6937a77273960a68f7d9bcbf47b55ed2d84940fb@167.235.211.87:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,bfc50a343de219d5cd744a81dab8f83911c076e5@65.109.90.96:26656,2cb8dd6195c65458e3c18505bb70ce2ff624f85c@89.58.61.223:2000,a50c8dcd0e83032b5e29d5c5beef6e54ddafb508@35.83.253.164:26656,12910da249bcee4cdafbef938b10b51c94c0057e@5.9.142.165:26656,cb0ad76ff7ec6488073a710e528d893892b9fe56@54.218.158.147:26656,f96947493f1edd08058afaeaef8f5830cc70b8f2@15.204.197.10:26656,1c398af2208984d4e59bc41132e3eac0508abb0f@95.216.76.251:26656,4cccbb26639559c39f44758d246c5ed928f7717f@176.9.19.66:26656,42f42a4b3527b927d5002d45abd37f66ecdd4861@51.178.74.75:16656,f666123ff189fdc2cf26186e2910b9b3fedf08bf@135.181.223.115:2000,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,7fc90a9c32c775ff685798c33fc06fe6d5009b26@202.61.229.102:26656,1a4706c2194cbc055adf4eb89a7b24493bcf33f8@15.235.9.22:26656,1990bfb9135023ca697bbb8a8d0defb6e4669478@211.219.19.74:26656,88fa3de90d06422b409ce6beb2367b94b2a1759e@51.79.17.73:26656,31d2c86f7957e2db91297e54c3b0456ea06c2250@173.67.177.115:26656,f9a920a61ee994b12b77178dd5f1fc1ed39b7cd2@142.132.255.49:26656,061a556e723575e576958ae4905eddfff7d5add2@176.9.62.180:26656,1c02ae0be21e3b08d9beadf91c26aec4193d2659@135.181.22.238:26656,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,3226b67b2bb9da41b633392a785e87e8f6749939@162.55.245.149:12000,33cf290cc0cfec8c59e6af86f1a5579303d21087@138.68.14.64:26656,c5afa50cac6814f16facafb0c680871ebd62482d@184.105.162.166:26656,7f36123a395e902deaecf63bdaf5656bbb209623@15.204.52.75:26656,2def96b97cab65a6a35f871f0ab3c384a1176869@35.210.137.157:26656,c61bf85fd330bb702b1f13f58dd3cf83c5363bf2@149.56.26.22:26656,ab4ea418db1c65c2517975988e2f35891637ff4a@185.111.159.235:2000"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
