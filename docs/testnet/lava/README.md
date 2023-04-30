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

**live-peers** (26)
```bash
peers="ed780f77754e8c4657b145144f0f95225d43bb03@65.108.224.156:27656,1f704611e8aa4a53504fac1b80eb55c876dae8bd@65.108.13.154:30656,035d086cc418352aba9e679e079f17391791ccc6@178.208.252.54:27656,92f8e4caaadb2f00c95e03068933f2045a93e910@65.109.65.163:21156,e6e852c92e35a4976dab99604b0e79c365345ef6@91.229.245.21:26656,e1383b216c42acc842193c5ac7321ce6c0d73db0@78.47.37.142:26656,ac589df63d0c325329009a1e8a60602a8fc2be9f@57.128.54.106:26656,370ae92bd28701e0c1d8dc912ccf0d40fe0db3d5@157.90.245.166:26656,9a151159039fd8abce61ddb21e5342605787792b@5.75.228.39:26656,c0efea9152aed75fcf3022b8af45243818c59d6a@49.12.13.104:26656,3173b2d34ce415ee9a1bf08646d85688bf49e299@5.189.186.222:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,13a9209a4d08803a3becac57de8eb02dd51f8f41@65.109.23.114:19956,7aa9d96f0a3f162385b743ef92a2c6e03a4a1d84@65.108.48.77:20656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,e1c09e10296de98d5637e0f948ada9d477ad4d75@31.42.191.74:36656,4732ed188fbe7603f81d9f4c825397277bb72217@5.75.235.195:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,2c419186cd96b59fe8b3307c54c27d6805414aba@65.108.8.28:60756,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,5b337f7ba27e2fdd27918be18af93f8728034267@65.108.41.168:26656,bd1e1f8df77e7b61200c490c9fabe6bbc4412d4e@91.223.3.144:26856,c58181fa2022022a36ddda08b79c5b666cb45a7d@194.34.232.225:17656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,c32d101819cedf78ea986e6d832e2306fb6d0649@185.248.24.224:16656,4f9120f706512162fbe4f39aac78b9924efbec58@65.109.92.235:11036"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
