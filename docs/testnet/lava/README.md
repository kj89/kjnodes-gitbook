# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/lava.png" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.10.1 | **Wasm**: OFF

[Website](https://lavanet.xyz) | [Discord](https://discord.com/invite/Tbk5NxTCdA) | [Twitter](https://twitter.com/lavanetxyz)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/lava-testnet](https://explorer.kjnodes.com/lava-testnet)

## Public endpoints

* api: [https://lava-testnet.api.kjnodes.com](https://lava-testnet.api.kjnodes.com)
* rpc: [https://lava-testnet.rpc.kjnodes.com](https://lava-testnet.rpc.kjnodes.com)
* grpc: lava-testnet.grpc.kjnodes.com:144090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@lava-testnet.rpc.kjnodes.com:144656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@lava-testnet.rpc.kjnodes.com:144659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/lava-testnet/addrbook.json > $HOME/.lava/config/addrbook.json
```

**live-peers** (30)
```bash
peers="99327e5cf0f31ac3bb1ca8e39cc9f17c823b7ec1@109.236.88.8:26656,e0f25590f8074b4ea70f069f9be332b19f81f344@23.88.70.109:15656,ed780f77754e8c4657b145144f0f95225d43bb03@65.108.224.156:27656,b4d53b1e7a2fee2192a30e411ba83136c07ab595@161.97.147.107:26656,342dbbf200eb906eed6901cb5edf6d341b4ebc9b@170.64.140.230:26656,c0efea9152aed75fcf3022b8af45243818c59d6a@49.12.13.104:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,ac589df63d0c325329009a1e8a60602a8fc2be9f@57.128.54.106:26656,92f8e4caaadb2f00c95e03068933f2045a93e910@65.109.65.163:21156,e1383b216c42acc842193c5ac7321ce6c0d73db0@78.47.37.142:26656,3b18b1dc95e02a36327b13fc45c225b23fb08ed8@78.47.187.72:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,9a151159039fd8abce61ddb21e5342605787792b@5.75.228.39:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,e1c09e10296de98d5637e0f948ada9d477ad4d75@31.42.191.74:36656,4fc42fdf634ef542094c7a44f22e031acea61162@91.77.165.172:27656,3173b2d34ce415ee9a1bf08646d85688bf49e299@5.189.186.222:36656,370ae92bd28701e0c1d8dc912ccf0d40fe0db3d5@157.90.245.166:26656,4732ed188fbe7603f81d9f4c825397277bb72217@5.75.235.195:26656,799077b3a3b52094ab3ca19b6a7ecab89c50cb61@185.144.99.97:26657,3456c9ba0df46cbb526717d73fa51ff0ed9a53a1@95.216.14.58:60756,147cf727f179eccbd29de3ebf5899c1f4a93f6de@46.38.235.53:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,c32d101819cedf78ea986e6d832e2306fb6d0649@185.248.24.224:16656,5b337f7ba27e2fdd27918be18af93f8728034267@65.108.41.168:26656,bb8c8cea499a1fa7e97922b5a9882c2360c6575a@176.103.222.21:26656,257856431ef33f9fbfe6c119fdf3820035891d0c@38.242.197.140:26656,0322670e17a172f25fec71f274f2bd28d1b7e74f@185.163.64.143:26656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
