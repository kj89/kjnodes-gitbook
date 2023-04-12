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
peers="0a528da95ca8025ef4043b6e73f1e789f4102940@176.103.222.22:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,25da069c4dca143029ddae47bf2b7de69c2a8678@65.108.9.164:21156,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,e0f25590f8074b4ea70f069f9be332b19f81f344@23.88.70.109:15656,f9af0186eec9a88a5a657deb9a7deff34c05d99f@86.111.48.156:26656,125935f63c123b6891b014ffc071fbf781270771@23.88.74.54:11656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,8cd81b9119e4aa45fe549dd12543de862457c989@38.242.155.47:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,4e0a2772bb3672e54c2ea655c30abdac62191f14@45.84.138.66:18656,11d25deba9c655a7312716810e3975fe175ada01@5.161.58.198:26656,d6a116d2aed64bd2f383b894e38f2a62232e44b7@116.202.161.165:36656,4634ca7cefe997035440df1095915ed255e81296@49.12.189.98:26656,2fd7bd090b7dae19023ba543f8c3015a838de9c6@185.16.38.122:24656,24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,d1772004f29d81f4c7cbb62ea71d2f230643abfb@65.108.150.175:24003,b591ef22e0c2082eb76dcac5ead95be55d01b695@65.109.178.147:26656,1f704611e8aa4a53504fac1b80eb55c876dae8bd@65.108.13.154:30656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,e232ba0d11839944d92b9035ef98445a0fb94c9f@95.214.53.37:12656,0d08a1b452e6d7ccdfbc9b54658b5f9ed24eff7b@135.181.138.160:29956,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:19956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
