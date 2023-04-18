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
peers="c7fb97358712f447ca0689e814fe8c965a71b314@65.21.133.114:26656,2f4c0337b2522034a614a5cb2c61a891fe753c03@5.9.81.187:29656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,34340a9151d4a97a850d2cd64d8778279faf3f96@194.163.181.100:26656,7fc90a9c32c775ff685798c33fc06fe6d5009b26@202.61.229.102:26656,e726816f42831689eab9378d5d577f1d06d25716@23.88.22.10:26656,677ef9606ea18a13b5dbfad19493d99d7ea068f5@149.56.24.130:26656,f860ee99ef34f10155065a97e95da07f712f1d6b@116.202.169.6:26666,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,31d2c86f7957e2db91297e54c3b0456ea06c2250@173.67.177.115:26656,913e9db0332df1152e5afe032ab81bdb65e3f91c@110.11.23.44:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,3226b67b2bb9da41b633392a785e87e8f6749939@162.55.245.149:12000,4cccbb26639559c39f44758d246c5ed928f7717f@176.9.19.66:26656,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,807eda3abecff79df294d127cf58d6d5e07393ee@67.209.54.21:26656,dd218877f3c12487ad5e21b1138a50f45e157dc8@20.108.43.60:26656,65f51ebf46256d829ae5903e9faf31dae35bdf46@65.109.64.245:26656,f96947493f1edd08058afaeaef8f5830cc70b8f2@15.204.197.10:26656,3d311ac374e6953e97ee07c74a76f399394c3025@173.215.85.171:20000,82e224c9640048a6513c589e904c0d903bb99f32@74.118.140.23:26656,fc358e432202f3bad58666de2e5bcffba9156711@20.216.164.199:26656,e17c0a849eb239acd9f08ba396dec0db149b6ffc@185.255.131.77:26656,ef573bd8b519f9572798444f6c229ab0a3204bb8@5.9.94.24:26656,79824a84c7bc35716839ac9c47dc05cceabf42c0@34.173.85.215:26656,a50c8dcd0e83032b5e29d5c5beef6e54ddafb508@35.83.253.164:26656,3e369738cb861a252e4836d553e982988e40a41b@15.235.53.45:2000,ebee7d93a224aaab7bf552b27e2ac7406f0d85b5@4.231.216.0:26656,8df1d1d8b7e1007f75dd4873d75b7c07611a2ded@40.68.14.103:26656,2048e1bc1f020fa210fb475e7a0ec0948919609f@185.217.125.64:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
