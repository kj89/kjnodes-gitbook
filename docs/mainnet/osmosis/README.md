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
peers="0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,31d2c86f7957e2db91297e54c3b0456ea06c2250@173.67.177.115:26656,6e9b0cf3ea78a9a540c75a4cfeb0c6a54b73fee4@65.108.127.166:26656,f95d9634ad68b8f0ac80ce308adb71d8c119ada5@141.98.219.104:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,2ff9bc1740a721a9baeda01abee181997bb65568@142.132.140.20:26656,4a837e3411b0281f00c07706cfea72d3ebc575f1@176.9.38.49:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,4cccbb26639559c39f44758d246c5ed928f7717f@176.9.19.66:26656,e0f3b604f1df9bf6590c4cc09fee1e28f46b0b39@65.109.28.226:15656,3d311ac374e6953e97ee07c74a76f399394c3025@173.215.85.171:20000,747d01891a83d6f759d88f9be07159c268b584b0@141.95.65.98:26656,cb0ad76ff7ec6488073a710e528d893892b9fe56@54.218.158.147:26656,9042664a475c4bd036d973b5783bb2f8a6928eb5@65.109.20.216:26656,6cbb199c891bf1ed925c64fd1ec0882afdc2e2dc@162.19.81.54:34656,3226b67b2bb9da41b633392a785e87e8f6749939@162.55.245.149:12000,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@178.211.139.77:26716,b6ec9c7284b45eb912b01c192f7ffd8ef7508ec7@51.81.123.33:26656,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,65f51ebf46256d829ae5903e9faf31dae35bdf46@65.109.64.245:26656,ef573bd8b519f9572798444f6c229ab0a3204bb8@5.9.94.24:26656,471518432477e31ea348af246c0b54095d41352c@169.155.47.35:26656,807eda3abecff79df294d127cf58d6d5e07393ee@67.209.54.21:26656,5696d9806c883beb725fb469d90039d921107b5b@116.202.209.186:26656,34340a9151d4a97a850d2cd64d8778279faf3f96@194.163.181.100:26656,9379a49cadb2e71d896c2d4ebd5ca394e50bf983@18.116.211.23:26656,6b1dd134b30aeaeb2f21f33bd2cd0370a2275501@138.68.6.165:26656,2048e1bc1f020fa210fb475e7a0ec0948919609f@185.217.125.64:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
