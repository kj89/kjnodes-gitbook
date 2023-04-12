# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.8.1 | **Wasm**: OFF

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

**live-peers** (24)
```bash
peers="14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,0a528da95ca8025ef4043b6e73f1e789f4102940@176.103.222.22:26656,4bb3bb98ca32b5a0f82d445e60065601bb93a38c@86.111.48.163:26656,4373d820675ffcad758892bbd8e442d545cb1f4b@86.111.48.155:26656,d9abc551547563e9a45160adc070b8bb42fc7d62@75.119.134.69:29656,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,40046fe63bdaa9efde27707b0d3de0bf84fedf80@86.111.48.158:26656,25da069c4dca143029ddae47bf2b7de69c2a8678@65.108.9.164:21156,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,f68c57ca955420779773f9320a6b7710c2b29f73@188.191.36.222:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,fb2b9d41678f3d1c9c0bdef1a87f2037b6b0088a@146.19.24.252:26666,0a78dd75926983ba06de451480673487ffa1bcc1@199.175.98.106:26656,125935f63c123b6891b014ffc071fbf781270771@23.88.74.54:11656,929d47994552e8cf6230f8b1d1a5c91e03209bf1@85.239.235.235:44656,6f71395e15c9f9f439df51fc6a667d93a1b7b019@35.162.117.131:26656,f137232fd25d5c3adc6d3f6cffa879beafe17768@89.250.150.241:26656,dc1c37e340a191ac0eea7c561b4a3c8fba2ce80a@65.21.237.241:26656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,95a490b4cde4c5311f7d58c3e47ee41fa039ddf4@144.76.27.79:60756,aebbf38433cc38ed3aad0bb5f2aa567797df78da@46.8.210.144:26756,0d08a1b452e6d7ccdfbc9b54658b5f9ed24eff7b@135.181.138.160:29956,370ae92bd28701e0c1d8dc912ccf0d40fe0db3d5@157.90.245.166:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
