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

**live-peers** (29)
```bash
peers="14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,0a528da95ca8025ef4043b6e73f1e789f4102940@176.103.222.22:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,e5aff8690b3fc34f81c1792d56ba5d182cce68e9@65.109.116.204:21156,92f8e4caaadb2f00c95e03068933f2045a93e910@65.109.65.163:21156,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,25da069c4dca143029ddae47bf2b7de69c2a8678@65.108.9.164:21156,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,0e0e01f932a124c45f7f8600e38dba445b5f5dc4@65.108.226.183:19956,464e98fa27165f3a13f4173c0ecfbe71ce8f1bf2@167.86.94.71:36656,f9af0186eec9a88a5a657deb9a7deff34c05d99f@86.111.48.156:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,491de3dfd0b52fe42768ca6f6cf534fc08c6f691@141.98.112.138:26656,2da2e10009a11cbdd56f7f272186eef06d805ef7@178.63.26.94:44656,5b337f7ba27e2fdd27918be18af93f8728034267@65.108.41.168:26656,64df498c92b9ccaf78012229d399aa34a014f087@65.109.122.105:56659,2c2353c872b0c5af562c518b1aa48a2649a4c927@65.108.199.62:11656,1f704611e8aa4a53504fac1b80eb55c876dae8bd@65.108.13.154:30656,bb8c8cea499a1fa7e97922b5a9882c2360c6575a@176.103.222.21:26656,71f6af45c867266f81d81193013fcb4137351355@194.163.155.84:56656,0314d53cc790860fb51f36ac656a19789800ce5c@176.103.222.20:26656,e0f25590f8074b4ea70f069f9be332b19f81f344@23.88.70.109:15656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,2162e7a8a1d0ec9ef9e3d952881c24222d16dcaf@86.48.30.243:44656,e7963fb84a34d1828f18a3573d52414c8fc4cca7@95.70.160.37:26656,bd1e1f8df77e7b61200c490c9fabe6bbc4412d4e@91.223.3.144:26856,e232ba0d11839944d92b9035ef98445a0fb94c9f@95.214.53.37:12656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
