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

**live-peers** (24)
```bash
peers="f9f49cc8ffbdee85fb8a9551f644f5554a610ebe@91.107.137.90:26656,24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,3a750868d3284cc4a07be4a878333e38b44b94bf@144.91.111.1:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,f30d07170a092f82702e3c12334fa9fd828b71c6@168.119.124.130:47656,f68c57ca955420779773f9320a6b7710c2b29f73@188.191.36.222:26656,3c47fd1662bcb17a4713c23e41d7b25e34478b8e@103.19.25.157:26672,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,bd1e1f8df77e7b61200c490c9fabe6bbc4412d4e@91.223.3.144:26856,13a9209a4d08803a3becac57de8eb02dd51f8f41@65.109.23.114:19956,6a55747d1f93e46696f233ac563e28fea24afc47@38.242.237.192:36656,90451ff8f47b8f4b077e95837f112135fea14531@207.180.231.123:31656,c44a02dba51e23ac06b006fb1285988c89051ce7@85.10.198.171:26556,7022dbc496c5cc645df6a44f792b40aa150844a3@62.141.44.209:38656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,8636a0d9276ee1b99c772e51904ea010862bc772@135.181.133.37:27656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,bb8c8cea499a1fa7e97922b5a9882c2360c6575a@176.103.222.21:26656,d3eb474a1f90d004e49638e384069c32d7dcc8a2@185.252.232.110:26656,dfa93668152cb6b3a822c987f9c22110a1c2f314@178.18.255.221:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,602c87226395588e141076abbc967945465bba8e@65.109.68.93:36656,6dd9c6d619f9e6fc75f39bacd313f811ca64b2c6@65.108.224.180:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
