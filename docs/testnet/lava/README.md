# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.4.4 | **Wasm**: OFF

[Website](https://lavanet.xyz) | [Discord](https://discord.com/invite/Tbk5NxTCdA) | [Twitter](https://twitter.com/lavanetxyz)




## Chain explorer
[https://explorer.kjnodes.com/lava-testnet](https://explorer.kjnodes.com/lava-testnet)

## Public endpoints

* api: [https://lava-testnet.api.kjnodes.com](https://lava-testnet.api.kjnodes.com)
* rpc: [https://lava-testnet.rpc.kjnodes.com](https://lava-testnet.rpc.kjnodes.com)
* grpc: [https://lava-testnet.grpc.kjnodes.com](https://lava-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@lava-testnet.rpc.kjnodes.com:44656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@lava-testnet.rpc.kjnodes.com:44659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/lava-testnet/addrbook.json > $HOME/.lava/config/addrbook.json
```

**live-peers** (29)
```bash
peers="dfa93668152cb6b3a822c987f9c22110a1c2f314@178.18.255.221:26656,24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,3c47fd1662bcb17a4713c23e41d7b25e34478b8e@103.19.25.157:26672,f68c57ca955420779773f9320a6b7710c2b29f73@188.191.36.222:26656,420704479ed1e13f862ee08162e40325107fef14@115.74.127.184:26656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,33298ebaaa99faad4f5c9880f555340f26ff66ff@161.97.160.19:26656,5b25ec3860445e50a41a80850970b3241350df72@194.233.90.134:26656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,a5c1d2e86c2dc0eecb009dc71c92d6b5e193db6b@35.210.166.150:26656,fb2b9d41678f3d1c9c0bdef1a87f2037b6b0088a@146.19.24.252:26666,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,1b09acd86e1a2db56c72db7848ada3ad581f027a@95.217.109.222:36656,0a78dd75926983ba06de451480673487ffa1bcc1@199.175.98.106:26656,ac7cefeff026e1c616035a49f3b00c78da63c2e9@18.215.128.248:26656,71fb615c968e6ea9458d065d71d47dd1bb10d11e@185.205.246.203:36656,bb8c8cea499a1fa7e97922b5a9882c2360c6575a@176.103.222.21:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,cb722cc36541920d3907cd67743db5444f53e80b@95.70.184.178:24656,0adbe1e790b58d19cc53a9839059a95d7d5d7aba@65.109.70.23:19956,1fd86f6ba06ef4b189276f97f70fea04161019db@144.76.176.154:11656,b1223ecc0fdde9d72551b9223f69b5310f870a67@85.208.51.197:26656,6dd9c6d619f9e6fc75f39bacd313f811ca64b2c6@65.108.224.180:26656,5676c8606f23471e220f8bf7317498a61bb93194@65.21.134.202:26686,d60e577b6dbdac7a7cd620f71a6bff71f9f82c2e@146.19.24.242:26656,fa17e6c47e7157258f854dba1a02184fc874b0d5@82.115.25.207:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
