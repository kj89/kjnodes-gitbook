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

**live-peers** (21)
```bash
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,0a528da95ca8025ef4043b6e73f1e789f4102940@176.103.222.22:26656,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,25da069c4dca143029ddae47bf2b7de69c2a8678@65.108.9.164:21156,e5aff8690b3fc34f81c1792d56ba5d182cce68e9@65.109.116.204:21156,35f045092f9c51ab743eec194438b91ecf8ce69e@65.109.116.22:11134,fb2b9d41678f3d1c9c0bdef1a87f2037b6b0088a@146.19.24.252:26666,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,4e0a2772bb3672e54c2ea655c30abdac62191f14@45.84.138.66:18656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,0d6983bcd192c0b4a0f61e6d849c152704e2f017@91.107.148.5:26656,125935f63c123b6891b014ffc071fbf781270771@23.88.74.54:11656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,d5f51ff7adf797e7e4be5f303e75686f6d277886@213.239.207.165:29556,8a20f8f798c5073f0867812e691f54b5cd0dd65d@109.123.242.188:26656,5f04e56cabc20ab2e94b03022f024a310dfdf840@85.10.198.169:11656,92f8e4caaadb2f00c95e03068933f2045a93e910@65.109.65.163:21156,57d64cbf5a16820aa9a0582335705f37dde4c18b@190.15.217.229:26656,4732ed188fbe7603f81d9f4c825397277bb72217@5.75.235.195:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
