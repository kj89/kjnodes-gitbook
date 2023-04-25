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
peers="1c398af2208984d4e59bc41132e3eac0508abb0f@95.216.76.251:26656,2f4c0337b2522034a614a5cb2c61a891fe753c03@5.9.81.187:29656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,e726816f42831689eab9378d5d577f1d06d25716@23.88.22.10:26656,3d311ac374e6953e97ee07c74a76f399394c3025@173.215.85.171:20000,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,13d17adf418ceab5528096dcacf130830fee2b86@35.215.50.201:26656,b6ec9c7284b45eb912b01c192f7ffd8ef7508ec7@51.81.123.33:26656,95dbddda671081fb433871fa612ff5291242d93d@45.67.221.200:26656,27e14df66c9e4cd6b176b0dca6adfa9b6750f911@5.161.72.103:26656,65f51ebf46256d829ae5903e9faf31dae35bdf46@65.109.64.245:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@169.155.169.186:26656,af678c610cf37bf5d443efdba7ac1354f104415c@137.184.9.18:32644,74e8ba742d8312c250f3237c8c8f3f951c01f9df@95.216.4.104:26656,ef573bd8b519f9572798444f6c229ab0a3204bb8@5.9.94.24:26656,9e4fab3bb896e647b4e3a3db1716eb32432a2a87@18.182.78.42:26656,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,071ae914b06e14148a6286a0fa087c797336f043@34.105.246.121:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@178.211.139.77:26716,12910da249bcee4cdafbef938b10b51c94c0057e@5.9.142.165:26656,7f36123a395e902deaecf63bdaf5656bbb209623@15.204.52.75:26656,0dcd3bc339e3018b68e1dd176007dbd7421db9f2@34.241.178.111:26656,993ab600d80d7d1884daf84a9dd2319d9332bb46@93.115.25.170:26656,8b534f8055d44776dbfb03e8502905e727125fbc@178.162.166.22:16656,7fc90a9c32c775ff685798c33fc06fe6d5009b26@202.61.229.102:26656,3e874613919a6f8b3fc26071fef563c88f031b3c@116.202.236.59:31656,3e3f8f3a9ed941600550d090900aee639abb7906@93.159.134.158:56656,991e8c2d75ed411c3ee620d61db7d49346a3f88b@146.190.48.40:32143"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
