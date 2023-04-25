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
peers="6171a52cf0ffc1706409d2dcec56c1db81c86aae@176.103.222.17:26656,13a9209a4d08803a3becac57de8eb02dd51f8f41@65.109.23.114:19956,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,ed780f77754e8c4657b145144f0f95225d43bb03@65.108.224.156:27656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,40046fe63bdaa9efde27707b0d3de0bf84fedf80@86.111.48.158:26656,257856431ef33f9fbfe6c119fdf3820035891d0c@38.242.197.140:26656,9a151159039fd8abce61ddb21e5342605787792b@5.75.228.39:26656,eac9351f5f6738458c39ed88f135a9c7996a6d43@45.249.244.209:26656,53cba364b17674a182a19bd0fd6fc06ffae488b0@161.97.133.186:26656,25da069c4dca143029ddae47bf2b7de69c2a8678@65.108.9.164:21156,92f8e4caaadb2f00c95e03068933f2045a93e910@65.109.65.163:21156,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,e1383b216c42acc842193c5ac7321ce6c0d73db0@78.47.37.142:26656,370ae92bd28701e0c1d8dc912ccf0d40fe0db3d5@157.90.245.166:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,c0efea9152aed75fcf3022b8af45243818c59d6a@49.12.13.104:26656,4ad3f3731073a016fa0c99118b2a5a2d313928f5@207.180.233.148:26656,4732ed188fbe7603f81d9f4c825397277bb72217@5.75.235.195:26656,3173b2d34ce415ee9a1bf08646d85688bf49e299@5.189.186.222:36656,5b337f7ba27e2fdd27918be18af93f8728034267@65.108.41.168:26656,35f045092f9c51ab743eec194438b91ecf8ce69e@65.109.116.22:11134,0edd924d5422ab3cbf71d212c4e5511e622ee464@31.220.87.123:26656,7aa9d96f0a3f162385b743ef92a2c6e03a4a1d84@65.108.48.77:20656,9ff4aa1369a5759a05e0f8a40ebec5dae57735e9@135.181.161.235:26656,ff27ef7b864955c912281d307c85d4ac9f9b9f54@159.223.64.76:26656,8b154033143fdedf4835dfc7b030c7d781bfd54e@195.201.219.227:26656,2c419186cd96b59fe8b3307c54c27d6805414aba@65.108.8.28:60756,1550fe479ee2dcfa35f7dcd2c66f37a50d34b0e3@178.63.132.243:2237,7fb838681ff9855a634c7823de605fb4a5d22eba@65.108.144.202:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
