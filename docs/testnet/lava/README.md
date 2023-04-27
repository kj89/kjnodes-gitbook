# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/lava.png" alt=""><figcaption></figcaption></figure>

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
peers="9a151159039fd8abce61ddb21e5342605787792b@5.75.228.39:26656,257856431ef33f9fbfe6c119fdf3820035891d0c@38.242.197.140:26656,24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,25da069c4dca143029ddae47bf2b7de69c2a8678@65.108.9.164:21156,c0efea9152aed75fcf3022b8af45243818c59d6a@49.12.13.104:26656,92f8e4caaadb2f00c95e03068933f2045a93e910@65.109.65.163:21156,3173b2d34ce415ee9a1bf08646d85688bf49e299@5.189.186.222:36656,370ae92bd28701e0c1d8dc912ccf0d40fe0db3d5@157.90.245.166:26656,5b337f7ba27e2fdd27918be18af93f8728034267@65.108.41.168:26656,e1383b216c42acc842193c5ac7321ce6c0d73db0@78.47.37.142:26656,4732ed188fbe7603f81d9f4c825397277bb72217@5.75.235.195:26656,d8e81881ced029758f9623179a3c1ecf72aece2e@195.74.86.49:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,2a588e5ddcfd8c9095cc6f34b5b6966e31020cfd@65.21.123.172:11656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,4ad3f3731073a016fa0c99118b2a5a2d313928f5@207.180.233.148:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,7aa9d96f0a3f162385b743ef92a2c6e03a4a1d84@65.108.48.77:20656,a724b94c593241890022e204e0065d8baa67168c@116.202.227.117:44656,c32d101819cedf78ea986e6d832e2306fb6d0649@185.248.24.224:16656,2c419186cd96b59fe8b3307c54c27d6805414aba@65.108.8.28:60756,230648adf4aa55029c72ec5d7bc1be59529acf34@37.120.171.159:26656,342dbbf200eb906eed6901cb5edf6d341b4ebc9b@170.64.140.230:26656,66be93bd38fadeedde32f6adce6859b9700b1f11@182.217.153.83:26656,47385d0a7051109de5342e3b27890c4a4b9e0763@65.108.72.233:16656,bb8c8cea499a1fa7e97922b5a9882c2360c6575a@176.103.222.21:26656,dd7f68ed87765006fa50d45fb7514afc27a53b6b@65.108.152.37:26656,8b154033143fdedf4835dfc7b030c7d781bfd54e@195.201.219.227:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
