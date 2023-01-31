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

**live-peers** (31)
```bash
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,dfa93668152cb6b3a822c987f9c22110a1c2f314@178.18.255.221:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,3c47fd1662bcb17a4713c23e41d7b25e34478b8e@103.19.25.157:26672,0a78dd75926983ba06de451480673487ffa1bcc1@199.175.98.106:26656,a5e5a9ef106ac952d212a982beb90190b74ee394@75.119.130.1:38656,5b25ec3860445e50a41a80850970b3241350df72@194.233.90.134:26656,b36a39d183383fa068f0db145b179bf8455a06f4@38.242.159.214:26656,2ba0a1c952954f37e3b14abc1e35c77f74c64c8a@161.97.136.244:36656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,3173b2d34ce415ee9a1bf08646d85688bf49e299@5.189.186.222:36656,d38ba32cc262b23c49748428880315485e48963d@65.108.126.35:25656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,0a528da95ca8025ef4043b6e73f1e789f4102940@176.103.222.22:26656,aa49801c761898c12d196120de9971353344061a@46.151.29.53:38656,04666ecb2f62163e684ca8632a6c293aedf5156c@161.97.179.184:26656,8ef9baeaaf8e4e3c478c74b2334ab61d7190be72@91.144.158.116:56656,441fffc1478d480934d11d397384682ac42acd2f@95.217.9.227:26656,0adbe1e790b58d19cc53a9839059a95d7d5d7aba@65.109.70.23:19956,d3eb474a1f90d004e49638e384069c32d7dcc8a2@185.252.232.110:26656,9cc793bd6f8aeb029a781178b1112294fbb307ce@65.21.79.97:36656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,b1223ecc0fdde9d72551b9223f69b5310f870a67@85.208.51.197:26656,602c87226395588e141076abbc967945465bba8e@65.109.68.93:36656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,5676c8606f23471e220f8bf7317498a61bb93194@65.21.134.202:26686,fa17e6c47e7157258f854dba1a02184fc874b0d5@82.115.25.207:26656,79a3b530b271b1f9b5e10617fcca9041c9f8f548@65.108.45.200:26858,821c9347c927db52138dcd4bb54478fdf17f273e@81.0.218.53:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
