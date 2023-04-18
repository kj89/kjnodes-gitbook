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
peers="c5358545d951ae666c695903036c1e93578951eb@135.181.176.113:26656,12910da249bcee4cdafbef938b10b51c94c0057e@5.9.142.165:26656,3e369738cb861a252e4836d553e982988e40a41b@15.235.53.45:2000,6b1dd134b30aeaeb2f21f33bd2cd0370a2275501@138.68.6.165:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,f1fe0a080d561d37a94bea6022cbc0972395a0f4@65.108.121.190:2000,c5afa50cac6814f16facafb0c680871ebd62482d@184.105.162.166:26656,34340a9151d4a97a850d2cd64d8778279faf3f96@194.163.181.100:26656,88fa3de90d06422b409ce6beb2367b94b2a1759e@51.79.17.73:26656,807eda3abecff79df294d127cf58d6d5e07393ee@67.209.54.21:26656,f860ee99ef34f10155065a97e95da07f712f1d6b@116.202.169.6:26666,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,75bae7b2af60155b6687ca3e5f92010d35cb0c12@54.164.100.216:26656,65f51ebf46256d829ae5903e9faf31dae35bdf46@65.109.64.245:26656,4cccbb26639559c39f44758d246c5ed928f7717f@176.9.19.66:26656,f96947493f1edd08058afaeaef8f5830cc70b8f2@15.204.197.10:26656,cb0ad76ff7ec6488073a710e528d893892b9fe56@54.218.158.147:26656,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,913e9db0332df1152e5afe032ab81bdb65e3f91c@110.11.23.44:26656,3226b67b2bb9da41b633392a785e87e8f6749939@162.55.245.149:12000,ef573bd8b519f9572798444f6c229ab0a3204bb8@5.9.94.24:26656,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,170e681516b039be361df87eb626ee81c08f07a4@157.245.115.42:26656,2cb8dd6195c65458e3c18505bb70ce2ff624f85c@89.58.61.223:2000,79824a84c7bc35716839ac9c47dc05cceabf42c0@34.173.85.215:26656,7fc90a9c32c775ff685798c33fc06fe6d5009b26@202.61.229.102:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,a50c8dcd0e83032b5e29d5c5beef6e54ddafb508@35.83.253.164:26656,ec929701754be057fb38c824fc127e26add9c900@138.201.121.185:26666,1c02ae0be21e3b08d9beadf91c26aec4193d2659@135.181.22.238:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
