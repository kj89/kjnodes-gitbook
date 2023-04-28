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
peers="4732ed188fbe7603f81d9f4c825397277bb72217@5.75.235.195:26656,8b154033143fdedf4835dfc7b030c7d781bfd54e@195.201.219.227:26656,13a9209a4d08803a3becac57de8eb02dd51f8f41@65.109.23.114:19956,bfe21dd5af98aa42d213cd5bd943162a36b0505f@92.243.165.98:26656,c0efea9152aed75fcf3022b8af45243818c59d6a@49.12.13.104:26656,25da069c4dca143029ddae47bf2b7de69c2a8678@65.108.9.164:21156,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,ac589df63d0c325329009a1e8a60602a8fc2be9f@57.128.54.106:26656,92f8e4caaadb2f00c95e03068933f2045a93e910@65.109.65.163:21156,370ae92bd28701e0c1d8dc912ccf0d40fe0db3d5@157.90.245.166:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,3b18b1dc95e02a36327b13fc45c225b23fb08ed8@78.47.187.72:26656,e1383b216c42acc842193c5ac7321ce6c0d73db0@78.47.37.142:26656,9a151159039fd8abce61ddb21e5342605787792b@5.75.228.39:26656,147cf727f179eccbd29de3ebf5899c1f4a93f6de@46.38.235.53:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,799077b3a3b52094ab3ca19b6a7ecab89c50cb61@185.144.99.97:26657,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,3173b2d34ce415ee9a1bf08646d85688bf49e299@5.189.186.222:36656,2c419186cd96b59fe8b3307c54c27d6805414aba@65.108.8.28:60756,257856431ef33f9fbfe6c119fdf3820035891d0c@38.242.197.140:26656,f0501090b870f7796dfdd1f1f5479aec2baecfe8@88.198.52.89:11656,5b337f7ba27e2fdd27918be18af93f8728034267@65.108.41.168:26656,1f704611e8aa4a53504fac1b80eb55c876dae8bd@65.108.13.154:30656,c32d101819cedf78ea986e6d832e2306fb6d0649@185.248.24.224:16656,47385d0a7051109de5342e3b27890c4a4b9e0763@65.108.72.233:16656,2a588e5ddcfd8c9095cc6f34b5b6966e31020cfd@65.21.123.172:11656,4e0a2772bb3672e54c2ea655c30abdac62191f14@45.84.138.66:18656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,cb722cc36541920d3907cd67743db5444f53e80b@95.70.184.178:24656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
