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

**live-peers** (30)
```bash
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,f31c4dc121f37db1e0e24b49584bbbe4bbbba6c4@162.55.39.16:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,3c47fd1662bcb17a4713c23e41d7b25e34478b8e@103.19.25.157:26672,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,1377a4d43745a650fe21cc87641818854e9fbdcf@65.109.88.254:35656,c19965fe8a1ea3391d61d09cf589bca0781d29fd@162.19.217.52:26656,3173b2d34ce415ee9a1bf08646d85688bf49e299@5.189.186.222:36656,897d44b1cb6633539cf51261f6629a9d5664eb9b@159.69.72.247:11656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,76c7e5d8e52067d06665f20966175163c88dab63@109.110.63.204:36656,22c51515eea1df09dc872dc8843efb7fc73770b1@199.175.98.102:26656,6a55747d1f93e46696f233ac563e28fea24afc47@38.242.237.192:36656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,bb8c8cea499a1fa7e97922b5a9882c2360c6575a@176.103.222.21:26656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,5ca04690ab3fdd0ec96929eb05122ca1a088697d@161.97.131.179:26656,0c548b2704594c7929b713de4c6985b9d9f03b8a@194.163.184.46:27656,86cd808d9f4674b8810e4720ccff745d8c88ba3b@65.108.90.48:26656,dfa93668152cb6b3a822c987f9c22110a1c2f314@178.18.255.221:26656,0adbe1e790b58d19cc53a9839059a95d7d5d7aba@65.109.70.23:19956,441fffc1478d480934d11d397384682ac42acd2f@95.217.9.227:26656,c5d6e795221044ca0fd0e1d4cbe4cbee4e5a7c0b@159.69.32.109:26656,160000efb6293c89e411ac81b086f8a9fe0c770a@161.97.144.208:26656,d3eb474a1f90d004e49638e384069c32d7dcc8a2@185.252.232.110:26656,f68c57ca955420779773f9320a6b7710c2b29f73@188.191.36.222:26656,e6703109f87389aea6b1ca9b8335a6eddbce50d6@185.182.186.85:26656,0a94c7f8451841f51bfaf86668edd212f181735f@95.214.55.155:21656,4732ed188fbe7603f81d9f4c825397277bb72217@5.75.235.195:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
