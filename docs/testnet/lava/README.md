# Services

[installation](./installation/ "mention") [upgrade](./upgrade/ "mention") [snapshot](./snapshot/ "mention") [state-sync](./state-sync/ "mention") [useful-commands](./useful-commands/ "mention")

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
peers="13a9209a4d08803a3becac57de8eb02dd51f8f41@65.109.23.114:19956,ed780f77754e8c4657b145144f0f95225d43bb03@65.108.224.156:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,92f8e4caaadb2f00c95e03068933f2045a93e910@65.109.65.163:21156,c0efea9152aed75fcf3022b8af45243818c59d6a@49.12.13.104:26656,25da069c4dca143029ddae47bf2b7de69c2a8678@65.108.9.164:21156,3173b2d34ce415ee9a1bf08646d85688bf49e299@5.189.186.222:36656,e1383b216c42acc842193c5ac7321ce6c0d73db0@78.47.37.142:26656,370ae92bd28701e0c1d8dc912ccf0d40fe0db3d5@157.90.245.166:26656,aebbf38433cc38ed3aad0bb5f2aa567797df78da@46.8.210.144:26756,799077b3a3b52094ab3ca19b6a7ecab89c50cb61@185.144.99.97:26657,4ad3f3731073a016fa0c99118b2a5a2d313928f5@207.180.233.148:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,9a151159039fd8abce61ddb21e5342605787792b@5.75.228.39:26656,5c107bb2b72c930a5ab3406a1f7c7345b7229b49@148.251.11.99:11656,8bb931d994a19c6647e6165cae98b14bcc2e22c2@144.76.99.105:38656,a2afdc48785be73f208af349e78d632b5556cc01@5.75.226.151:26656,4732ed188fbe7603f81d9f4c825397277bb72217@5.75.235.195:26656,0d08a1b452e6d7ccdfbc9b54658b5f9ed24eff7b@135.181.138.160:29956,5b337f7ba27e2fdd27918be18af93f8728034267@65.108.41.168:26656,dd7f68ed87765006fa50d45fb7514afc27a53b6b@65.108.152.37:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,47385d0a7051109de5342e3b27890c4a4b9e0763@65.108.72.233:16656,b591ef22e0c2082eb76dcac5ead95be55d01b695@65.109.178.147:26656,c32d101819cedf78ea986e6d832e2306fb6d0649@185.248.24.224:16656,3d05c96b70553fa5feb5d088fb4c0e2f01b3ec4e@136.243.147.235:38656,d8e81881ced029758f9623179a3c1ecf72aece2e@195.74.86.49:26656,f137232fd25d5c3adc6d3f6cffa879beafe17768@89.250.150.241:26656,a8bcdfc4d1037c82407408f4b8269f6a3ec694b1@49.12.57.34:26656,bb8c8cea499a1fa7e97922b5a9882c2360c6575a@176.103.222.21:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
