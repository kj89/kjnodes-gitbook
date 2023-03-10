# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.7.0 | **Wasm**: OFF

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

**live-peers** (32)
```bash
peers="f642b376722d6ce104ffd4c204e78ffe811e16c3@5.75.230.221:26656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,d6a116d2aed64bd2f383b894e38f2a62232e44b7@116.202.161.165:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,f68c57ca955420779773f9320a6b7710c2b29f73@188.191.36.222:26656,5bdbd9a68d212ec341c781cc553043486ce5b8ee@31.220.76.135:26656,9d5802ec3e10fbac150850ffdfa50f324e804b95@95.214.55.62:35656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,0735c5a841fe98ee0a74de7cef537c03b4c66a1b@45.89.54.153:26656,b591ef22e0c2082eb76dcac5ead95be55d01b695@65.109.178.147:26656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,0f9f0fb4b9371a65bdf1c883a2a7dc52d0023019@34.233.69.21:26656,aebbf38433cc38ed3aad0bb5f2aa567797df78da@46.8.210.144:26756,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,7ec0007e3c24012db9d5596745db5cb7c8321b50@95.216.7.169:60956,e06519a36d7c780af9ad2be69616a98445112c7a@80.79.5.171:29656,5a469a75fb05eddf2d79fb17063cc59e84d0821a@207.180.236.115:34656,9057ee9d3d9b3c42c184dc89a7b2a07026b81a45@31.220.76.131:26656,550d7467d6a442da11d9772b804252a8dfdca27e@91.107.243.149:26656,f7c1a998b8ef7cae7e38b0eff64d96206924e957@45.84.138.167:26656,0325a40dfa74c462cc51e64f1c5e331dff1cae2c@65.109.111.159:38656,92b2e2f59cbbb11c601919f058575fbc50cb73c6@65.109.183.202:26656,0749517ad6e04173bbcbb2cd87a1e56519ca7038@109.205.181.35:26656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,b62eb3baed171ab5654292e5e35d56a1287693c9@45.32.66.24:26656,0adbe1e790b58d19cc53a9839059a95d7d5d7aba@65.109.70.23:19956,94e57de2ffaa856ca23c23b81dc17d21a71833c5@194.233.75.144:26656,8b774eabd1b4fbffdf9d14fba3d4a1690c69d0ad@65.109.24.227:30656,0925c475208d8e338907383ab87a094ad03c478e@65.109.55.186:40656,4634ca7cefe997035440df1095915ed255e81296@49.12.189.98:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
