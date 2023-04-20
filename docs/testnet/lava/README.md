# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.9.8 | **Wasm**: OFF

[Website](https://lavanet.xyz) | [Discord](https://discord.com/invite/Tbk5NxTCdA) | [Twitter](https://twitter.com/lavanetxyz)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/lava-testnet](https://explorer.kjnodes.com/lava-testnet)

## Public endpoints

* api: [https://lava-testnet.api.kjnodes.com](https://lava-testnet.api.kjnodes.com)
* rpc: [https://lava-testnet.rpc.kjnodes.com](https://lava-testnet.rpc.kjnodes.com)
* grpc: lava-testnet.grpc.kjnodes.com:44090

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
peers="e13f5c3fb2f1a4ebe03d7a3ceda83c0994cf05ec@68.183.186.121:26656,b1a9277efbd2634979b8bf90ebfde19f3af830bd@75.119.146.252:44656,25da069c4dca143029ddae47bf2b7de69c2a8678@65.108.9.164:21156,92f8e4caaadb2f00c95e03068933f2045a93e910@65.109.65.163:21156,c0efea9152aed75fcf3022b8af45243818c59d6a@49.12.13.104:26656,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,e1383b216c42acc842193c5ac7321ce6c0d73db0@78.47.37.142:26656,370ae92bd28701e0c1d8dc912ccf0d40fe0db3d5@157.90.245.166:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,ed780f77754e8c4657b145144f0f95225d43bb03@65.108.224.156:27656,342dbbf200eb906eed6901cb5edf6d341b4ebc9b@170.64.140.230:26656,4ad3f3731073a016fa0c99118b2a5a2d313928f5@207.180.233.148:26656,9a151159039fd8abce61ddb21e5342605787792b@5.75.228.39:26656,3173b2d34ce415ee9a1bf08646d85688bf49e299@5.189.186.222:36656,c32d101819cedf78ea986e6d832e2306fb6d0649@185.248.24.224:16656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,99327e5cf0f31ac3bb1ca8e39cc9f17c823b7ec1@109.236.88.8:26656,4732ed188fbe7603f81d9f4c825397277bb72217@5.75.235.195:26656,257856431ef33f9fbfe6c119fdf3820035891d0c@38.242.197.140:26656,bbf1fd8b2b993dd354453f90749bd08d108b5de3@194.61.28.30:16656,e1c09e10296de98d5637e0f948ada9d477ad4d75@31.42.191.74:36656,5b337f7ba27e2fdd27918be18af93f8728034267@65.108.41.168:26656,8b154033143fdedf4835dfc7b030c7d781bfd54e@195.201.219.227:26656,1d2b4cb05b8408b06dc195b9238461ca2b594fe8@88.198.8.79:3720,71e3686daaa1acf39eb3c325883f0ae330f91959@207.180.194.162:38656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,3d05c96b70553fa5feb5d088fb4c0e2f01b3ec4e@136.243.147.235:38656,f1bb78a30c9381bed392fda141a5c1f6fa4d25e6@144.76.114.49:26656,71fb615c968e6ea9458d065d71d47dd1bb10d11e@185.205.246.203:36656,7aa9d96f0a3f162385b743ef92a2c6e03a4a1d84@65.108.48.77:20656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
